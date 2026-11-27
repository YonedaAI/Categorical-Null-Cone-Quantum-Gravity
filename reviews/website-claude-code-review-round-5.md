**First action: run `git ls-files --error-unmatch lean/Cmrps/MarkedCut.lean`.** If it errors, the status page's Lean link will 404 the moment this deploys.

I reviewed only the code in the brief. No files were changed and I ran nothing locally, so the browser results you reported are taken as given.

## What passes (11 of the 13 areas reviewed)

| Area | Result |
|---|---|
| Status section accessibility | Pass. The section is a region named by its heading. The nav link works. Both lists use `role="list"` and have labels. The section stacks to one column at 740 px or less. |
| Status wording | Pass. It states the order-dependent phase for the log-area reading and dilation, with the mark kept and an independent system added. It says the gravitational correspondence is still open. |
| Five status links on the page | Pass. There are exactly 5, and they match the brief. |
| Supplement and older routes | Pass. `marked-cut` is in `PAPERS`, so the build gate, reader routes and PDF copy all cover it. The four earlier slugs are unchanged. |
| Edition hash | Pass. The reader is rendered from the same bytes (preamble, `.tex`, PDF) that `build_site.edition_hash` hashes. The stored hash matches because bs4's default output sorts attributes, so `content` comes before `name`. |
| Share card | Pass. Git shows only `marked-cut.png` as new, so regenerating did not change the other 5 cards. |
| Site-relative vs repo links | Pass. Readers and PDFs use `/…` paths. Repository material uses absolute GitHub `blob/main` URLs. |
| Private context | Pass for the deployed site. `dist` is a copy of `website/` plus `papers/`, and `.vercelignore` also drops `context/`, `reviews/` and `prompts/` from the upload. |
| Native MathML | Pass. The check fails on any `merror`, and on any reader page with no `main math`. |
| Mobile CSS | Pass. Grid columns use `minmax(0, …)`, and the check fails on any horizontal overflow at all 5 widths. |
| PDF serving | Pass. All 5 are fetched and must return 200 and start with `%PDF-`. |

## Blockers (2)

1. **Make sure the newly linked repository files exist on `main` before deploying.**
   - `lean/Cmrps/MarkedCut.lean` is untracked in the git snapshot, as are its import in `lean/Cmrps.lean`, `papers/latex/marked-cut.tex` and `verification/check_marked_cut.py`.
   - The status link `…/blob/main/lean/Cmrps/MarkedCut.lean` returns 404 until those are pushed.
   - `check_site.py` never looks at the GitHub links, so it would pass anyway.
   - **Fix:** in `scripts/check_site.py`, for each `expected` href under `repo`, strip the prefix and run `subprocess.run(["git","ls-files","--error-unmatch",rel], cwd=ROOT, check=True)`. This must run locally, because `.vercelignore` drops `.git` from the Vercel build. Then commit and push before the production deploy.

2. **Make the status-link check exact.**
   - At `scripts/check_site.py`, `expected.difference(links)` only catches missing links. An extra, wrong or duplicate link still passes, but the brief requires exactly five.
   - **Fix:** `if sorted(links) != sorted(expected): raise ValueError(f"Research status links: {links}")`

## Optional observations (7)

| # | File | Observation | Suggested change |
|---|---|---|---|
| 1 | `build_site.py` / `check_site.py` | On a Vercel preview build, `VERCEL_PROJECT_PRODUCTION_URL` wins, so `og:image` points at production. Production has no `marked-cut.png` until the release ships. The check accepts any host, so it tests production rather than the deployment under test. | Use `VERCEL_URL` when `VERCEL_ENV != "production"`. In the check, require `image_url.netloc == urlsplit(base).netloc` unless a production origin is passed in explicitly. |
| 2 | `build_site.py` | The `content="…" name="paper-edition"` match only works because bs4 sorts attributes. A change in bs4 or the formatter would fail every reader. | Parse the meta tag, e.g. a regex allowing either attribute order. |
| 3 | `edition_hash` | It hashes only `preamble.tex` and `{slug}.tex`, but `render_reader` copies every `*.tex`. A shared `\input` could change without the build gate noticing. | Hash every file the render copies, or list per-paper inputs. |
| 4 | `check_site.py` | Your manual check for scrollable MathML frames is not automated. | Assert that every `.mathframe` with `scrollWidth > clientWidth` has `tabindex="0"` and an accessible name. |
| 5 | `check_site.py` | A served PDF is only tested for the `%PDF-` prefix, not for being the hashed edition. | Compare the sha256 of the served file with `papers/pdf/{slug}.pdf`. |
| 6 | `index.html` | "Download the PDF" doesn't say which PDF when read out of context. | "Download the note (PDF)". |
| 7 | `index.html` | The library row says "An area reading", while the status text and the result are about the log of the area. | "A log-area reading and a dilation acquire a phase…" |

Both blockers are a few lines each. After fixing them, push, rerun `check_site.py`, and the review becomes a PASS.

VERDICT: REVISE
