# /// script
# requires-python = ">=3.10"
# dependencies = ["playwright==1.56.0"]
# ///
"""Check publication routes, anchors and math at mobile and desktop widths."""
import argparse
from urllib.parse import urljoin, urlsplit

from playwright.sync_api import sync_playwright

from build_site import PAPERS, ROOT


REPOSITORY = "https://github.com/YonedaAI/Categorical-Null-Cone-Quantum-Gravity/blob/main/"
STATUS_SOURCES = ("context/manuscript-comparison.md", "lean/Cmrps/ClassicalImage.lean", "lean/Cmrps/MarkedCut.lean")


def check_status(page):
    jump = page.get_by_role("navigation", name="Main", exact=True).get_by_role(
        "link", name="Research status", exact=True
    )
    section = page.get_by_role("region", name="Research status", exact=True)
    box = jump.bounding_box()
    if not box or box["y"] < 0 or box["y"] + box["height"] > page.viewport_size["height"]:
        raise ValueError("Research status is unreachable from the initial viewport")
    jump.click()
    if urlsplit(page.url).fragment != "status" or not section.evaluate(
        "el => el.getBoundingClientRect().top >= -1 && el.getBoundingClientRect().top < innerHeight"
    ):
        raise ValueError("Research status navigation did not reach the section")
    expected = ["/read/marked-cut/", "/papers/marked-cut.pdf", *(REPOSITORY + path for path in STATUS_SOURCES)]
    links = section.get_by_role("link").evaluate_all("links => links.map(link => link.getAttribute('href'))")
    if sorted(expected) != sorted(links):
        raise ValueError(f"Unexpected research status links: {links}")
    for paper in PAPERS:
        if not page.locator(f'#papers a[href="/read/{paper}/"]').is_visible():
            raise ValueError(f"Missing library entry for {paper}")


def check(base):
    routes = ["/", *(f"/read/{paper}/" for paper in PAPERS)]
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(channel="chrome")
        try:
            page = browser.new_page()
            resource_errors = []
            page.on("requestfailed", lambda request: resource_errors.append((request.url, request.failure)))
            page.on("response", lambda response: resource_errors.append((response.url, response.status))
                    if response.status >= 400 else None)
            for width in (320, 375, 430, 768, 1280):
                page.set_viewport_size({"width": width, "height": 900})
                for route in routes:
                    response = page.goto(urljoin(base, route))
                    if response is None or response.status != 200:
                        raise ValueError(f"Failed to open {route}")
                    page.evaluate("document.fonts.ready")
                    problems = page.evaluate("""() => {
                      const root = document.documentElement;
                      const issues = [];
                      if (root.scrollWidth > root.clientWidth + 1) issues.push('horizontal overflow');
                      if (document.querySelector('merror')) issues.push('invalid MathML');
                      if (!document.querySelector('main h1')) issues.push('main heading missing');
                      if (document.querySelector('.reader') && !document.querySelector('main math'))
                        issues.push('no rendered mathematics');
                      for (const box of document.querySelectorAll('.mathframe, .inline-math')) {
                        if (box.scrollWidth > box.clientWidth + 1 && (box.tabIndex !== 0 ||
                            !box.getAttribute('aria-label') || !['auto','scroll'].includes(getComputedStyle(box).overflowX)))
                          issues.push('inaccessible overflowing equation');
                      }
                      for (const image of document.images)
                        if (!image.naturalWidth) issues.push('missing image: ' + image.src);
                      for (const anchor of document.querySelectorAll('a[href^="#"]')) {
                        const id = decodeURIComponent(anchor.hash.slice(1));
                        if (id && !document.getElementById(id) && !document.getElementsByName(id).length)
                          issues.push('missing anchor: ' + id);
                      }
                      return issues;
                    }""")
                    if resource_errors:
                        raise ValueError(f"{width}px {route}: resource errors {resource_errors}")
                    if problems:
                        raise ValueError(f"{width}px {route}: {problems}")
                    if route == "/":
                        check_status(page)
                    if width == 320:
                        card = "series" if route == "/" else route.split("/")[2]
                        expected_path = f"/assets/og/{card}.png"
                        image = page.locator('meta[property="og:image"]').get_attribute("content") or ""
                        image_url = urlsplit(image)
                        if image_url.scheme not in {"http", "https"} or not image_url.netloc or image_url.path != expected_path:
                            raise ValueError(f"Missing share image for {route}")
                        result = page.request.get(image)
                        if result.status != 200 or not result.body().startswith(b"\x89PNG\r\n\x1a\n"):
                            raise ValueError(f"Invalid share image at {image}")
                print(f"{width}px: home and all {len(PAPERS)} readers passed")
            for paper in PAPERS:
                url = urljoin(base, f"/papers/{paper}.pdf")
                response = page.request.get(url)
                if response.status != 200 or not response.body().startswith(b"%PDF-"):
                    raise ValueError(f"Invalid PDF at {url}")
            print(f"All {len(PAPERS)} PDF downloads passed")
            local = urlsplit(base).hostname in {"localhost", "127.0.0.1", "::1"}
            for path in STATUS_SOURCES:
                if local:
                    if not (ROOT / path).is_file():
                        raise ValueError(f"Missing research source at {path}")
                else:
                    url = REPOSITORY + path
                    response = page.request.head(url)
                    if response.status != 200 or response.url != url:
                        raise ValueError(f"Unpublished research source at {url}: {response.status}")
            print(f"All {len(STATUS_SOURCES)} research sources verified {'locally' if local else 'on GitHub'}")
        finally:
            browser.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("base_url", help="An HTTP(S) origin serving the built site")
    check(parser.parse_args().base_url)
