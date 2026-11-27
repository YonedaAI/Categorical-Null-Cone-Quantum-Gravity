**Action: none needed — the file is correct as written; merge it.**

## Checks performed (all against the on-disk `check_marked_cut.py`, 65 lines)

| Area | What I verified | Result |
|---|---|---|
| Operator order | `M U`: `e^{ibq} ψ(q+a)` → `shift=0`. `U M`: `(Mψ)(q+a) = e^{ib(q+a)} ψ(q+a)` → `shift=a`, extra factor `e^{iab}` (`check_marked_cut.py:27-29`) | Correct |
| Gaussian closed form | Completing the square gives `exp(-a²/8w² − w²b²/2 + i(pa + bc − ab/2))`; the normalization `(2πw²)^{-1/2}·√(2π)w = 1` (`:23-26`) | Matches derivation exactly |
| Integration | `quad_vec` over `(-inf, inf)` with complex output, `full_output=True` → `info.success` is checked, `cmath.isclose` at 1e-10 (`:31-34`) | Sound |
| Jacobi ODE | `x''=κ²x`, `y''=−κ²y`, `B(0)=0`, `B'(0)=I` → `x=sinh(κu)/κ`, `y=sin(κu)/κ`, area `= sinh·sin/κ²`; `κ=0` → `u²` (`:43-54`) | Correct |
| Caustic guard | First zero of `sin(κu)` is at `κu=π`; `kappa*outer >= pi` rejected, `inner>0` keeps `areas[0]>0` for the ratio (`:39, :57`) | Correct |
| Solver accuracy | DOP853, `rtol=1e-12`, `atol=1e-14`, compared at `rel_tol=1e-10` | Adequate margin |
| Input rejection | `width<=0`, `kappa<0`, bad cut order, past-caustic all raise `ValueError`. NaN inputs slip the guards but then fail `isclose` and still raise | Acceptable |
| Python version | `zip(..., strict=True)` needs 3.10; header declares `>=3.10` | Consistent |

## Previous concern: reviewer code in the file
- **Not present.** The file ends at `check_marked_cut.py:60-65`: only the `__main__` block with 5 check calls. No reviewer or test-harness code follows it.

## Optional nits (not blocking)
1. Only `scipy` is pinned; `numpy` comes in transitively unpinned. Pin it if bit-for-bit reproducibility matters.
2. An explicit `math.isfinite` guard would give a clearer error message for NaN/inf inputs than the downstream `isclose` failure does.

**Not verified by me:** I did not run it (read-only review). I'm relying on your report that the pinned `uv` run passed.

VERDICT: PASS
