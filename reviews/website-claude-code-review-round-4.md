**Next action: deploy as-is. All three fixes keep the existing behavior.**

| Fix | Where | Behavior check | Result |
|---|---|---|---|
| Explicit list role | `render_reader.py`: `element(doc, "ul", role="list")` | `new_tag(attrs={"role":"list"})` writes the attribute. This restores list semantics that Safari drops when `list-style:none` is set (`.reader .contents ul`). The contents links, their hrefs and the `links.select("a")` completeness guard are unchanged. | ✅ |
| h4 size | `reader.css`: `.reader h4{font-size:1.3rem}` | Same specificity as `.reader :is(h2,h3,h4)` (0,1,1), but that rule sets no font-size, so the two don't conflict. The rule sits last, after the h3 rule at 1.65rem, so the hierarchy holds: h2 > h3 (1.65rem) > h4 (1.3rem). The h5→h4 rename runs after the h4→h3 pass and selects by class, so no heading is renamed twice. | ✅ |
| Guard before truncating the abstract | `render_reader.py`: `if len(description) > 250:` | Abstracts of 250 characters or fewer are no longer given a `…`. Longer ones are cut at the last word boundary. If the first 250 characters contain no space, `rsplit` returns the whole string, so nothing crashes. | ✅ |

**Optional follow-ups (none of them block):**
1. The home page `.sources ul` also uses `list-style:none` but has no `role="list"`. If the audit meant that list too, add `role="list"` in `index.html`.
2. If `.abstract p` is missing, `select_one(...).stripped_strings` raises `AttributeError` before the "Incomplete TeX4ht output" check runs. The build still stops, just with a less helpful error. This was already the case before these fixes.

I reviewed the sources only and ran nothing. Browser and PDF evidence is your packet's: 5 widths × 5 routes passed, and 4 of 4 PDFs passed.

VERDICT: PASS
