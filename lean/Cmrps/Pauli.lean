module
import Std.Tactic

/-! Action on a signed computational basis. The Booleans for phases record the
exponent of -1. These finite identities verify the product sign and the conjugation
identity used in the one-bit to two-bit probe example. -/
public section
namespace Cmrps.Pauli

abbrev SignedBit := Bool × Bool
abbrev SignedPair := Bool × Bool × Bool

/-- Apply X^a Z^b, recording the bit value and the sign exponent. -/
def word (a b : Bool) (v : SignedBit) : SignedBit :=
  (v.1 ^^ a, v.2 ^^ (b && v.1))

def changeSign (e : Bool) (v : SignedBit) : SignedBit := (v.1, v.2 ^^ e)

/-- Two words multiply with the sign from commuting the first phase past the second flip. -/
theorem product_sign : ∀ a b c d s e : Bool,
    word a b (word c d (s, e)) =
      changeSign (b && c) (word (a ^^ c) (b ^^ d) (s, e)) := by decide

/-- A controlled flip is its own inverse. -/
def cnot (v : SignedPair) : SignedPair :=
  (v.1, v.2.1 ^^ v.1, v.2.2)

def pairWord (a₁ b₁ a₂ b₂ : Bool) (v : SignedPair) : SignedPair :=
  (v.1 ^^ a₁, v.2.1 ^^ a₂, (v.2.2 ^^ (b₁ && v.1)) ^^ (b₂ && v.2.1))

theorem cnot_involutive : ∀ s t e : Bool,
    cnot (cnot (s, t, e)) = (s, t, e) := by decide

/-- Conjugating a one-bit word by the controlled flip transports the flip to
both bits and the phase to the first bit. -/
theorem embedding_square : ∀ a b s t e : Bool,
    cnot (pairWord a b false false (cnot (s, t, e))) =
      pairWord a b a false (s, t, e) := by decide

end Cmrps.Pauli
