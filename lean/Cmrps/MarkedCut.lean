module

public import Mathlib.Analysis.SpecialFunctions.Log.Basic
public import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic

/-! Calibrated area readings and pointwise operations on complex-valued functions.
No measure, Hilbert completion, or field equations are assumed. -/
public section

namespace Cmrps.MarkedCut

/-- The logarithm of the ratio of a flat round patch area to its calibration area. -/
noncomputable def logReading (weight reference radius : ℝ) : ℝ :=
  Real.log (radius ^ 2 * weight / reference)

/-- Resampling at a new waist moves the logarithmic readout by twice the log radius ratio. -/
theorem logReading_rescale {weight reference radius factor : ℝ}
    (hw : 0 < weight) (href : 0 < reference) (hr : 0 < radius) (hf : 0 < factor) :
    logReading weight reference (factor * radius) =
      logReading weight reference radius + 2 * Real.log factor := by
  unfold logReading
  have hratio : 0 < radius ^ 2 * weight / reference := by positivity
  rw [show (factor * radius) ^ 2 * weight / reference =
      factor ^ 2 * (radius ^ 2 * weight / reference) by ring,
      Real.log_mul (pow_ne_zero _ hf.ne') hratio.ne', Real.log_pow]
  push_cast
  ring

/-- The unit phase of a real additive readout. -/
noncomputable def phase (x : ℝ) : ℂ :=
  Complex.exp ((x : ℂ) * Complex.I)

theorem phase_add (x y : ℝ) : phase (x + y) = phase x * phase y := by
  simp [phase, add_mul, Complex.exp_add]

/-- The real readout changes the phase without changing its norm. -/
theorem norm_phase (x : ℝ) : ‖phase x‖ = 1 :=
  Complex.norm_exp_ofReal_mul_I x

/-- A nonzero additive calibration shift can be turned into an exact sign reversal. -/
theorem phase_shift_halfturn (x : ℝ) {δ : ℝ} (hδ : δ ≠ 0) :
    phase (Real.pi / δ * (x + δ)) = -phase (Real.pi / δ * x) := by
  rw [mul_add, phase_add, div_mul_cancel₀ _ hδ]
  simp [phase, Complex.exp_pi_mul_I]

/-- A real frequency can distinguish a larger waist from the original marked cut by a sign. -/
theorem waist_phase_flip {weight reference radius factor : ℝ}
    (hw : 0 < weight) (href : 0 < reference) (hr : 0 < radius) (hf : 1 < factor) :
    let t := Real.pi / (2 * Real.log factor)
    phase (t * logReading weight reference (factor * radius)) =
      -phase (t * logReading weight reference radius) := by
  dsimp only
  rw [logReading_rescale hw href hr (zero_lt_one.trans hf)]
  exact phase_shift_halfturn _ (mul_ne_zero (by norm_num) (Real.log_pos hf).ne')

/-- A bounded phase probe takes different values at the two cuts. -/
theorem exists_waist_phase_ne {weight reference radius factor : ℝ}
    (hw : 0 < weight) (href : 0 < reference) (hr : 0 < radius) (hf : 1 < factor) :
    ∃ t : ℝ, phase (t * logReading weight reference (factor * radius)) ≠
      phase (t * logReading weight reference radius) := by
  refine ⟨Real.pi / (2 * Real.log factor), ?_⟩
  rw [waist_phase_flip hw href hr hf, ne_eq, CharZero.neg_eq_self_iff]
  exact Complex.exp_ne_zero _

/-- Translation acts by reading the function at x + a. -/
def translate (a : ℝ) (ψ : ℝ → ℂ) (x : ℝ) : ℂ := ψ (x + a)

/-- Multiplication by the character with frequency t. -/
noncomputable def modulate (t : ℝ) (ψ : ℝ → ℂ) (x : ℝ) : ℂ := phase (t * x) * ψ x

/-- The ordered operation M_t T_a. -/
noncomputable def probe (a t : ℝ) (ψ : ℝ → ℂ) : ℝ → ℂ := modulate t (translate a ψ)

/-- Moving the second phase past the first translation contributes exp(i u a). -/
theorem probe_product (a t b u : ℝ) (ψ : ℝ → ℂ) (x : ℝ) :
    probe a t (probe b u ψ) x = phase (u * a) * probe (a + b) (t + u) ψ x := by
  simp only [probe, modulate, translate, mul_add, add_mul, phase_add, add_assoc]
  ring

/-- Apply a one-variable operation separately at each fixed spectator label. -/
def onFirst {Z : Type*} (op : (ℝ → ℂ) → ℝ → ℂ) (Ψ : ℝ × Z → ℂ) (p : ℝ × Z) : ℂ :=
  op (fun x => Ψ (x, p.2)) p.1

/-- A single available spectator label suffices to recover the original operation. -/
theorem onFirst_injective {Z : Type*} (z : Z) : Function.Injective (@onFirst Z) := by
  intro op₁ op₂ same
  funext ψ x
  exact congrFun (congrFun same (fun p => ψ p.1)) (x, z)

/-- The phase/translation order survives adding any spectator, for arbitrary joint functions. -/
theorem lifted_probe_product {Z : Type*} (a t b u : ℝ) (Ψ : ℝ × Z → ℂ) (p : ℝ × Z) :
    onFirst (probe a t) (onFirst (probe b u) Ψ) p =
      phase (u * a) * onFirst (probe (a + b) (t + u)) Ψ p :=
  probe_product a t b u (fun x => Ψ (x, p.2)) p.1

/-- Extending a function by a spectator factor intertwines the original and lifted probes. -/
theorem probe_tensor {Z : Type*} (a t : ℝ) (ψ : ℝ → ℂ) (spectator : Z → ℂ) (p : ℝ × Z) :
    onFirst (probe a t) (fun q => ψ q.1 * spectator q.2) p =
      probe a t ψ p.1 * spectator p.2 := by
  simp [onFirst, probe, modulate, translate, mul_assoc]

/-- Expectation of a diagonal observable in the equal mixture of two label states. -/
noncomputable def forgetPair (v : ℂ × ℂ) : ℂ := (v.1 + v.2) / 2

/-- The diagonal factors contributed by two choices of calibration. -/
noncomputable def labelPhases (c₀ c₁ t : ℝ) : ℂ × ℂ := (phase (t * c₀), phase (t * c₁))

/-- Forgetting the label cancels the two contributions at the half-turn setting. -/
theorem forget_halfturn {c₀ c₁ : ℝ} (h : c₁ ≠ c₀) :
    forgetPair (labelPhases c₀ c₁ (Real.pi / (c₁ - c₀))) = 0 := by
  have flip := phase_shift_halfturn c₀ (sub_ne_zero.mpr h)
  rw [add_sub_cancel c₀ c₁] at flip
  simp [forgetPair, labelPhases, flip]

/-- Averaging the adjoint product retains the unit response at every setting. -/
theorem forget_star_mul (c₀ c₁ t : ℝ) :
    let v := labelPhases c₀ c₁ t
    forgetPair (star v * v) = 1 := by
  have unit (x : ℝ) : star (phase x) * phase x = 1 := by
    rw [phase, Complex.star_def, ← Complex.exp_conj, ← Complex.exp_add]
    simp
  change (star (phase (t * c₀)) * phase (t * c₀) +
    star (phase (t * c₁)) * phase (t * c₁)) / 2 = 1
  rw [unit, unit]
  norm_num

/-- A unitary diagonal reading witnesses failure to preserve multiplication. -/
theorem forget_not_multiplicative {c₀ c₁ : ℝ} (h : c₁ ≠ c₀) :
    let v := labelPhases c₀ c₁ (Real.pi / (c₁ - c₀))
    forgetPair (star v * v) ≠ forgetPair (star v) * forgetPair v := by
  dsimp only
  rw [forget_star_mul, forget_halfturn h, mul_zero]
  exact one_ne_zero

end Cmrps.MarkedCut
