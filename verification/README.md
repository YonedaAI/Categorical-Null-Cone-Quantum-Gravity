# Lean 4 verification

Run these commands after cloning.

```sh
cd lean
lake exe cache get Mathlib.Algebra.Star.Subalgebra Mathlib.Algebra.Ring.Subring.Basic Mathlib.GroupTheory.GroupAction.Basic Mathlib.Data.Matrix.Mul Mathlib.RingTheory.TwoSidedIdeal.Operations Mathlib.Tactic.Abel
lake build
```

Lean 4.35.0 and the mathlib revision at tag v4.35.0 are pinned in the project. All declarations use the namespace `Cmrps`. The following claims are machine-checked.

| Module | Declarations | Mathematical scope |
| --- | --- | --- |
| Transport | `agree_of_generates`, `natural_on_arrow`, `star_natural_on_arrow` | Ring maps agree under generation as a ring over the integers. The separate star-algebra theorem permits scalar coefficients and applies over the complex numbers. Both prove equality of a comparison square from its equation on generators. |
| Invisible | `mem_stableKernel`, `stableKernel_le`, `map_mem_stableKernel`, `stableKernel_greatest` | On an inclusion preorder, intersecting preimages of local two-sided ideals gives the largest compatible family below them. The proofs assume ring transports with identity and composition. The ideals here are algebraic two-sided ideals. Involution and norm closure would require extra hypotheses. |
| Pauli | `product_sign`, `cnot_involutive`, `embedding_square` | On every signed Boolean basis state, verifies the product sign and the one-bit to two-bit transport of a shift/phase word by controlled-NOT conjugation. Extension to a complex matrix algebra and spanning by character orthogonality are proved in Paper I. |
| Reduction | `matching_transport`, `quotient_descent`, `triangle_levels` | Equivariant pullback preserves invariance. A function on representatives factors uniquely through a setoid quotient exactly when it respects the relation. Three oriented edge levels are vertex differences exactly when their sum vanishes. |
| Sewing | `sectorProjector_idempotent`, `sewing_assoc`, `compression_eq_iff` | A diagonal choice of admissible labels gives an idempotent. Three kernels with finite intermediate label spaces and two fixed cuts can be multiplied in either order over any semiring. Compression to coordinate preparations and detectors tests exactly the entries they select. |

The type parameters can range over infinite sets where a lemma does not sum over them. The sewn intermediate label types in `sewing_assoc` must be finite. The construction of gravitational algebras, their comparison, convergence of continuum amplitudes and the field equations remain conjectural research targets in this series. No physics assumptions are imported as Lean axioms.
