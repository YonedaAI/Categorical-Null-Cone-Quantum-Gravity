# /// script
# requires-python = ">=3.10"
# dependencies = ["beautifulsoup4==4.14.3"]
# ///
"""Build a PDF and a full HTML reading edition from the same LaTeX sources."""
import argparse
import shutil
import subprocess
import tempfile
from pathlib import Path

from bs4 import BeautifulSoup, Comment

from build_site import PAPERS, ROOT, edition_hash


def element(doc, tag_name, text=None, **attrs):
    node = doc.new_tag(tag_name, attrs=attrs)
    if text:
        node.string = text
    return node


def render(slug):
    destination = ROOT / "website/read" / slug
    with tempfile.TemporaryDirectory() as directory:
        work = Path(directory)
        for source in (ROOT / "papers/latex").glob("*.tex"):
            shutil.copy2(source, work / source.name)
        print_build = subprocess.run(["latexmk", "-pdf", "-halt-on-error", "-interaction=nonstopmode",
                                      "-outdir=print", f"{slug}.tex"], cwd=work, capture_output=True, text=True)
        if print_build.returncode:
            raise SystemExit(print_build.stdout + print_build.stderr)
        paper_pdf = work / "print" / f"{slug}.pdf"
        run = subprocess.run(["make4ht", "-u", "-f", "html5", f"{slug}.tex", "mathml,charset=utf-8"],
                             cwd=work, capture_output=True, text=True)
        if run.returncode or "[ERROR]" in run.stdout or "[ERROR]" in run.stderr:
            raise SystemExit(run.stdout + run.stderr)
        doc = BeautifulSoup((work / f"{slug}.html").read_text(), "html.parser")
        for comment in doc.find_all(string=lambda text: isinstance(text, Comment)):
            comment.extract()
        for heading in doc.select("h3.sectionHead,h3.likesectionHead,h3.abstracttitle"):
            heading.name = "h2"
        for heading in doc.select("h4.subsectionHead,h4.likesubsectionHead"):
            heading.name = "h3"

        for heading in doc.select("h5.subsubsectionHead,h5.likesubsubsectionHead"):
            heading.name = "h4"

        title = doc.select_one(".titleHead")
        title_break = title.find("br")
        if title_break:
            series = element(doc, "p", **{"class": "series-label"})
            for node in list(title_break.next_siblings):
                series.append(node.extract())
            title_break.decompose()
            title.insert_before(series)
        for table in list(doc.find_all("table")):
            if table.find_parent("table"):
                continue
            frame = element(doc, "div", **{"class": "mathframe"})
            table.wrap(frame)

        for display in doc.select('math[display="block"]'):
            if display.find_parent(class_="mathframe"):
                continue
            frame = element(doc, "div", **{"class": "mathframe"})
            display.wrap(frame)

        for inline in doc.select('math[display="inline"]'):
            if not inline.find_parent(class_="mathframe"):
                inline.wrap(element(doc, "span", **{"class": "inline-math"}))

        doc.head.append(element(doc, "link", rel="stylesheet", href="/assets/site.css"))
        doc.head.append(element(doc, "link", rel="stylesheet", href="/assets/reader.css"))
        abstract = " ".join(doc.select_one(".abstract p").stripped_strings)
        description = " ".join(abstract.split())
        if len(description) > 250:
            description = description[:250].rsplit(" ", 1)[0] + "…"
        doc.head.append(element(doc, "meta", name="description", content=description))
        doc.head.append(element(doc, "meta", property="og:description", content=description))
        doc.head.append(element(doc, "meta", property="og:title", content=title.get_text(" ", strip=True)))
        doc.head.append(element(doc, "meta", property="og:image", content=f"/assets/og/{slug}.png"))
        doc.head.append(element(doc, "meta", name="twitter:card", content="summary_large_image"))
        doc.head.append(element(doc, "meta", name="paper-edition", content=edition_hash(work, slug, paper_pdf)))
        doc.body["class"] = "reader"
        main = element(doc, "main", id="text")
        for node in list(doc.body.contents):
            main.append(node.extract())
        nav = element(doc, "nav", **{"class": "reader-nav", "aria-label": "Paper navigation"})
        nav.append(element(doc, "a", "← Research series", href="/#papers"))
        nav.append(element(doc, "a", "Download PDF ↓", href=f"/papers/{slug}.pdf"))
        doc.body.append(element(doc, "a", "Skip to paper", href="#text", **{"class": "skip"}))
        doc.body.append(nav)
        doc.body.append(main)
        doc.body.append(element(doc, "script", src="/assets/reader.js", defer=""))
        contents = element(doc, "details", **{"class": "contents"})
        contents.append(element(doc, "summary", "Contents"))
        links = element(doc, "ul", role="list")
        for heading in main.select(".sectionHead[id],.likesectionHead[id]"):
            item = element(doc, "li")
            label = " ".join(heading.stripped_strings)
            item.append(element(doc, "a", label, href="#" + heading["id"]))
            links.append(item)
        contents.append(links)
        main.select_one(".maketitle").insert_after(contents)
        if not main.select("math") or not main.select_one(".abstract") or not links.select("a"):
            raise ValueError(f"Incomplete TeX4ht output for {slug}")
        staged = work / "reader"
        staged.mkdir()
        for tag, key in [("img", "src"), ("link", "href")]:
            for node in doc.find_all(tag):
                resource = node.get(key, "")
                if resource and "/" not in resource:
                    shutil.copy2(work / resource, staged / resource)
        (staged / "index.html").write_text(str(doc) + "\n")
        destination.parent.mkdir(parents=True, exist_ok=True)
        if destination.is_dir():
            shutil.rmtree(destination)
        shutil.copytree(staged, destination)
        pdf_dir = ROOT / "papers/pdf"
        pdf_dir.mkdir(exist_ok=True, parents=True)
        shutil.copy2(paper_pdf, pdf_dir / paper_pdf.name)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("papers", nargs="+", choices=PAPERS)
    for paper in parser.parse_args().papers:
        render(paper)
