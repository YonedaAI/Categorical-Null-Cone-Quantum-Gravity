module

public import Mathlib.RingTheory.TwoSidedIdeal.Operations

/-! The largest transport-stable family of invisible ideals on an inclusion preorder. -/
public section
namespace Cmrps

variable {D : Type*} [Preorder D] {A : D → Type*} [∀ d, Ring (A d)]

/-- Ring-level observable transport along a nesting of regions. -/
structure RingTransport (D : Type*) [Preorder D] (A : D → Type*) [∀ d, Ring (A d)] where
  map : ∀ {d e : D}, d ≤ e → A d →+* A e
  map_id : ∀ (d : D) (x : A d), map (le_refl d) x = x
  map_comp : ∀ {d e f : D} (i : d ≤ e) (j : e ≤ f) (x : A d),
    map (i.trans j) x = map j (map i x)

namespace RingTransport
variable (T : RingTransport D A) (K : ∀ d, TwoSidedIdeal (A d))

/-- Intersect the preimages of all ambient invisible ideals, including the local one. -/
def stableKernel (d : D) : TwoSidedIdeal (A d) :=
  ⨅ (e : {e : D // d ≤ e}), (K e.val).comap (T.map e.property)

theorem mem_stableKernel {d : D} {x : A d} :
    x ∈ T.stableKernel K d ↔ ∀ (e : D) (h : d ≤ e), T.map h x ∈ K e := by
  simp only [stableKernel, TwoSidedIdeal.mem_iInf, TwoSidedIdeal.mem_comap, Subtype.forall]

theorem stableKernel_le (d : D) : T.stableKernel K d ≤ K d := by
  intro x hx
  simpa [T.map_id] using (T.mem_stableKernel K).mp hx d (le_refl d)

theorem map_mem_stableKernel {d e : D} (h : d ≤ e) {x : A d}
    (hx : x ∈ T.stableKernel K d) : T.map h x ∈ T.stableKernel K e := by
  apply (T.mem_stableKernel K).mpr
  intro f j
  rw [← T.map_comp]
  exact (T.mem_stableKernel K).mp hx f (h.trans j)

theorem stableKernel_greatest (J : ∀ d, TwoSidedIdeal (A d)) (contained : ∀ d, J d ≤ K d)
    (stable : ∀ {d e : D} (h : d ≤ e) {x : A d}, x ∈ J d → T.map h x ∈ J e)
    (d : D) : J d ≤ T.stableKernel K d := by
  intro x hx
  exact (T.mem_stableKernel K).mpr fun e h => contained e (stable h hx)

end RingTransport
end Cmrps
