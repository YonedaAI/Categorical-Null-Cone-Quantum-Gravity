module

public import Mathlib.Data.Matrix.Basis

/-! A necessary test for identifying a classical observable product with a quantum one. -/
public section

namespace Cmrps

/-- A noncommuting pair in the target rules out a surjective homomorphism
from a commutative semiring. -/
theorem not_surjective_of_noncommuting {A B : Type*} [CommSemiring A] [Semiring B]
    (f : A →+* B) {u v : B} (hne : u * v ≠ v * u) : ¬ Function.Surjective f := by
  intro onto
  obtain ⟨a, rfl⟩ := onto u
  obtain ⟨b, rfl⟩ := onto v
  exact hne (by rw [← map_mul, mul_comm a b, map_mul])

/-- The two opposite matrix units on distinct basis labels give an explicit
witness over any nontrivial coefficient semiring. -/
theorem not_surjective_to_matrix {A R I : Type*} [CommSemiring A] [Semiring R]
    [Nontrivial R] [Fintype I] [DecidableEq I] (i j : I) (hij : i ≠ j)
    (f : A →+* Matrix I I R) : ¬ Function.Surjective f := by
  apply not_surjective_of_noncommuting f
    (u := Matrix.single i j 1) (v := Matrix.single j i 1)
  intro commute
  have entry := congrArg (fun m : Matrix I I R => m i i) commute
  simp [hij.symm] at entry

end Cmrps
