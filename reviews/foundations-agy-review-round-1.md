
# Referee Report

**Manuscript Title:** Categorical Foundations of Null-Cone Quantization (Part I)  
**Subject Area:** Mathematical Physics, Algebraic Quantum Field Theory, Quantum Gravity  

---

### General Overview

This manuscript investigates the functorial assignment of local observable $*$-algebras to causal regions (diamonds) equipped with characteristic boundary data. The primary conceptual question addressed is: *under what conditions does an observable defined through local probe moments in a smaller region retain its identity and relation structure when embedded into a larger ambient causal region?*

The author formalizes local observables as quotients of free involutive algebras $\mathcal{F}_D$ by an "invisible ideal" $K_D$, defined as the intersection of kernels of GNS representations over a prescribed family of calibrated states $\mathcal{P}_D$. The core mathematical contributions are:
1. An ambient preparation criterion (Theorem 4.1) characterizing when an arrow $f: D \to E$ induces an algebra homomorphism $Y(f): Y(D) \to Y(E)$.
2. The construction of the maximal compatible quotient ideal $\widehat{K}_D$ (Theorem 6.1) yielding an extended functor $Y^{\mathrm{ext}}: \mathcal{D} \to \mathbf{Alg}_*$.
3. A low-dimensional matrix counterexample ($\mathbb{C}^2 \to M_2(\mathbb{C})$) proving that agreement of unconditioned cyclic moments is strictly insufficient to guarantee functoriality.
4. A concrete finite non-commutative realization on binary strings based on twisted group algebras (finite Weyl systems), controlled flip intertwining, and discrete Fourier/Hadamard symmetries.
5. A programmatic discussion applying these tests to null-cone quantization of gravity (referencing recent work by Chandrasekaran and Long).

The mathematical core of the paper is elegant, precise, and correct. However, significant physical and functional-analytic gaps remain between the finite algebraic toy models and the continuum gravitational null-cone setting advertised in the title. 

Below is an evaluation of the specific technical constructions, followed by concrete issues and proposed changes organized by severity.

---

### Evaluation of Specific Mathematical Components

1. **Two-Sided GNS Ideals ($K_D$ and Lemma 3.2):**  
   The mathematical treatment is exact. The author correctly distinguishes between the left GNS ideal $N_\omega = \{b \in \mathcal{F}_D : \omega(b^* b) = 0\}$ (which annihilates only the cyclic vector $[1]$) and the two-sided $*$-ideal $\ker \pi_\omega = \{a \in \mathcal{F}_D : ab \in N_\omega\ \forall b \in \mathcal{F}_D\}$ (the annihilator of the full cyclic representation domain). The proof of Lemma 3.2 via the norm identity $\|\pi_\omega(a)[b]\|^2 = \omega(b^* a^* a b) = 0$ is completely sound.

2. **The Maximal Compatible Quotient ($\widehat{K}_D$ and Theorem 6.1):**  
   The definition $\widehat{K}_D = \bigcap_{f: D \to E} T_f^{-1}(K_E)$ and the proof that $\widehat{K}$ provides the largest compatible sub-ideal of $K_D$ are rigorous and algebraically standard. The duality between $\widehat{K}_D$ and the state space of ambient preparations $\mathcal{P}_D^{\mathrm{ext}}$ (Proposition 6.3) is cleanly established.

3. **The Matrix Counterexample (Section 5):**  
   The counterexample $\F_D = \mathbb{C}^2 \hookrightarrow \F_E = M_2(\mathbb{C})$ with $T_f(a_0, a_1) = \operatorname{diag}(a_0, a_1)$ and cyclic vector $v_0$ is completely accurate. It cleanly demonstrates the phenomenon: while $\omega \circ T_f = \rho$ on all of $\mathbb{C}^2$, the projection $e_1 = (0,1)$ lies in $K_D$ (since $\rho(b^* e_1^* e_1 b) = 0$ for all $b \in \mathbb{C}^2$) but $T_f(e_1) = E_{11} \notin K_E$ because $b = E_{10}$ excites $v_0$ to $v_1$. This demonstrates that local cyclic preparations can fail to detect sectors that become accessible via ambient operations.

4. **Finite Twisted Multiplication and Weyl Realization (Section 7.1 & 7.2):**  
   The product and involution formulas:
   $$w(a,b)w(c,d) = (-1)^{b \cdot c} w(a+c, b+d), \qquad w(a,b)^* = (-1)^{a \cdot b} w(a,b)$$
   define a valid associative $*$-algebra $B_m$. Associativity holds because the exponents $b \cdot c + (b+d) \cdot e$ and $d \cdot e + b \cdot (c+e)$ agree modulo 2. The involution condition $(xy)^* = y^* x^*$ holds because $b \cdot c + (a+c) \cdot (b+d) \equiv a \cdot b + c \cdot d + d \cdot a \pmod 2$. The identification with $M_{2^m}(\mathbb{C})$ via $X(a)Z(b)$ and character orthogonality (Eq. 7.3) is completely correct.

5. **Map on a Proper Inclusion (Section 7.3):**  
   The embedding for $m=1 \to m=2$ via $T_f(x_1) = (x_1 x_2 + x_2 x_1)/2$ and $T_f(z_1) = z_1$ correctly corresponds to $(a,b) \mapsto ((a,a), (b,0))$. It preserves the symplectic phase $(-1)^{(b,0)\cdot(c,c)} = (-1)^{bc}$. The unitary intertwining on $\mathbb{C}^2 \otimes \mathbb{C}^2$ via the controlled-NOT/flip operator $U|s,t\rangle = |s, t+s\rangle$ satisfies $U(X(1)\otimes 1)U = X(1)\otimes X(1)$ and $U(Z(1)\otimes 1)U = Z(1)\otimes 1$, which matches $N(f)$ exactly.

6. **The Symmetry Example and Loop Obstruction (Sections 6.3 & 7.4):**  
   The Hadamard-like automorphism $\theta(w(a,b)) = (-1)^{ab} w(b,a)$ satisfies $\theta^2 = \mathrm{id}$ and respects the algebra product:
   $$bc + (a+c)(b+d) \equiv ab + cd + ad \pmod 2.$$
   The loop obstruction in Section 6.3 correctly notes that natural isomorphisms between functors on groupoids can be obstructed by global holonomy / automorphisms, preventing trivialization of the comparison.

---

### Issues and Proposed Changes

#### Severity: High (Critical conceptual and domain limitations)

1. **Unbounded Operators and the Free Algebra Assumption in Field Theory:**  
   *Issue:* The framework models observables through the free $*$-algebra $\mathcal{F}_D = \mathbb{C}\langle L_D, L_D^*\rangle$. In continuous gravitational null-cone quantization (e.g., Chandrasekaran [3]), the fundamental generators are radiative news $\mathcal{N}_{AB}(u,\theta)$, boundary area metrics, and BMS-like fluxes. These are operator-valued distributions that yield *unbounded* operators upon smearing.  
   In the algebraic GNS construction for free algebras generated by unbounded operators, arbitrary polynomial products $a b$ generally lack a common invariant dense domain, and algebraic kernels do not correspond to closures or von Neumann algebras.  
   *Proposed Change:* The author must explicitly delimit the domain of validity of the algebraic GNS quotient. The paper should either:
   - Formulate the framework in terms of bounded Weyl-like exponentiated operators (e.g., via resolvent algebras as in Buchholz & Grundling (2008), or $C^*$-inductive limits), or
   - Formally state that Section 3–6 treats the strict polynomial/pre-Hilbert setting, and provide an explicit discussion of the domain and core problems that arise when taking closures for continuous null-cone fields.

2. **The Reeh-Schlieder Contrast in Gauge Theory vs. Standard AQFT:**  
   *Issue:* In standard axiomatic quantum field theory (Haag-Kastler / BFV [4]), the Reeh-Schlieder theorem guarantees that the global vacuum vector $\Omega$ is cyclic *and separating* for any local diamond algebra $\mathcal{A}(O)$ with non-empty causal complement. If a state $\omega$ is separating, then $\pi_\omega(a) = 0 \implies a = 0$, meaning $K_D = 0$ automatically, and no non-trivial two-sided ideal can be "invisible" in a single vacuum state.  
   The paper's matrix counterexample relies heavily on non-separating cyclic states. While this is entirely appropriate for systems with gauge constraints, boundaries, and superselection sectors, the manuscript fails to explain *why* the standard Reeh-Schlieder evasion fails in the gravitational/null-cone setting.  
   *Proposed Change:* Add an explicit remark in Section 3 or Section 5 explaining that:
   - In the presence of local boundaries and edge modes (Donnelly-Freidel [5]), local algebras possess non-trivial centers (classical boundary observables / charges).
   - Superselection sectors prevent any single pure state from being separating for the full local algebra.
   - Spacetime diffeomorphism invariance precludes the global positive-energy translation group required by the Reeh-Schlieder theorem.

3. **Disparity Between Title/Abstract and Section 8 Content:**  
   *Issue:* The paper is titled *"Categorical Foundations of Null-Cone Quantization (Part I)"*, yet Section 8 ("A first gravitational test") does not compute or prove any theorem concerning continuous null cones. It provides a purely qualitative checklist of what an eventual null-cone comparison would require.  
   *Proposed Change:* Clarify in the Introduction and the title/abstract that Part I establishes the *algebraic and categorical framework* for local boundary/probe inclusions, illustrating it with finite Weyl systems, while formulating the necessary compatibility criteria for null-cone gravity as an open programmatic problem.

---

#### Severity: Medium (Missing literature and precision of categorical formulation)

1. **Missing Literature on Edge Modes and Null Surface Quantization:**  
   *Issue:* The paper references Donnelly & Freidel (2016) [5] and Chandrasekaran (2026) [3], but omits foundational and recent literature on edge modes, corner symmetries, and algebraic quantization of null boundaries:
   - Harlow and Wu, *Covariant phase space with boundaries* (JHEP 2020 / arXiv:1906.08616).
   - Chandrasekaran, Flanagan, and Prabhu, *Symmetries and charges of general relativity at null boundaries* (JHEP 2020 / arXiv:2007.03664).
   - Hopfmüller and Freidel, *Gravity Local Subsystems, Gauge Equivalence, and Classical Edge Modes* (PRD 2017 / arXiv:1611.03096).
   - Ciambelli and Leigh, *Universal Corner Symmetry and the Classical Horizon* (JHEP 2021).  
   *Proposed Change:* Cite these works in Sections 2.2 and 8 to properly anchor the discussion of cap/corner frames, boundary charges, and gauge vs. physical symmetries.

2. **Small Category vs. Continuum Spacetime Sites:**  
   *Issue:* In Section 2.2 and Section 6.1, the category $\mathcal{D}$ is assumed to be a *small category*. However, in differential geometry, spacetimes and causal diamonds with arbitrary smooth embeddings form a large category. Forming the intersection $\widehat{K}_D = \bigcap_{f: D \to E} T_f^{-1}(K_E)$ requires an intersection over a set, not a proper class.  
   *Proposed Change:* Explicitly state that $\mathcal{D}$ is chosen as a skeletal small subcategory or an admissible small site of regions (e.g., diamonds with rational coordinates, or a restricted countable family of charts/diamonds), ensuring that the intersection defining $\widehat{K}_D$ is set-theoretically well-defined.

3. **Notation in Theorem 4.1:**  
   *Issue:* Condition 2 is stated as $K_D \subseteq T_f^{-1}(K_E)$. While mathematically equivalent to $T_f(K_D) \subseteq K_E$, the latter is much more intuitive in representation theory (it states directly that the map carries null/invisible operators into null/invisible operators).  
   *Proposed Change:* State Condition 2 as $T_f(K_D) \subseteq K_E$ (or explicitly mention $T_f(K_D) \subseteq K_E \iff K_D \subseteq T_f^{-1}(K_E)$).

---

#### Severity: Low (Clarity, typos, and minor technical remarks)

1. **Clarification of Commutation in $B_2$ vs. $\mathcal{F}$ in Section 7.3:**  
   *Issue:* The author writes: *"Choose $(x_1 x_2 + x_2 x_1)/2$ as the raw substitution; its image under $r_2$ is $w((1,1),(0,0))$."* In the raw algebra $\mathcal{F}$, $x_1$ and $x_2$ do not commute, so the symmetrization is needed for self-adjointness. However, in the quotient $B_2$, $w(e_1,0)$ and $w(e_2,0)$ commute because $e_1 \cdot 0 + 0 \cdot e_2 = 0$.  
   *Proposed Change:* Add a brief parenthetical note pointing out that while $x_1$ and $x_2$ are non-commuting in the free algebra $\mathcal{F}$, their images in the target quotient commute, ensuring $(x_1 x_2 + x_2 x_1)/2$ projects cleanly to $w((1,1),(0,0))$.

2. **Definition of $\mathcal{W}_D$ in Proposition 7.1 (labeled 7.1 in draft):**  
   *Issue:* Proposition 7.1 assumes $\sigma_D$ is surjective onto $N(D)$ and that $\mathcal{W}_D$ has zero joint kernel. It would be helpful to note that this mirrors the standard definition of a separating family of states.

3. **Bibliography References:**  
   *Issue:* Several references ([1], [2], [3]) refer to manuscripts from 2026 with external links. Ensure consistency in citation styles and archive identifiers.

---

### Conclusion and Recommendation

This is a well-conceived, mathematically sound, and rigorously argued paper. The algebraic theorems regarding the transport of GNS kernels and the maximal compatible quotient $\widehat{K}_D$ are original, insightful, and clearly illustrated by the matrix and finite Weyl models. The paper makes a valuable conceptual contribution to the interface of algebraic quantum field theory, category theory, and local subsystem physics.

However, because the manuscript links these abstract results directly to gravitational null-cone quantization in its title and motivation, it cannot leave the functional-analytic issues of unbounded operators, Reeh-Schlieder superselection, and boundary literature unaddressed. Addressing these points through the proposed revisions will substantially strengthen the work and make it suitable for publication in a high-level mathematical physics journal.

VERDICT: REVISE
