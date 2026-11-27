
### Referee Report on: *Ordered probes at a marked null cut (Supplement to Categorical Null-Cone Quantum Gravity)*

---

### 1. General Assessment

The updated supplementary note provides an exact, self-contained mathematical analysis of non-commuting ordered probes associated with a marked null cut, the role of calibration data across region inclusions, optical area distortions in a curved background, and the spectral obstructions inherent to finite/bounded area sectors.

The primary addition in this final draft is Subsection 4.1 ("*Forgetting a calibration label*"), which addresses the algebraic transport problem when internal calibration data (reference shifts) are either preserved or averaged out. The requested checks, detailed below, confirm that the mathematical physics of this new subsection is completely sound and integrates seamlessly with the rest of the manuscript.

---

### 2. Detailed Technical Verification of Subsection 4.1 (*Forgetting a calibration label*)

1. **Controlled Translation Operator and Unitarity:**
   The unitary operator defined on $\mathcal{H} \otimes \mathbb{C}^2$ is:
   \[
   V = U(c_0) \otimes E_0 + U(c_1) \otimes E_1,
   \]
   where $E_0, E_1$ are orthogonal rank-1 projections on $\mathbb{C}^2$ satisfying $E_j E_k = \delta_{jk} E_j$ and $E_0 + E_1 = 1$. Since $U(c_j)$ are unitary translation operators on $\mathcal{H} = L^2(\mathbb{R}, dq)$ ($U(c_j)^* = U(-c_j)$), we have:
   \[
   V V^* = U(c_0)U(-c_0) \otimes E_0 + U(c_1)U(-c_1) \otimes E_1 = 1 \otimes (E_0 + E_1) = 1 \otimes 1.
   \]
   Thus $V$ is unitary, and $\alpha(A) = V (A \otimes 1) V^*$ defines a faithful unital $*$-homomorphism into $B(\mathcal{H} \otimes \mathbb{C}^2)$.

2. **Signs of the Conjugation Phases:**
   The Heisenberg relation for the one-mode chart is $[Q, P] = i\hbar \mathbf{1}$, so $U(a) M(b) = e^{i a b} M(b) U(a)$, which gives:
   \[
   U(c_j) M(b) U(-c_j) = e^{i b c_j} M(b).
   \]
   Because the projections $E_j$ are diagonal and orthogonal, conjugating $M(b) \otimes 1$ yields:
   \[
   \alpha(M(b)) = \sum_{j=0}^1 U(c_j) M(b) U(-c_j) \otimes E_j = M(b) \otimes \left( e^{i b c_0} E_0 + e^{i b c_1} E_1 \right).
   \]
   Because the translation generators commute with each other ($[P, P] = 0$), $U(c_j) U(a) U(-c_j) = U(a)$, which immediately implies:
   \[
   \alpha(U(a)) = U(a) \otimes (E_0 + E_1) = U(a) \otimes 1.
   \]
   The relative signs in the phase factors $+i b c_0$ and $+i b c_1$ are correct.

3. **Normalized Partial Trace and Complete Positivity:**
   The state reduction/forgetting map is defined via $\Phi = \mathrm{id} \otimes \mathrm{tr}_2$, where $\mathrm{tr}_2(\cdot) = \frac{1}{2}\operatorname{Tr}_{\mathbb{C}^2}(\cdot)$. Acting on $\alpha(M(b))$ gives:
   \[
   \Phi(\alpha(M(b))) = M(b) \cdot \mathrm{tr}_2\left(e^{i b c_0} E_0 + e^{i b c_1} E_1\right) = M(b) \left( \frac{e^{i b c_0} + e^{i b c_1}}{2} \right),
   \]
   which is exact. Since $\Phi$ is a conditional expectation and $\alpha$ is a unital $*$-homomorphism, the composite channel $\mathcal{E} = \Phi \circ \alpha$ is unital and completely positive (UCP).

4. **Failure of Multiplicativity:**
   Setting the readout frequency to $b = \frac{\pi}{c_1 - c_0}$ yields $e^{i b c_1} = -e^{i b c_0}$, causing the trace coefficient to vanish identically:
   \[
   \Phi(\alpha(M(b))) = 0 \implies \mathcal{E}(M(b))^* \mathcal{E}(M(b)) = 0.
   \]
   On the other hand, $M(b)^* M(b) = \mathbf{1}$, so:
   \[
   \mathcal{E}(M(b)^* M(b)) = \Phi(1 \otimes 1) = \mathbf{1}.
   \]
   Hence $\mathcal{E}(M(b)^* M(b)) \ne \mathcal{E}(M(b))^* \mathcal{E}(M(b))$, establishing the failure of multiplicativity (homomorphism property). This rigorously underpins the note's conclusion that forgetting a calibration frame induces state decoherence / quantum channel mixing rather than an algebraic embedding.

---

### 3. Compatibility Across the Manuscript

- **Compatibility with the Spectral No-Go Result (Section 5):**
  Section 5 proves that an exact unitary dilation $\mathcal{U}(a) K_{\mathrm{sec}} \mathcal{U}(a)^* = e^a K_{\mathrm{sec}}$ cannot exist on any nonzero bounded operator (since $\|K_{\mathrm{sec}}\| = e^a \|K_{\mathrm{sec}}\|$ implies $a=0$ or $K_{\mathrm{sec}}=0$) nor in a discrete spectrum. Subsection 4.1 introduces a finite auxiliary register $\mathbb{C}^2$ specifically for the calibration label, while the area coordinate $K = K_* e^Q$ remains on the continuous affine chart $L^2(\mathbb{R})$. This discrete-continuous split is mathematically consistent and correctly avoids conflating the finite label space with the continuous scaling generator.
- **Compatibility with the Plane-Wave Area Calculation (Section 4.2):**
  The Jacobi propagator $B(u) = \kappa^{-1}\operatorname{diag}(\sinh(\kappa u), \sin(\kappa u))$ correctly produces the exact local cross-sectional density $j(u) = \det B(u) = \kappa^{-2}\sinh(\kappa u)\sin(\kappa u)$. The Taylor expansion:
  \[
  \frac{j(S)}{j(R)} = \frac{S^2}{R^2}\left[ 1 - \frac{\kappa^4(S^4 - R^4)}{90} + O((\kappa S)^8) \right]
  \]
  is verified: the $O(\kappa^2)$ terms from stretching ($\sinh$) and focusing ($\sin$) cancel exactly due to the trace-free curvature condition $R_{uu} = 0$. The distinction between this classical geometric density variation and the quantum operator algebra transport is maintained with precision.
- **Restriction to a Conditional One-Mode Quantum Chart:**
  The note remains scrupulously clear regarding its domain of validity: the algebra of probes operates on the pull-back chart where transverse metric perturbations and constraint couplings are turned off, and the cut maintains a marked angular/normal reference. The caveats in Sections 1, 4, and 5 correctly state that the result is an operational benchmark rather than an unconstrained full quantum gravity representation.

---

### 4. Required Changes

None. The mathematical derivations are exact, the signs and normalization factors are verified, and the conceptual boundaries of the physical model are precisely demarcated.

VERDICT: PUBLISHABLE
