**Run `lake build Cmrps.ClassicalImage` once to confirm it compiles. I reviewed the source only and did not build it.** The rest of this review is a static read of the code.

## Checks

| Check | Result |
|---|---|
| No `sorry`, `admit`, `axiom` or custom assumptions | ✅ None present |
| `not_surjective_of_noncommuting` logic | ✅ Sound. Pull back `u = f a` and `v = f b`, then `f a * f b = f(ab) = f(ba) = f b * f a` contradicts `hne` |
| Matrix witness | ✅ Correct. `E_ij·E_ji = E_ii` and `E_ji·E_ij = E_jj`; at entry `(i,i)` that is `1` vs `0`, which needs `[Nontrivial R]` and `i ≠ j` |
| Typeclass context | ✅ `Fintype I` and `DecidableEq I` are exactly what `Semiring (Matrix I I R)` needs |
| API name | ✅ `Matrix.single` (formerly `stdBasisMatrix`) is in `Mathlib.Data.Matrix.Basis` |
| Import by `Cmrps.lean` | ✅ `public import Cmrps.ClassicalImage` is present |
| Scope | ✅ A purely algebraic claim about classical (commutative) observables; no quantum-gravity overreach |

## Non-blocking issues

1. **Make the first proof less fragile.** `rw [← map_mul]` with no arguments only works because `rw` happens to match the left-hand `f a * f b` first. If that changes, the next `mul_comm a b` finds no `a * b` and fails. Name the arguments:
   ```lean
   exact hne (by rw [← map_mul f a b, mul_comm a b, map_mul])
   ```
2. **Make the docstring say exactly what is proved.** "A necessary test for identifying…" is vague. The theorem rules out a **surjective** product-preserving map. It does not rule out embedding a classical algebra into a quantum one: commutative subalgebras such as diagonal matrices exist. Suggested wording:
   > A product-preserving map from a commutative observable algebra has commutative image, so it cannot be onto a target with a noncommuting pair, such as `Matrix I I R` with `|I| ≥ 2`.
3. **Optional generalization.** The argument only uses multiplicativity, so the lemma could take `[FunLike F A B] [MulHomClass F A B]` over `CommMagma`/`Mul`. Alternatively, it could expose the stronger `∀ a b, Commute (f a) (f b)` and derive non-surjectivity from that. Neither is needed for the stated scope.
4. **Optional style point.** `public section` is never closed. Lean 4 accepts this at end of file. Add a matching `end` only if the sibling modules (`Pauli`, `Invisible`, …) do.
5. **Not reviewed:** the prompt text also contained the Python driver script. It is outside the Lean scope.

VERDICT: PASS
