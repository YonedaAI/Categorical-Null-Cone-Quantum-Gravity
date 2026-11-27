**Run `git check-ignore -v papers/pdf/*.pdf papers/latex/*.tex website/read/*/index.html` before the first push.** If nothing prints, the Vercel build has the inputs it needs. The repo has no commits yet and `.gitignore`/`.vercelignore` weren't in the packet, so I couldn't check this step.

## Result

**No blockers.** The earlier failure, missing PDFs, is fixed, and the evidence covers it:

| Check | Evidence | Status |
|---|---|---|
| Routes | Home plus 4 readers return 200 at 5 widths (320–1280px) | ✅ |
| Horizontal overflow, MathML errors, images, in-page anchors | Checked on every page at every width | ✅ |
| PDFs | 4 of 4 return 200 and start with `%PDF-` (20, 12, 20 and 9 pages) | ✅ |
| Reader and PDF in sync | `edition_hash` ties each reader to its 2 TeX inputs and its PDF; `build_site` fails fast if they drift | ✅ |
| Share image URLs | The regex rewrites `content="/assets/og/…"` regardless of attribute order (bs4 sorts attributes) | ✅ |
| `trailingSlash: true` | Every reader link ends in `/`; `.pdf` paths are exempt from the redirect | ✅ |
| Skip links, focus outlines, nav labels, heading order on home | All present | ✅ |
| Scrollable formulas | Become keyboard-focusable only when they actually overflow | ✅ |

## Should-fix (small, not blocking)

1. **Brand link name doesn't match its visible text (WCAG 2.5.3).** The visible text is "YonedaAI Research Collective", but `aria-label="YonedaAI research series home"` replaces it, so speech-control users can't say the label they see. Fix: drop the `aria-label`, or use `aria-label="YonedaAI Research Collective home"`.
2. **External links aren't covered by `check_site`.** Three links have not been verified:
   - the GitHub repository link (2 of them; the repo has no commits yet);
   - the two yonedaai.com PDFs;
   - arXiv `2611.34924v1`.

   Open each once after pushing.

## Conditional (depends on paper content I couldn't see)

| If the papers contain… | What goes wrong | Fix |
|---|---|---|
| Unnumbered sections (`likesectionHead`) or appendices | The numbering in the Contents `<ol>` stops matching the section numbers; "A Proof…" would show as "7. A Proof…" | Use `<ul>`, or keep the original number in the text |
| `\subsubsection` | `h5` comes straight after `h3`, skipping a heading level | Also rename `h5.subsubsectionHead` to `h4` |
| `\input` of other `.tex` files, a `.bib`, or figure files | `edition_hash` won't notice edits to them; `render` copies only `*.tex` | Add them to the hash and the copy |

## Optional enhancements

- Readers have no `og:description` or `<meta name="description">`.
- `↗` marks both internal links (paper rows, "Read the perspective") and external ones, so it doesn't tell readers which links leave the site.
- The figcaption reads aloud as "A causal diamond Null sheets meet…" with no pause; add a period or a separator.
- No favicon.
- The `paper-edition` check matches a raw substring and depends on bs4's attribute order. Parsing the `<meta>` tag would be more robust.
- On preview deploys, share-image URLs point to the production domain. That's fine once production exists.

VERDICT: PASS
