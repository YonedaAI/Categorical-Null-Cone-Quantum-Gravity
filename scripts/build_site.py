"""Assemble the static site from the reading editions and the canonical PDFs."""
from pathlib import Path
import hashlib
import os
import re
import shutil

ROOT = Path(__file__).resolve().parents[1]
PAPERS = ("foundations", "reduction", "gluing", "synthesis")


def edition_hash(source_dir, slug, pdf):
    """Bind the reader to its two local TeX inputs and the PDF built alongside it."""
    digest = hashlib.sha256()
    for path in (source_dir / "preamble.tex", source_dir / f"{slug}.tex", pdf):
        data = path.read_bytes()
        digest.update(len(data).to_bytes(8, "big"))
        digest.update(data)
    return digest.hexdigest()


def main():
    site = ROOT / "website"
    output = ROOT / "dist"
    for slug in PAPERS:
        for source in (site / "read" / slug / "index.html", ROOT / "papers/pdf" / f"{slug}.pdf"):
            if not source.is_file():
                raise SystemExit(f"Missing publication artifact: {source.relative_to(ROOT)}")
        expected = edition_hash(ROOT / "papers/latex", slug, ROOT / "papers/pdf" / f"{slug}.pdf")
        reader = (site / "read" / slug / "index.html").read_text()
        if f'content="{expected}" name="paper-edition"' not in reader:
            raise SystemExit(f"Rebuild {slug} with uv run scripts/render_reader.py {slug}")
    if output.is_dir():
        shutil.rmtree(output)
    shutil.copytree(site, output)
    project_domain = os.getenv("VERCEL_PROJECT_PRODUCTION_URL") or os.getenv("VERCEL_URL")
    origin = os.getenv("SITE_ORIGIN") or (f"https://{project_domain}" if project_domain else "http://localhost:8000")
    # Home is hand-authored HTML; TeX4ht reading editions serialize attributes in a different order.
    for page in [output / "index.html", *(output / "read" / name / "index.html" for name in PAPERS)]:
        html = page.read_text()
        page.write_text(re.sub(r'(content=")(/assets/og/)', lambda m: m[1] + origin.rstrip("/") + m[2], html))
    pdf_dir = output / "papers"
    pdf_dir.mkdir(exist_ok=True)
    for slug in PAPERS:
        shutil.copy2(ROOT / "papers/pdf" / f"{slug}.pdf", pdf_dir / f"{slug}.pdf")


if __name__ == "__main__":
    main()
