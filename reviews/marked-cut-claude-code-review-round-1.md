**Optional first edit:** add a `norm_phase` lemma (or reword "bounded"). It is the only gap I found, and it is low severity.

## Review of `lean/Cmrps/MarkedCut.lean`, the `Cmrps.lean` import and the README row

**Result: 8 of 8 declarations are mathematically correct, and their statements match the README row and the paper's sign conventions.** I checked the math by hand; I did not rebuild, so the compile status relies on your native `lake build`.

| Item | Check | Status |
|---|---|---|
| `logReading` | It is `log(r²·w/ref)`. With `w = 4π/(8πG)` and `ref = K_*` it equals Q = log(K/K_*) from the paper | ✅ |
| `logReading_rescale` | `(f r)²w/ref = f²·(r²w/ref)`, so the reading moves by `+2 log f`. All four positivity hypotheses are used | ✅ |
| `phase`, `phase_add` | `exp(ixI)`, and it turns sums into products | ✅ |
| `waist_phase_flip` | With `t = π/(2 log f)` the shift is `t·2 log f = π`, which flips the sign. `1 < factor` makes log f > 0, so `t` is defined | ✅ |
| `exists_waist_phase_ne` | `-p ≠ p` holds because `exp ≠ 0` | ✅ |
| `probe_product` | M_t T_a M_u T_b = e^{iua} M_{t+u} T_{a+b}. This matches U(a)M(b)=e^{iab}M(b)U(a) and V(a,b)V(c,d)=e^{iad}V(a+c,b+d) in `marked-cut.tex` | ✅ |
| `onFirst_injective` | The argument picks `Ψ = ψ ∘ fst` and evaluates at `(x, z)`. It is correct, and the hypothesis is needed: if Z is empty, every map collapses to the same one. It proves faithfulness on raw maps only, and the text claims nothing more | ✅ |
| `lifted_probe_product` | Proved by definitional equality, reducing to `probe_product` at the fibre `p.2` | ✅ |
| `probe_tensor` | `e^{itx}ψ(x+a)·s(z)` | ✅ |
| Import | `public import Cmrps.MarkedCut` is added in `lean/Cmrps.lean` | ✅ |
| README cache line | It lists `Log.Basic` and `Trigonometric.Basic`, which match the module's two imports | ✅ |
| Physics or Hilbert-space overclaim | None. The module header disclaims measure, Hilbert completion and field equations, and README line 25 restricts the scope to pointwise functions | ✅ |

## Actionable items (none blocking)

1. **"Bounded" is asserted but not machine-checked.** It appears in the README row ("A bounded phase distinguishes the two readings") and in the docstring of `exists_waist_phase_ne`. The table is introduced as machine-checked claims, so pick one:
   - add `theorem norm_phase (x : ℝ) : ‖phase x‖ = 1` (via `Complex.norm_exp_ofReal_mul_I`) and list it in the README row, or
   - change "bounded" to "unit phase" in both places.
2. **Cosmetic wording.** The `probe_tensor` docstring says "Extending a readout by a spectator factor", but `ψ` is an arbitrary function, not the log readout. "Extending a function by a spectator factor" would be accurate.

VERDICT: PASS
