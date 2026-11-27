**Merge as written. No blocking issue found; the optional items below can wait for a later change.**

## Requirement check

| Requirement | Result | Where in the code |
|---|---|---|
| Real browser navigation | ✅ | `page.goto` on a separate Chrome tab, so GitHub's own resources stay out of the site's `resource_errors` |
| Exact HTTPS source URL | ✅ | `response.url` and `page.url` must equal `REPOSITORY + path`. The scheme comes from the `https://` constant. `check_status` also checks the hrefs against the same constant |
| Local validation kept | ✅ | localhost, 127.0.0.1 and ::1 check the file exists under `ROOT` and never contact GitHub |
| Bounded retries | ✅ | At most 3 attempts. Sleeps are at most 30s each and at most 2 sleeps happen, so the worst case is 60s per source |
| Temporary statuses | ✅ | 408, 429, 500, 502, 503 and 504 retry. Any other status other than 200 fails at once |
| Navigation timeout | ✅ | Caught, waits with the normal backoff, then reported as "navigation timed out" |
| Retry-After as seconds | ✅ | Only ASCII digits count. `max(backoff, n)` never retries earlier than the server asked |
| Retry-After as HTTP date | ✅ | A date without a timezone is read as UTC. A past date falls back to the backoff. Invalid values or overflow fall back to the backoff |
| Delay too long | ✅ | Fails without sleeping and quotes the header in the message |
| Separate failure messages | ✅ | 5 different messages: permanent HTTP status, wrong or redirected URL, 200 without the file title, still unverified after 3 attempts, Retry-After over 30s |
| Regression risk | Low | The checks for site pages, share images, PDFs and the research-status section are unchanged |

## Optional observations (none blocking)

1. **Network errors are not retried.** `page.goto` can raise a plain Playwright `Error` such as `net::ERR_CONNECTION_RESET` or `ERR_HTTP2_PROTOCOL_ERROR`. That is not a `TimeoutError`, so the run stops with a traceback after the first attempt. It still fails loudly (non-zero exit) and never passes silently, so it is only a robustness gap.
   - Fix if wanted: also catch `playwright.sync_api.Error`, set `outcome = f"navigation error: {exc.message}"`, and let the existing retry loop handle it.
2. **The message for `response is None` is misleading.** It says "did not serve the exact source URL … landed on …" even when the URL is exact. This is rare because `goto` only returns `None` for a navigation within the same document.
3. **A throttle sent as 403 counts as permanent.** GitHub's secondary rate limit uses 403 with `Retry-After` on the API. It is not seen on blob pages today. If it ever shows up there, the check would fail at once instead of waiting. Leave it as it is unless it is seen in practice.
4. **Small tidy-up.** `source_page` is never closed. `browser.close()` in `finally` covers it, so there is no functional effect.

## Not verified by me

- I reviewed the code shown in the request only. I did not run it, and I did not compare it with the file on disk.
- The browser and route-interception results are the ones you reported. I did not reproduce them.

VERDICT: PASS
