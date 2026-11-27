**Verdict: the captured response cannot produce a false success or hide a permanent error. No changes needed.**

| Risk | What the code does | Result |
|---|---|---|
| False success | `navigate_source` returns the captured response only when `goto` raised **and** `status >= 400`. Any 2xx or 3xx falls through to the timeout/raise path. | **Cannot happen** |
| Permanent error swallowed | A captured 404, 403 or 410 is handed back to `check_public_source`. That status is not in the retry set, so it raises immediately. | **Still fails** |
| Stale or foreign response | A new listener is set up on every call and removed in `finally`. It only records main-frame navigation responses, so subframes and other subresources are ignored. | **No leakage** |
| Redirect chain ending in an error | The listener keeps the last main-frame response, which is the final status. A 3xx in the middle is never returned on its own. | **Correct** |
| Error response from a redirected URL | `response.url != url` raises at once instead of retrying. That is stricter, and it is still a failure. | **Acceptable** |
| Timeout after a 503 was received | Returns the 503 with its Retry-After, so the retry uses the real header. | **Improvement** |

Non-blocking: a non-timeout `NavigationError` that comes with a captured 5xx gets retried, not raised. That is the intended behaviour, and it is still capped at 3 attempts with a 30-second limit.

VERDICT: PASS
