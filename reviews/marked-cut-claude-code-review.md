**No change is required. The file can be committed as it is.** The three findings below are optional polish.

## Theorem-by-theorem check (13 of 13 sound)

| # | Declaration | What the proof does | Status |
|---|---|---|---|
| 1 | `logReading_rescale` | Uses `(fr)²w/ref = f²·(r²w/ref)`, then `log_mul` and `log_pow` with nonzero factors. It needs positive `w`, `ref`, `r`, `f` (the `positivity` step uses them). | ✅ |
| 2 | `phase_add` | `exp((x+y)i) = exp(xi)·exp(yi)` | ✅ |
| 3 | `norm_phase` | Uses `Complex.norm_exp_ofReal_mul_I` directly. This adds the unit-norm theorem the earlier review asked for. | ✅ |
| 4 | `phase_shift_halfturn` | `π/δ·(x+δ) = π/δ·x + π`, then `exp(πi) = −1`. `δ ≠ 0` is enforced. | ✅ |
| 5 | `waist_phase_flip` | Sets `δ = 2·log f`, which is nonzero because `1 < f` gives `log f > 0`. | ✅ |
| 6 | `exists_waist_phase_ne` | `−p ≠ p` holds because `p = exp(·) ≠ 0`, using `CharZero.neg_eq_self_iff`. The phase is bounded by #3. | ✅ |
| 7 | `probe_product` | LHS = `φ(tx)·φ(u(x+a))·ψ(x+a+b)` and RHS = `φ(ua)·φ((t+u)x)·ψ(x+a+b)`. They are equal. The docstring places the factor `exp(iua)` correctly. | ✅ |
| 8 | `onFirst_injective` | Evaluates on `Ψ(p) = ψ(p.1)` at `(x, z)`. The spectator label needs to be inhabited, and the witness `z` supplies it. | ✅ |
| 9 | `lifted_probe_product` | The term proof reduces by definition to #7 on the slice `x ↦ Ψ(x, p.2)`. **`Ψ` is an arbitrary joint function, not only a product.** | ✅ |
| 10 | `probe_tensor` | Product-function intertwining, closed by `simp` and `mul_assoc`. | ✅ |
| 11 | `forget_halfturn` | With `t = π/(c₁−c₀)`, `add_sub_cancel` rewrites `c₀+(c₁−c₀)` to `c₁`, so `φ(tc₁) = −φ(tc₀)`. **The average is 0.** | ✅ |
| 12 | `forget_star_mul` | `conj(φ)·φ = exp(conj(xi)+xi) = 1` in each component, so `(1+1)/2 = 1` **for every `t`**. | ✅ |
| 13 | `forget_not_multiplicative` | `ω(v*v) = 1` but `ω(v*)·ω(v) = ω(v*)·0 = 0`. **So `1 ≠ 0`, and multiplicativity fails.** | ✅ |

## Scope and documentation

| Item | Finding |
|---|---|
| Representation scope | The probes act on **all functions `ℝ → ℂ`**. The file never claims L², unitarity or closure. The README sentence "pointwise functions before measure, operator closure, or a gravitational representation" matches this. ✅ |
| Calibration | The area formula is an input (`radius² · weight`), and the README says so explicitly. ✅ |
| Product-function wording | "Intertwines product functions" and the `probe_tensor` docstring now say exactly what is proved. This was the earlier request. ✅ |
| Declaration list | The README table, the axiom report and the source each contain the same 13 names. ✅ |
| Axioms | Only `propext`, `Classical.choice` and `Quot.sound` appear. No physics axioms. ✅ |
| Build | `Cmrps.MarkedCut` and the root module `Cmrps` build: 2013/2013 jobs. ✅ |

## Optional polish (not blocking)

1. **Interpretation of #13.** `forgetPair` is an equal-weight state on the *commutative* algebra ℂ×ℂ. A non-multiplicative state there is simply a mixed state rather than a character. If the paper describes the result as more than "the label-forgetting mixture is not a character," narrow that sentence. The Lean side claims nothing more.
2. **The hypothesis `1 < factor` in #5 and #6 is stronger than needed.** `0 < factor` with `factor ≠ 1` gives `log factor ≠ 0` just as well. This is acceptable as written, because the docstring says "larger waist".
3. **`phase_add` has no docstring.** It is the only declaration without one, which is a cosmetic gap.

VERDICT: PASS
