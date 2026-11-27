# Paper I and Lean

The algebraic ring version of Lemma 7.2 corresponds to the two declarations below. The statements in Lean quantify over ordinary rings, subrings and ring homomorphisms. The star-algebra version, `Cmrps.star_natural_on_arrow`, includes the scalar and involution structure and uses generation as a star algebra.

- Cmrps.agree_of_generates
- Cmrps.natural_on_arrow

The ring-level restriction of Theorem 6.1 to regions forming an inclusion preorder is expressed using two-sided ideals. These declarations treat an arbitrary family of ideals, which can then model the invisible ideals.

- Cmrps.RingTransport.mem_stableKernel
- Cmrps.RingTransport.stableKernel_le
- Cmrps.RingTransport.map_mem_stableKernel
- Cmrps.RingTransport.stableKernel_greatest

The gravitational construction of the ideals, GNS domain and linearized corner observables requires inputs beyond these statements.

The signed basis model in `Cmrps.Pauli` checks the product sign, the controlled flip involution and its conjugation on transported words. The matrix-algebra spanning result is proved in Paper I.
