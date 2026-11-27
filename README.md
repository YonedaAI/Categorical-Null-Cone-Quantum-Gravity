# Categorical Null-Cone Quantum Gravity

Can a gravitational measurement reconstructed from local probes be identified with an observable obtained by quantizing null initial data, and does that identification survive an enlargement of the region? This repository develops that question for causal diamonds. It contains the first three papers in the proposed series, a synthesis, and Lean 4 proofs of selected algebraic results.

[Read the series](https://categorical-null-cone-quantum-gravity.vercel.app/) · [Start with the perspective](https://categorical-null-cone-quantum-gravity.vercel.app/read/synthesis/) · [Primary source notes](context/README.md)

| Paper | Main calculation | Manuscript |
| --- | --- | --- |
| I. Categorical Foundations of Null-Cone Quantization | Binary probe words and shift/phase matrices give a trace-preserving correspondence from one bit to two. A missing-sector example shows why the same construction can fail for local probes. | [PDF](papers/pdf/foundations.pdf) · [LaTeX](papers/latex/foundations.tex) |
| II. Derived Gauge Reduction and Quantum Observable Algebras | A linear translation constraint leaves one relative canonical pair. A duplicated constraint creates a degree −1 Koszul class. On a graph, a nonzero cycle sum obstructs a consistent assignment of quantum matching levels. | [PDF](papers/pdf/reduction.pdf) · [LaTeX](papers/latex/reduction.tex) |
| III. Gravitational Gluing and Categorical Descent | For finite boundary kernels, two choices of cut agree on specified preparations and detectors precisely when their compressed matching projectors coincide. | [PDF](papers/pdf/gluing.pdf) · [LaTeX](papers/latex/gluing.tex) |
| The Categorical Null-Cone Realization Conjecture | The perspective states the comparison, gives a one-arrow test, and explains how a candidate effective action would have to reproduce the vacuum one-loop backreaction calculation. | [PDF](papers/pdf/synthesis.pdf) · [LaTeX](papers/latex/synthesis.tex) |

The four-dimensional realization conjecture remains open. Its first physical test requires a specified inclusion of decorated diamonds and two independently constructed images of the same boundary observable. Matter coupling, a categorical derivation of the Einstein action, black-hole entropy matching and cosmological predictions depend on further work. Volumes IV through VII are outlined in the perspective.

## Formal results

The Lean project covers the shift/phase product sign and controlled-NOT embedding on signed basis states, the ring-level comparison on generators, the universal property of the stable invisible ideals on an inclusion preorder, descent to an orbit-type quotient, the triangle consistency condition and finite matrix sewing. The verification notes give exact theorem names, hypotheses and reproduction commands. [Lean sources](lean/Cmrps) · [Verification notes](verification/README.md)

A follow-up traces seven of the original manuscripts to dated Git commits and checks a proposed identification of observables. Two opposite matrix units prove that a homomorphism from the commutative classical observable algebra cannot be onto the full matrix algebra. The same obstruction applies to a bounded-operator algebra on a Hilbert space of dimension at least two. [Source comparison](context/manuscript-comparison.md) · [Lean proof](lean/Cmrps/ClassicalImage.lean)

## Build the papers and readers

The PDFs and HTML reading editions are included. To rebuild one manuscript, install TeX Live with `latexmk` and `make4ht`, and run the following from the repository root. The HTML renderer uses `uv` to supply its pinned Python parser.

```sh
uv run scripts/render_reader.py synthesis
```

Replace `synthesis` with `foundations`, `reduction` or `gluing` to rebuild another paper. The page-one sidebar is a manuscript label. The repository and website are the publication locations for this installment.

## Run the website

The static build reads the checked-in HTML editions and PDFs. It needs Python 3 and serves mathematical notation as native MathML. Fonts and figures ship with the site.

```sh
python3 scripts/build_site.py
python3 -m http.server 8000 --directory dist
```

With the site running and Google Chrome installed, check the readers at phone, tablet and desktop widths and verify the four PDF downloads.

```sh
uv run scripts/check_site.py http://127.0.0.1:8000
```

The diagram uses null sheets in a flat spacetime with two spatial dimensions. Its circular corner illustrates the intersection of the sheets. In four spacetime dimensions the corresponding round corner is a two-sphere. [Figure source](scripts/diamond_figure.py)

## Authorship and review

The byline follows the earlier YonedaAI manuscripts. Codex drafted and revised this installment, AGY reviewed the scientific manuscripts, and Claude reviewed the Lean and publication code. The repository includes their reports and the output of the Lean kernel checks. [Review records](reviews) · [Build output](verification/lean-build.txt) · [Axiom dependencies](verification/lean-axioms.txt)
