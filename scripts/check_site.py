# /// script
# requires-python = ">=3.10"
# dependencies = ["playwright==1.56.0"]
# ///
"""Check publication routes, anchors and math at mobile and desktop widths."""
import argparse
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from math import ceil
from time import sleep
from urllib.parse import urljoin, urlsplit

from playwright.sync_api import Error as NavigationError
from playwright.sync_api import TimeoutError as NavigationTimeout
from playwright.sync_api import sync_playwright

from build_site import PAPERS, ROOT


REPOSITORY = "https://github.com/YonedaAI/Categorical-Null-Cone-Quantum-Gravity/blob/main/"
STATUS_SOURCES = ("context/manuscript-comparison.md", "lean/Cmrps/ClassicalImage.lean", "lean/Cmrps/MarkedCut.lean")


def retry_delay(header, backoff):
    """Retry-After accepts either whole seconds or an HTTP date."""
    if header:
        header = header.strip()
        if header.isascii() and header.isdecimal():
            return max(backoff, int(header))
        try:
            retry_at = parsedate_to_datetime(header)
            if retry_at.tzinfo is None:
                retry_at = retry_at.replace(tzinfo=timezone.utc)
            return max(backoff, ceil((retry_at - datetime.now(timezone.utc)).total_seconds()))
        except (TypeError, ValueError, OverflowError):
            pass
    return backoff


def navigate_source(page, url):
    # Chrome can abort navigation on an empty HTTP error page after it has
    # received the status and Retry-After. Keep those actual response headers.
    document = None

    def remember(response):
        nonlocal document
        if response.request.is_navigation_request() and response.frame == page.main_frame:
            document = response

    page.on("response", remember)
    try:
        return page.goto(url, wait_until="domcontentloaded", timeout=20000)
    except NavigationError as error:
        if document is not None and document.status >= 400:
            return document
        if isinstance(error, NavigationTimeout):
            return None
        raise
    finally:
        page.remove_listener("response", remember)


def check_public_source(page, path):
    url = REPOSITORY + path
    for attempt in range(1, 4):
        header = None
        response = navigate_source(page, url)
        if response is None:
            outcome = "navigation timed out"
        else:
            if response.url != url or (response.status == 200 and page.url != url):
                raise ValueError(f"GitHub did not serve the exact source URL {url} (landed on {page.url})")
            if response.status == 200:
                if path.rsplit("/", 1)[-1] not in page.title():
                    raise ValueError(f"GitHub returned HTTP 200 without the expected file title at {url}")
                print(f"GitHub source confirmed (HTTP 200): {url}", flush=True)
                return
            outcome = f"HTTP {response.status}"
            if response.status not in {408, 429, 500, 502, 503, 504}:
                raise ValueError(f"GitHub source check failed: {outcome} at {url}")
            header = response.headers.get("retry-after")
        if attempt == 3:
            raise ValueError(f"GitHub source remains unverified after {attempt} attempts: {outcome} at {url}")
        delay = retry_delay(header, 2 ** attempt)
        if delay > 30:
            raise ValueError(f"GitHub source remains unverified: {outcome} at {url}; Retry-After exceeds 30s ({header})")
        print(f"GitHub source check: {outcome} at {url}; retrying in {delay}s", flush=True)
        sleep(delay)


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
            if urlsplit(base).hostname in {"localhost", "127.0.0.1", "::1"}:
                for path in STATUS_SOURCES:
                    if not (ROOT / path).is_file():
                        raise ValueError(f"Missing research source at {path}")
                print(f"All {len(STATUS_SOURCES)} research sources verified locally")
            else:
                # A separate tab exercises the links as a reader without mixing GitHub
                # subresource traffic into the publication's own resource checks.
                source_page = browser.new_page()
                for path in STATUS_SOURCES:
                    check_public_source(source_page, path)
                print(f"All {len(STATUS_SOURCES)} research sources verified on GitHub")
        finally:
            browser.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("base_url", help="An HTTP(S) origin serving the built site")
    check(parser.parse_args().base_url)
