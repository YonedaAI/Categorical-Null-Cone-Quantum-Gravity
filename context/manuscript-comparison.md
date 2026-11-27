# What the dated manuscripts establish

Seven YonedaAI manuscripts named in the conversation have copies in Git commits that GitHub verified before Chandrasekaran submitted his null-cone preprint on 25 November 2026. They document a categorical use of causal diamonds, a classical construction of gauge-invariant observables, and several models of gluing and reconstruction. The observable formulas give a way to decide how far that overlap extends. [Null-cone preprint, v1](https://arxiv.org/abs/2611.34924v1)

## Dating the copies

I computed the Git blob ID of each PDF served by YonedaAI and matched it to the blob at the corresponding path in a pinned commit. All seven matched. The dates below come from the title pages and GitHub’s persistent signature-verification records. The latter establish when GitHub had verified a commit containing those bytes. Establishing the first public release anywhere, or who first proved a theorem, requires additional evidence. [GitHub’s explanation of signature verification](https://docs.github.com/en/authentication/managing-commit-signature-verification/about-commit-signature-verification)

| Manuscripts | Printed date | GitHub verified the commit (UTC) | Pinned files and verification record |
| --- | --- | --- | --- |
| *Quantum Gravity and Emergent Spacetime from Perspectival Structure* | 24 Feb 2026 | 25 Feb 2026 at 04:17:47 | [Paper directory](https://github.com/MagnetonIO/quantum-gravity-emergent-spacetime/tree/46fd5fb383eb29a22bdb5ba292a49e49f0a185ac/papers) · [GitHub API](https://api.github.com/repos/MagnetonIO/quantum-gravity-emergent-spacetime/commits/46fd5fb383eb29a22bdb5ba292a49e49f0a185ac) |
| Five papers on BV–BRST, factorization algebras, Lorentzian geometry, spin foams and tensor networks | 6 Jul 2026 | 7 Jul 2026 at 05:21:59 | [Paper directory](https://github.com/YonedaAI/math-qg-representation-library/tree/82a8e3c499d3fef0b470e928b143f082cd99aa1b/papers/pdf) · [GitHub API](https://api.github.com/repos/YonedaAI/math-qg-representation-library/commits/82a8e3c499d3fef0b470e928b143f082cd99aa1b) |
| *A Representation-Theoretic Foundation for Quantum Gravity* | 7 Jul 2026 | 8 Jul 2026 at 03:53:47 | [Paper directory](https://github.com/YonedaAI/condensed-representation-theory-of-physics/tree/c43ca98a832c59ece97dde03c54ad313bb9ba636/papers/pdf) · [GitHub API](https://api.github.com/repos/YonedaAI/condensed-representation-theory-of-physics/commits/c43ca98a832c59ece97dde03c54ad313bb9ba636) |

To repeat a match, download a PDF from the next table and run `git hash-object <downloaded-file>`. In a clone of the linked repository, run `git rev-parse <commit>:<path>` for the same paper. Compare the two IDs and read `commit.verification.verified_at` in the linked API record.

The chronology extends back further on the null-boundary side. In 2019 Chandrasekaran and Prabhu studied vacuum gravitational charges and symmetries on causal diamonds. In January 2026 Chandrasekaran and Flanagan treated subregion algebras in classical and perturbative gravity. The November paper proposes a nonperturbative quantization from reduced null data. Any priority claim has to specify which of these results it concerns. [2019 paper](https://arxiv.org/abs/1908.00017) · [January preprint](https://arxiv.org/abs/2601.07915v1) · [November preprint](https://arxiv.org/abs/2611.34924v1)

## What to compare

| YonedaAI manuscript | What the cited passage supplies | What a null-cone comparison would need |
| --- | --- | --- |
| [Quantum Gravity and Emergent Spacetime, Example 4.8](https://yonedaai.com/papers/pdf/quantum-gravity-emergent-spacetime.pdf) | A category of diamonds in Minkowski space, with inclusions and a covering rule. | A prescription for transporting a dressed measurement from a smaller diamond to a specified cut of a larger one. |
| [Observables as Cohomology, Theorem 7.1](https://yonedaai.com/papers/pdf/library/math-qg-library/bv-brst-derived-geometry.pdf) | Degree-zero classical BV cohomology with its commutative product. Its on-shell interpretation uses regularity assumptions. | A quantum product or an independently reconstructed quantum observable algebra with the required commutators. |
| [Observables from Gluing, Theorem 3.9 and §4](https://yonedaai.com/papers/pdf/library/math-qg-library/factorization-algebras.pdf) | Interval factorization gives an associative product, illustrated by a finite group-algebra model. | Operators on a gravitational cut, shared charge matching, and a comparison between different choices of cut. |
| [The Solution Stack of General Relativity, Proposition 3.3](https://yonedaai.com/papers/pdf/library/math-qg-library/lorentzian-geometry.pdf) | The stabilizer of an Einstein solution records its isometries. | A determination of which transformations are gauge and which carry a charge once a null frame and boundary data are fixed. |
| [Covariant Quantum Geometry as a State Sum, §3.4 and §7](https://yonedaai.com/papers/pdf/library/math-qg-library/spin-foams.pdf) | Composition along a common spin-network boundary, with a separate refinement problem. | An identification of those boundary states and their pairing with the states and pairing of a null cap. |
| [Many Boundary Representatives, One Bulk Operator, Proposition 3.5 and §6.1](https://yonedaai.com/papers/pdf/library/math-qg-library/tensor-networks-qec.pdf) | An operator on a code space can have several boundary representatives. The pentagon example constructs representatives explicitly. | A specified gravitational state space and a test that the representatives give the same physical matrix elements there. |
| [A Representation-Theoretic Foundation for Quantum Gravity, Theorems 5.7–5.8](https://yonedaai.com/papers/pdf/library/condensed-representation/part6-condensed-quantum-gravity.pdf) | Recovery of a finite weighted graph’s path distance from spectral data. | A Lorentzian causal structure, scale, and dynamics on the proposed continuum domain. |

The February paper has two numbering schemes. Use the following pairs when following citations from the chat. They refer to the same passages. [HTML edition](https://www.yonedaai.com/papers/quantum-gravity-emergent-spacetime.html) · [PDF edition](https://yonedaai.com/papers/pdf/quantum-gravity-emergent-spacetime.pdf)

| Passage | HTML reader | PDF |
| --- | --- | --- |
| Diamond topology | Example 17 | Example 4.8 |
| Einstein equation and scope of the derivation | Conjecture 29, Remark 30 | Conjecture 6.3, Remark 6.4 |
| Boundary reconstruction | Theorem 33 | Theorem 7.3 |
| Entropy coefficient and area bound | Remark 36, Proposition 37 | Remark 7.6, Proposition 7.7 |

## A direct algebraic test

Can the ordinary product on the classical BV observables already give the whole quantum operator algebra? Let $A$ be the degree-zero classical algebra in Long’s Theorem 7.1. If $F$ preserves multiplication, any two elements in its image commute, since $F(a)F(b)=F(ab)=F(ba)=F(b)F(a)$. In Chandrasekaran’s Gaussian representation, Eq. (4.17) identifies the bicommutant of the represented algebra with $B(\mathcal H_\omega)$. On a Hilbert space of dimension at least two, choose orthonormal vectors $e_0,e_1$ and the two operators that take one to the other and vanish on the orthogonal complement of their respective input lines. Their products in opposite orders are the projections onto $e_0$ and $e_1$. These are different even on the vector $e_0$. Hence no product-preserving map from $A$ is onto that full factor. [Classical BV algebra](https://yonedaai.com/papers/pdf/library/math-qg-library/bv-brst-derived-geometry.pdf) · [Null-cone representation, §4.2](https://arxiv.org/html/2611.34924v1)

The same obstruction applies to generating the factor by taking the bicommutant of a bounded, involution-preserving image. If $C$ is that commutative image then $C\subseteq C'$. Taking commutants reverses inclusions, so $C''\subseteq C'$. Every element of $C''$ commutes with every element of $C'$, hence with every element of $C''$. The bicommutant is still commutative. This argument allows proper commutative subalgebras, such as bounded functions of a single measured area.

The Lean module proves the surjectivity obstruction and its finite-matrix witness. The Hilbert-space and bicommutant arguments above are given in prose. An independently constructed quantum product on the categorical side could pass this test. The next comparison would then use two ordered probe measurements on a marked diamond and ask whether their commutator survives transport to the larger region. The published perspective already works through the area of one marked cut and explains which ordering data are still missing. [Lean proof](../lean/Cmrps/ClassicalImage.lean) · [Perspective, §4](../papers/latex/synthesis.tex)

The Einstein-equation comparison asks a different question. The February sketch assumes a geometric action with an Einstein–Hilbert limit. Chandrasekaran’s Eq. (6.13) computes a vacuum one-loop term from the graviton covariance under the preprint’s assumptions. Neither calculation measures the comparative accuracy of the two approaches. An empirical ranking would require distinct predictions for the same observable and observations against which to test them. [February paper, §6.3](https://yonedaai.com/papers/pdf/quantum-gravity-emergent-spacetime.pdf) · [Null-cone preprint, §6.2](https://arxiv.org/html/2611.34924v1)
