**Next action:** build the two missing PDFs, then re-run the site build.

```sh
for p in foundations gluing; do
  (cd papers/latex && latexmk -pdf -halt-on-error -outdir=../../build/tex/$p $p.tex)
  cp build/tex/$p/$p.pdf papers/pdf/$p.pdf
done
python3 scripts/build_site.py
```

## Blocking issue (1)

| # | Where | Issue | Impact | Fix |
|---|---|---|---|---|
| 1 | `papers/pdf/` and `scripts/build_site.py:13-15` | **`foundations.pdf` and `gluing.pdf` don't exist.** Only `reduction.pdf` and `synthesis.pdf` are there. | `build_site.py` exits with "Missing publication artifact", so **the Vercel deploy fails**. On any older deploy, two "Download PDF ↓" links return 404. | Run the commands above, then `uv run scripts/check_site.py http://127.0.0.1:8000`. |

The `foundations` reader appeared while I was reviewing, so a regeneration may still be running. If it is, re-check after it finishes.

## Non-blocking issues (9), by impact

| # | Where | Issue | Impact | Fix |
|---|---|---|---|---|
| 2 | `render_reader.py:54-63` | Every displayed equation and table is wrapped in a frame with `role="region"`, `tabindex="0"` and the same label. That is **70 frames across the 4 readers** (23 in foundations). | The screen-reader landmark list fills with identical "Displayed equation" entries. Keyboard users have to tab through every equation. | Give the role and tabindex only to frames that actually overflow (`scrollWidth > clientWidth`), or drop `role="region"`. |
| 3 | `site.css:8` | The orange focus ring `#de8512` has about **2.9:1** contrast against `#f2f1eb` and `#f6f5ef`. The paper list and all reader pages use these light backgrounds. | Below the 3:1 that WCAG 1.4.11 requires for focus indicators. It is fine (about 5.3:1) on the dark sections. | Use a darker ring on light backgrounds, e.g. `#a85400`. |
| 4 | `reader.css:27` | `.inline-math` scrolls horizontally but cannot take keyboard focus. `overflow-y:hidden` can clip tall subscripts and superscripts. | Long inline formulas are unreachable for keyboard users and may be visibly cut off. | Allow wrapping, or make overflowing spans focusable, and remove `overflow-y:hidden`. |
| 5 | `check_site.py` | No check for failed CSS, font or other subresource requests. Only `img` elements are checked. | A missing `/assets/fonts/*.woff2` or reader CSS file would still pass. | Record every `requestfailed` event and every response with status ≥ 400, and fail on any. |
| 6 | `build_site.py` | Nothing checks that the committed readers and PDFs match the current `.tex` sources. | Stale readers or PDFs can deploy without any warning. | Store a source hash in each generated artifact, or fail when a `.tex` file is newer than its reader or PDF. |
| 7 | `build_site.py:16`, `render_reader.py:93-98` | Neither script clears its output first (`dist/`, `website/read/<slug>/`). | Removed or renamed files stay behind. Locally, a deleted reader keeps "passing". | Run `shutil.rmtree` on the output before copying. |
| 8 | `diamond_figure.py` | No PEP 723 header declaring Pillow, unlike the other scripts. | `uv run scripts/diamond_figure.py` fails, so the figure can't be reproduced the way the README describes. | Add a `# /// script` block with `dependencies = ["pillow==…"]`. |
| 9 | `.gitignore` | `build/` (the README's LaTeX output directory) and `__pycache__/` are not ignored. `scripts/__pycache__/` already exists. | `git add .` would commit build artifacts and `.pyc` files. | Add `build/` and `__pycache__/` to `.gitignore`. |
| 10 | `reader.css:6` | The `h1.titleHead br` rule targets an element that `render_reader.py:49` removes. | Dead CSS, no visible effect. | Delete the rule. |

## Checked with no issues

- **Mathematics and figure:** q is the future tip at the top and p the past tip at the bottom, matching D(p,q) = J⁺(p) ∩ J⁻(q). The waist circle is the corner S. The alt text and caption agree with the image, and the label positions match the PNG geometry.
- **Content:** source citations are consistent across the home page, `context/README.md` and the `.tex` bibliographies. The volume numbering (Parts I–III plus the perspective, then IV–VII) is consistent.
- **Reader markup:**
  - Viewport meta is present.
  - Each reader has one `h1`.
  - Headings go h2 → h3 with no skipped levels.
  - Table-of-contents and cross-reference anchors resolve.
  - There are no `<merror>` elements.
  - The only local asset is `<slug>.css`, which is copied.
- **Links:** routes, `trailingSlash` and PDF paths are consistent between `vercel.json`, the home page and the readers.

VERDICT: NEEDS_FIX
