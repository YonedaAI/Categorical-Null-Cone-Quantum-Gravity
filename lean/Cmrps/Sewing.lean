module

public import Mathlib.Data.Matrix.Mul

/-! Finite boundary labels and kernels with a sector selection on each cut. -/
public section

namespace Cmrps

open Matrix

/-- A diagonal kernel implements the choice of admissible middle labels. -/
def sectorProjector {I R : Type*} [DecidableEq I] [Semiring R]
    (allowed : I → Bool) : Matrix I I R :=
  diagonal (fun i => if allowed i then 1 else 0)

theorem sectorProjector_idempotent {I R : Type*} [Fintype I] [DecidableEq I]
    [Semiring R] (allowed : I → Bool) :
    sectorProjector (R := R) allowed * sectorProjector allowed = sectorProjector allowed := by
  unfold sectorProjector
  rw [diagonal_mul_diagonal]
  congr 1
  funext i
  cases allowed i <;> simp

theorem sewing_assoc {I J K L R : Type*} [Fintype J] [Fintype K]
    [DecidableEq J] [DecidableEq K] [Semiring R]
    (u : Matrix I J R) (v : Matrix J K R) (w : Matrix K L R)
    (p : J → Bool) (q : K → Bool) :
    ((u * sectorProjector p * v) * sectorProjector q) * w =
      u * sectorProjector p * (v * sectorProjector q * w) := by
  simp only [Matrix.mul_assoc]

/-- Compression to coordinate preparations and detectors agrees exactly when
all entries visible to those probes agree. No inner-product structure is needed. -/
theorem compression_eq_iff {I J R : Type*} [Fintype I] [Fintype J]
    [DecidableEq I] [DecidableEq J] [Semiring R]
    (p q : Matrix I J R) (detect : I → Bool) (prepare : J → Bool) :
    sectorProjector detect * p * sectorProjector prepare =
      sectorProjector detect * q * sectorProjector prepare ↔
    ∀ i j, detect i = true → prepare j = true → p i j = q i j := by
  constructor
  · intro h i j hi hj
    have entry := congrArg (fun m : Matrix I J R => m i j) h
    simpa [sectorProjector, hi, hj] using entry
  · intro h
    ext i j
    cases hi : detect i <;> cases hj : prepare j <;>
      simp [sectorProjector, *]

end Cmrps
