**Next action: push the reviewed proof and site together, then run `uv run scripts/check_site.py https://<production-host>/`. The live run is the release gate for `MarkedCut.lean`.**

## Blockers

None. Round five's two blockers are fixed in the code:

| Round-5 blocker | Fix in round 6 | Where | Would it catch a regression after publication? |
|---|---|---|---|
| A missing GitHub link could pass | The five status hrefs are compared as a multiset, so a missing, extra, duplicated or changed href fails | `check_site.py` `check_status` | Yes |
| The status href check only caught missing links | Non-local hosts send a HEAD request to each of the 3 exact `blob/main/...` URLs. Each must return 200 and must not redirect (`response.url == url`) | `check_site.py` source loop | Yes. A proof missing from `main`, a private repo, a renamed repo or a moved file all fail |

## Checked against the brief

1. **Status section is accessible.** It is a labelled `region`. The nav jump is checked to be in the first viewport and to land on `#status`. The two `ul` lists have `role=list` and labels. The `#status`, `#papers`, `#program`, `#main` and `#title` anchors all exist.
2. **Exactly 5 links.** Read note, note PDF, `MarkedCut.lean`, the manuscript comparison and `ClassicalImage.lean`. They match `expected` exactly.
3. **Edition hashes.** The hash binds `preamble.tex`, `<slug>.tex` and the PDF. bs4's default formatter sorts attributes, so the `content="…" name="paper-edition"` lookup matches what `render_reader.py` writes. All 5 slugs are enforced before anything is copied.
4. **Share cards.** Each page has 1 `og:image`. It is made absolute by the build (production uses `VERCEL_PROJECT_PRODUCTION_URL`, preview uses `VERCEL_URL`). The checker requires a matching path, http(s) and PNG magic bytes. The `marked-cut` card is in the generator list.
5. **Private context is excluded twice.** `dist` is built only from `website/` plus `papers/pdf`, and `.vercelignore` also drops `context/`, `reviews/`, `prompts/`, `references/` and `settings/`. `context/manuscript-comparison.md` is linked only on GitHub, which is the intended route.
6. **Link types.** Site links are root-relative. Repository links are absolute GitHub URLs. No repo-relative paths leak onto the site.
7. **Science wording matches the brief.** Order-dependent phase, log area reading against dilation, positive-area model, retained mark, an independent (spectator) system, and the gravitational correspondence stated as open.
8. **Mobile widths.** 5 widths × 6 routes. The checks cover overflow, MathML `merror`, overflowing equation frames that cannot be reached, images, anchors and PDFs.

## Optional observations (not blocking)

| # | Observation | Suggested fix |
|---|---|---|
| 1 | A GitHub 429 rate limit during the HEAD check fails the release with no clear cause | One retry with backoff, and print the status code (already printed) |
| 2 | The `↗` glyph in link text is read aloud ("north east arrow") in the status, nav and sources links | Wrap it as `<span aria-hidden="true">↗</span>`, as `.button` already does |
| 3 | `<cite>Observables as Cohomology</cite>` has no link, and the title does not appear elsewhere on the page | Link it, or name which part or manuscript it comes from |
| 4 | A local check served on a port other than 8000 builds og URLs pointing at `:8000` | Document `SITE_ORIGIN=http://localhost:<port>` for local runs |
| 5 | The live check proves `MarkedCut.lean` is published, not that it compiles | Add `lake build` to CI separately |

VERDICT: PASS
