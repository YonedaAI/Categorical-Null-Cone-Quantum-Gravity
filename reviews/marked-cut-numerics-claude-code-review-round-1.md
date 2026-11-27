**Delete everything after `check_optics(1, 0.3, 1.6)`: the review launcher as shown is part of the checker file and runs on every invocation.**

## Fix list

| # | Severity | Finding | Fix |
|---|---|---|---|
| 1 | **Blocking** | As shown in the source, the `import os,subprocess,…` block after the `__main__` guard is module-level code. Each `uv run` of the checker would require `claude` auth, start a paid `claude -p` subprocess and overwrite `reviews/marked-cut-numerics-claude-code-review-round-1.md`. It also fails on any machine without that CLI. | Move it to a separate script outside `verification/`. |
| 2 | Minor | `check_optics` never asserts the stated precondition that u is before the first conjugate point (κu < π). The current fixtures meet it (max κu = 1.6), but a later fixture could silently stop testing the claimed regime. | Add `if kappa and kappa*outer >= pi: raise ValueError(...)`. |
| 3 | Minor | RK45 at `rtol=1e-12` is checked against `rel_tol=1e-10`. On these short intervals the global error should stay under that margin, but it isn't guaranteed. | Use `method="DOP853"`, or loosen the check to `rel_tol=1e-9`. |

## Verified by hand: both halves are mathematically correct

1. **State normalization:** |ψ|² = (2πσ²)^(-1/2) e^{-(q−c)²/2σ²}, so ψ is normalized.
2. **Operator ordering:** (M T ψ)(q) = e^{ibq} ψ(q+a), so `shift=0` is right. (T M ψ)(q) = e^{ib(q+a)} ψ(q+a), so `shift=a` is right. This gives **T M = e^{iab} M T**, which matches the `U M` exact value.
3. **Closed form:** completing the square gives ∫ψ̄(q)ψ(q+a)e^{ibq} = exp(−a²/8σ² − σ²b²/2 + i[b(c−a/2)+pa]). This is exactly `expected`.
4. **Fixtures:**
   - Fixture 1 (a = b = √π) gives e^{iab} = −1, a real sign flip. It is a sharp test of ordering.
   - Fixture 2 sets c, p, a and b to non-zero values, so every phase term is used.
5. **Optics:** x = sinh(κu)/κ and y = sin(κu)/κ, so the area is sinh·sin/κ². The κ = 0 branch, u², is right.
6. **API usage is valid for SciPy 1.14.1:**
   - `quad_vec` accepts infinite limits, complex values and `full_output` (`info.success`).
   - `solve_ivp` accepts a tuple return and a sorted `t_eval` inside the span.
   - `cmath.isclose` handles both complex and real values.
   - `zip(strict=)` is fine on Python 3.12.

**Not verified:** I had no tool access, so I did not run `uv run --python 3.12 verification/check_marked_cut.py`. The pass/fail of the 1e-12 quadrature and 1e-10 comparison tolerances has not been observed. Run it once after fix #1 and confirm 4 expectation lines and 3 area lines print.

VERDICT: NEEDS_FIX
