# Pythagorean Theorem — research repo (four passes)

## Project 4 (current) — a non-circular trigonometric proof — verdict: **VARIANT / likely DUPLICATE of KUS 2025**

Search-first attempt at a non-circular trig proof using a mechanism not in the known set
(Zimba 2009, Luzia 2015, Jackson–Johnson 2024, Kise–Uehara–Shinzato 2025). Files:
`known_trig_proofs.md`, `candidates.md`, `audits.md`, `proof/FINAL_PROOF.md` (rewritten),
`verify/trig_check.py`, `NOVELTY.md`, and the Project-4 sections of `LOG.md`/`verify/README.md`.

- **Phase 0 tooling (honest):** web search ✅, SymPy ✅; **WebFetch ❌ — HTTP 403 on every
  domain** (arXiv, cut-the-knot, Wikipedia, ResearchGate), so no full paper was readable;
  all collision evidence is search-snippets only.
- **The proof (P-β):** bisect both acute angles → `tan(A/2)=a/(b+c)`, `tan(B/2)=b/(a+c)`
  (angle-bisector theorem); with `A/2+B/2=45°` and `tan45°=1`, tangent addition gives the
  exact identity `tan(A/2+B/2)−1=(a²+b²−c²)/(c(a+b+c))`, forcing `a²+b²=c²`.
  **Rigorously non-circular** (clean audit; key point: `tan45°=1` uses leg/leg, not the
  hypotenuse, unlike the circular `sin45°`). SymPy-verified algebra (with the caveat that
  SymPy can't certify non-circularity).
- **Collision (the heart):** the mechanism is KUS 2025's angle-bisector / half-angle-tangent
  route; snippets associate `tan=a/(b+c)`+`tan45°`+summed-half-angles with arXiv:2506.06304.
  **Verdict: VARIANT, very likely DUPLICATE of KUS 2025; not addable** (couldn't read the
  paper to confirm line-by-line). Two candidates died honestly: Weierstrass `t=tan(A/2)`
  is **circular**; law of tangents is **vacuous**.

Project-3 deliverables sharing filenames are archived as `ARCHIVE_project3_*`.

---

# (older) Pythagorean Theorem — research repo (three passes)

## Project 3 (current) — a dissection "addable to the catalog" — verdict: **DUPLICATE (family-level)**

Search-first attempt at a *direct, rigorous, not-already-catalogued* dissection proof.
Files: `known_dissections.md`, `candidates.md`, `collisions.md`, `proof/FINAL_PROOF.md`
(rewritten), `verify/explore.py`, `verify/inspect_candidate.py`,
`verify/verify_dissection.py`, `verify/dissection.svg`, `NOVELTY.md`, and the Project-3
sections of `LOG.md` / `verify/README.md`.

- **Phase 0 tooling (honest):** web ✅, SymPy ✅, **Shapely ✅** (2.1.2); **cut-the-knot
  unreachable** (gateway 403) → catalog evidence from search snippets only.
- **The dissection (candidate K1):** corner-anchored, **5 pieces, translation-only,
  both leg squares cut (3+2)** — fully verified by Shapely for many `(a,b)` (areas,
  zero overlap, exact unions, exact vertex maps). Rigorous and correct.
- **Collision gauntlet (the heart):** K1 is a member of the catalogued **2-parameter
  "superposition of two plane tessellations" family** (cut-the-knot `DoublePythLattice`,
  "Perigal a special case"). So K1 is **DUPLICATE (family-level)** — a *VARIANT* of the
  classic Perigal cut, but not addable. Documented with sources in `collisions.md`.
- Honest deliverable = a verified dissection + an auditable proof that it is **already
  in the catalog's tessellation family**.

Project-2 deliverables sharing filenames are archived as `ARCHIVE_project2_*` and
`proof/ARCHIVE_project2_skew_generator.md`.

---

## Earlier passes (novelty-focused)

This repo also holds **two earlier passes** at proving the theorem from scratch.

## Project 2 (current, search-first) — honest verdict: **NOT NOVEL**

A stricter, search-first attempt that treats novelty as the hard part and accepts a
documented negative as success. New files:
`candidates.md`, `prior_art.md`, `NOVELTY.md`, `proof/FINAL_PROOF.md` (rewritten),
`verify/lie_generator_check.py`, and the Project 2 sections of `LOG.md` and
`verify/README.md`.

- **Phase 0 tooling (honest):** web search ✅, SymPy ✅ (1.14, runs), Lean ❌ (no
  toolchain → Lean file is **NOT COMPILED**).
- **Gauntlet result:** five candidate foundations (SO(2)-invariant form, entropy
  power inequality, information geometry, area functional equation, skew generator)
  were each searched; all are **KNOWN / circular / route-only**. See `prior_art.md`.
- **Best survivor:** the skew-infinitesimal-generator proof (`proof/FINAL_PROOF.md`)
  — rigorous and non-circular, verified by SymPy (exact) + numeric (5.5e-16), but
  honestly **core (C)**: orthogonality via `J²=−I` and skew-adjointness
  (`B(u,Ju)=0`). **Verdict: NOT NOVEL foundationally; plausibly novel only as an
  exposition/route, confidence LOW.**
- Project 1's integral-geometry proof is **archived** (`proof/ARCHIVE_project1_*`)
  and its novelty claim is **retracted** — it rediscovered Cauchy/Crofton integral
  geometry.

The valuable deliverable is the **negative result with its audit trail**:
`NOVELTY.md` (ledger + skeptical referee) and `prior_art.md` (queries + URLs).

---

## Project 1 (archived) — original survey + integral-geometry proof

A research project that (1) surveys the full landscape of known proofs and the
mathematical fields the theorem touches, then (2) constructs and verifies a proof
on an integral-geometry foundation. **Superseded:** Project 2 shows that foundation
is not new ground. The survey files (`research/`) remain useful background.

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
