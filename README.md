# An Original Proof of the Pythagorean Theorem from First Principles

A research project that (1) surveys the full landscape of known proofs and the
mathematical fields the theorem touches, then (2) constructs and rigorously
verifies a **new** proof that is not a re-skin of an existing one.

## The new proof in one paragraph

For a planar vector `u` and a direction `θ`, let `p_θ(u)` be the **signed length
of the orthogonal projection** of `u` onto the line of direction `θ`. Average the
square over all directions, `Q(u) = ∫₀^{2π} p_θ(u)² dθ`, and form the bilinear
pairing `B(u,v) = ∫₀^{2π} p_θ(u)p_θ(v) dθ`. Then **(Lemma 2)** `Q(u) = c0·L(u)²`
for a universal `c0>0`, by rotation invariance plus quadratic homogeneity — *the
value of the integral is never needed*; and **(Lemma 3)** `B(u,v)=0` whenever
`u⟂v`, because the reflection that fixes `u` and negates `v` preserves `B`. For a
right triangle with legs `u,v` and hypotenuse `v−u`,
`c0·c² = Q(v−u) = Q(u)+Q(v) = c0·(a²+b²)`, so `a²+b²=c²`. No coordinates, no
inner-product formula, no `sin²+cos²=1`.

The foundation — **integral geometry over the rotation group** (mean squared
projection), which also carries the **probabilistic** reading (variance/covariance
of a random direction) — is essentially absent from Loomis's 367 proofs. See
`proof/FINAL_PROOF.md` for the full development, figure, circularity audit, and an
honest novelty claim.

## Repository layout

```
research/
  01_proof_catalog.md     Every proof family + worked representatives (Loomis, cut-the-knot)
  02_history.md           Authorship, dates, primary sources; legend vs. record
  03_math_fields.md       Every connected field + its precise link + fresh-proof potential
  04_novelty_targets.md   Under-mined foundations; choice + justification
proof/
  candidate_proofs.md     3 drafted candidates with critique (2 rejected, 1 chosen)
  FINAL_PROOF.md          The chosen proof: axioms, lemmas, figure, circularity audit, novelty
verify/
  symbolic_check.py       SymPy: all lemma identities hold (PASS)
  monte_carlo.py          Random right triangles + MC pairing estimate (PASS)
  lean/Pythagoras.lean    Lean 4 / mathlib: abstract core step (written; toolchain absent)
  README.md               What was and wasn't verified
LOG.md                    Running decisions, dead ends, referee self-critique
```

## Reproduce the verification

```bash
pip install sympy
python3 verify/symbolic_check.py     # ALL SYMBOLIC CHECKS: PASS
python3 verify/monte_carlo.py        # OVERALL: PASS
```

## Honesty notes

- The proof's *conclusion line* necessarily matches the inner-product proof
  (Family G); what is new is the **route and foundation** (constructed metric from
  averaged shadows; orthogonality from reflection symmetry), documented in the
  Novelty Claim of `FINAL_PROOF.md`.
- The Lean file formalizes only the abstract endpoint; the integral-geometric
  construction is not formalized, and no Lean toolchain was available to compile it
  in this environment. Stated plainly in `verify/README.md`.
- `LOG.md` keeps the dead ends (naive variance proof; Gaussian isotropy) because
  they explain why the final proof is shaped the way it is.
