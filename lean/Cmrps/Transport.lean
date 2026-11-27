module

public import Mathlib.Algebra.Ring.Subring.Basic
public import Mathlib.Algebra.Star.Subalgebra

/-! An equalizer argument extends agreement on generators to a whole ring.
A second comparison uses generation as a star algebra over a scalar ring. -/
public section

namespace Cmrps

/-- Every subring containing the proposed generators contains every element. -/
def Generates {A : Type*} [Ring A] (S : Set A) : Prop :=
  ∀ K : Subring A, S ⊆ K → ∀ x : A, x ∈ K

theorem agree_of_generates {A B : Type*} [Ring A] [Ring B]
    {S : Set A} (hS : Generates S) (f g : A →+* B)
    (agree : ∀ a ∈ S, f a = g a) (x : A) : f x = g x := by
  exact hS (f.eqLocus g) agree x

/-- Naturality for one arrow follows from its square on a generating family. -/
theorem natural_on_arrow {A B C D : Type*} [Ring A] [Ring B] [Ring C] [Ring D]
    {S : Set A} (hS : Generates S) (left : A →+* B) (right : C →+* D)
    (source : A →+* C) (target : B →+* D)
    (onGenerators : ∀ a ∈ S, target (left a) = right (source a)) :
    target.comp left = right.comp source := by
  ext x
  exact agree_of_generates hS (target.comp left) (right.comp source) onGenerators x

/-- The comparison square on algebraic star algebras, with scalars included in
the generated algebra. This version applies over the complex numbers. -/
theorem star_natural_on_arrow {R A B C D : Type*} [CommSemiring R] [StarRing R]
    [Semiring A] [Algebra R A] [StarRing A] [StarModule R A]
    [Semiring B] [Algebra R B] [StarRing B]
    [Semiring C] [Algebra R C] [StarRing C]
    [Semiring D] [Algebra R D] [StarRing D]
    {S : Set A} (generates : StarAlgebra.adjoin R S = ⊤)
    (left : A →⋆ₐ[R] B) (right : C →⋆ₐ[R] D)
    (source : A →⋆ₐ[R] C) (target : B →⋆ₐ[R] D)
    (onGenerators : ∀ a ∈ S, target (left a) = right (source a)) :
    target.comp left = right.comp source :=
  StarAlgHom.ext_of_adjoin_eq_top generates onGenerators

end Cmrps
