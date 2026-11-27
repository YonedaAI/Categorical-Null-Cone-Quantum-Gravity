
### Referee Report on: *Gravitational Gluing and Categorical Descent (Part III)*

---

### 1. Overview and Scope
The manuscript investigates the algebraic and categorical mechanics of gluing spacetime regions along cuts and corners, contrasting finite-dimensional Hilbert space / projector models with the continuum null-cone quantization framework of Chandrasekaran (`arXiv:2611.34924v1`) and the categorical descent framework of Long. 

The paper touches on important questions: how physical sector projectors behave under refinement, when discrepancies between candidate cuts are detectable by restricted boundary probes, the limitations of classical sheaf/descent conditions for states, and the analytic pitfalls of composing resolutions of the identity in infinite-dimensional settings.

While several linear-algebraic results are sound, the paper contains mathematically substantive conceptual defects regarding the physical interpretation of "cut changes", as well as misleading attributions concerning the scope and machinery of Section 4.4 versus Appendix E.1 in Chandrasekaran.

---

### 2. Evaluation of Key Components

#### 2.1 Finite Projector Theorem (Theorem 5.1 & Proposition 5.2)
* **Mathematical Assessment:** Theorem 5.1 is mathematically correct. Given finite-dimensional Hilbert spaces $H, H'$, orthogonal projections $P$ on $H$ and $Q$ on $H'$, an isometry or unitary $U: H \to H'$, and subspaces $L, R \subseteq H$ with orthogonal projectors $\Pi_L, \Pi_R$, the equivalence of:
  1. $a(\ell, r) = a'(\ell, r)$ for all $\ell \in L, r \in R$,
  2. $D(L) \subseteq R^\perp$ where $D = P - U^*QU$,
  3. $\Pi_R D \Pi_L = 0$,
  is an exact property of sesquilinear forms on Hilbert spaces. The norm compression identity
  $$\max_{\substack{\ell \in L, r \in R \\ \|\ell\|=\|r\|=1}} |a(\ell, r) - a'(\ell, r)| = \|\Pi_R D \Pi_L\|$$
  holds by Cauchy–Schwarz and the attainment of the operator norm on finite-dimensional unit spheres.
* Proposition 5.2 ($U^*QU = P \iff QU = UP$ for an isometry $U$ and projections $P, Q$) is also correctly proved via the orthogonal decomposition $H = \im P \oplus \ker P$.

#### 2.2 Cut-Change Interpretation (Section 5 & Example 5.1)
* **Substantive Conceptual Defect:** In Section 5 and Example 5.1, the manuscript models a "change of cut" by holding the exterior preparation maps $A: X \to H$ and $B: H \to Y$ fixed while replacing the projector $P$ with $Q$ on $H' \cong H$, setting $U = 1$. The manuscript states:
  > *"Two one-dimensional sectors give an example in which all contractions associate while a change of cut changes a measurable amplitude."* (Abstract & Example 5.1)
* In standard general boundary quantum field theory (e.g., Oeckl) and gravitational path integrals, changing an intermediate cut $\Sigma \to \Sigma'$ alters the flanking subregions: $M_1 \to M_1'$ and $M_2 \to M_2'$. The region $M_1'$ is related to $M_1$ by the intermediate slab $\Delta M$ bounded by $\Sigma$ and $\Sigma'$. The dynamical propagator across $\Delta M$ is an operator $U_{\Delta M}: \mathcal{H}_\Sigma \to \mathcal{H}_{\Sigma'}$.
* In Example 5.1, by choosing $P = |e_0\rangle\langle e_0|$, $Q = |e_1\rangle\langle e_1|$, and setting the identification map $U = \mathbf{1}$, the author declares that the physical state $|e_0\rangle$ on the first cut is identified with the orthogonal, unphysical state $|e_0\rangle$ on the second cut. The resulting amplitude change ($BPA = 1$ vs $BQA = 0$) does not demonstrate that a "change of cut changes a measurable amplitude"; rather, it demonstrates that setting $U = \mathbf{1}$ fails to implement the dynamical transport between the cuts ($UP \neq QU$). 
* Although Section 5.2 notes in passing that exterior kernels could change, the framing throughout the Abstract, Introduction, and Example 5.1 asserts that associative contractions can fail to preserve amplitudes under a genuine change of cut, which conflates a non-intertwining identification of slices with physical cut-dependence.

#### 2.3 Analytic Limits and the Double Series (Section 6 & Example 6.1)
* **Mathematical Assessment of Example 6.1:** The construction in Example 6.1 is mathematically rigorous and instructive. For $H = \bigoplus_{n\ge 1} \CC^{4^n}$, $F = \bigoplus_{n\ge 1} F_{4^n}$ (block discrete Fourier transforms), and $x = y$ with components $1/(n\sqrt{d_n})$, the vector norm $\|x\|^2 = \sum n^{-2} < \infty$ is finite and the amplitude $\langle y, Fx\rangle = \sum n^{-2} 2^{-n} < \infty$ converges. The double expansion $\sum_{i,j} |\overline{y_i} F_{ij} x_j|$ diverges as $\sum 2^n/n^2 = \infty$.
* This correctly proves that inserting two complete resolutions of the identity into $\langle y, T_3 T_2 T_1 x\rangle$ does not produce an absolutely convergent double sum in the absence of trace-class conditions. Strong operator convergence of cutoffs does not imply absolute summability of matrix elements.

#### 2.4 Distinction Between Section 4.4 and Appendix E.1 of Chandrasekaran
* **Misleading Attribution and Conflation:**
  1. **Section 4.4 of Chandrasekaran:** Treats the temporal composition of *two specific null sheets* meeting at a single regulated spacelike cap. Equation (4.29) inserts a single resolution of the identity on that cap, and Eq. (4.30) bounds the sum by $\|y\|\|x\|$ using the Cauchy–Schwarz inequality for a single orthonormal basis. Chandrasekaran makes no claim in Section 4.4 that un-filtered, iterated double resolutions of the identity converge as absolute double series.
  2. **Appendix E.1 of Chandrasekaran:** Sets out an *axiomatic framework* for general Lorentzian preparations and cobordisms. Here, cut-independence is formulated as an axiom (Axiom 1), and convergence/finiteness under composition is explicitly governed by **Axiom 5 (Energy Filtering and Spectral Positivity)**, which introduces smooth compactly supported test functions $f \in C_c^\infty(\mathbb{R})$ acting on the Hamiltonian generator.
  3. **The Defect in the Manuscript:** In Section 6.1, the manuscript frames Example 6.1 as revealing a gap in Chandrasekaran's sewing construction ("*Equation (7) does not bound the absolute sum over two independent intermediate indices after inserting a resolution at each cut...*"). This is a misleading comparison: the author critiques Section 4.4 for failing to guarantee absolute convergence of multi-cut expansions, while omitting that the regulatory mechanism designed to control multi-region compositions in Chandrasekaran is precisely the energy-filtering structure formulated in Appendix E.1.

---

### 3. Summary of Specific Evidence and Corrections Needed

1. **Clarify Cut Changes in Example 5.1 and Abstract:**
   * *Issue:* The Abstract and Section 5 claim that an example is provided where "all contractions associate while a change of cut changes a measurable amplitude."
   * *Evidence:* In Example 5.1, $A$ and $B$ are held rigid while $P \to Q$ and $U = \mathbf{1}$. This is an incompatible redefinition of the physical projector on the same slice, not a dynamical transport across a moved cut.
   * *Correction:* State explicitly that amplitude mismatch under $U = \mathbf{1}$ reflects a failure of $U$ to intertwine the dynamical evolution across the slab $\Delta M$ with the physical sub-selection ($UP \neq QU$).
2. **Accurate Contextualization of Chandrasekaran Section 4.4 vs Appendix E.1:**
   * *Issue:* Section 6.1 attacks Eq. (4.30) (Eq. 7 of the manuscript) for not bounding double resolutions across two cuts.
   * *Evidence:* Chandrasekaran's Eq. (4.30) only claims absolute convergence for a single intermediate spacelike cap between two fixed exterior preparations. Multi-cut composition and spectral convergence are handled under the Axioms of Appendix E.1 via energy filtering (Axiom 5).
   * *Correction:* Distinguish explicitly between the local, single-slice sewing calculation of Section 4.4 and the multi-region axiomatic composition in Appendix E.1. Acknowledge that energy filters in Appendix E.1 are designed precisely to prevent the divergence demonstrated in Example 6.1.
3. **Notation and Contextuality in Section 7:**
   * The Abramsky–Brandenburger contextuality example on the triangle is mathematically correct, but the manuscript should explicitly state that the obstruction to extending local probability measures arises from non-trivial cohomology / contextuality loops, and clarify its operational relevance to gravitational diamond covers.

---

VERDICT: REVISE
