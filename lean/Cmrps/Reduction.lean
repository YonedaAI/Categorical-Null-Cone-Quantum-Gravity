module

public import Mathlib.GroupTheory.GroupAction.Basic
public import Mathlib.Tactic.Abel

/-! Observables constant on the orbits of a finite or infinite group.
No analytic properties of null data are assumed. -/
public section

namespace Cmrps

theorem matching_transport {G X Y V : Type*} [Group G] [MulAction G X]
    [MulAction G Y] (i : X → Y) (equivariant : ∀ (g : G) (x : X), i (g • x) = g • i x)
    (observable : Y → V) (invariant : ∀ (g : G) (y : Y), observable (g • y) = observable y)
    (g : G) (x : X) : observable (i (g • x)) = observable (i x) := by
  rw [equivariant, invariant]

/-- Descent along a quotient exists and is unique exactly when the observable is constant
on related data. The relation can be the orbits of an action. -/
theorem quotient_descent {X V : Type*} (s : Setoid X) (a : X → V) :
    (∀ x y, s.r x y → a x = a y) ↔
    ∃! b : Quotient s → V, ∀ x, b (Quotient.mk s x) = a x := by
  constructor
  · intro h
    refine ⟨Quotient.lift a (fun {x y} hxy => h x y hxy), fun _ => rfl, ?_⟩
    intro b hb
    funext q
    induction q using Quotient.inductionOn with
    | _ x => exact hb x
  · rintro ⟨b, hb, _⟩ x y hxy
    rw [← hb x, ← hb y, Quotient.sound hxy]

/-- Three oriented edge levels arise as vertex differences exactly when their
cycle sum vanishes. This is the consistency test before quantizing a triangle. -/
theorem triangle_levels {V : Type*} [AddCommGroup V] (a b c : V) :
    (∃ x y z : V, a = y - x ∧ b = z - y ∧ c = x - z) ↔ a + b + c = 0 := by
  constructor
  · rintro ⟨x, y, z, rfl, rfl, rfl⟩
    abel
  · intro h
    refine ⟨0, a, a + b, by simp, by abel, ?_⟩
    rw [zero_sub]
    exact eq_neg_of_add_eq_zero_right h

end Cmrps
