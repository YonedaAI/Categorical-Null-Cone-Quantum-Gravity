# /// script
# requires-python = ">=3.10"
# dependencies = ["playwright==1.56.0"]
# ///
"""Check publication routes, anchors and math at mobile and desktop widths."""
import argparse
from urllib.parse import urljoin

from playwright.sync_api import sync_playwright

from build_site import PAPERS


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
                print(f"{width}px: home and all {len(PAPERS)} readers passed")
            for paper in PAPERS:
                url = urljoin(base, f"/papers/{paper}.pdf")
                response = page.request.get(url)
                if response.status != 200 or not response.body().startswith(b"%PDF-"):
                    raise ValueError(f"Invalid PDF at {url}")
            print(f"All {len(PAPERS)} PDF downloads passed")
        finally:
            browser.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("base_url", help="An HTTP(S) origin serving the built site")
    check(parser.parse_args().base_url)
