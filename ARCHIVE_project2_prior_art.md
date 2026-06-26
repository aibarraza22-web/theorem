# Phase 2 — Prior-Art Gauntlet

For each surviving candidate I tried hard to **prove it is NOT new**. Searches were
actually run via web search on 2026-06-25; queries, findings, and URLs are recorded
so the gap (or its absence) is auditable. Verdicts: **KNOWN** (closest source),
**PARTIAL** (variant/route exists or trivially adaptable), **NO PRIOR ART FOUND**.

> Tooling honesty (see `LOG.md`, Phase 0): web search and WebFetch **work**;
> SymPy **runs**; there is **no Lean toolchain** to compile. All searches below were
> performed; none are asserted without being run.

---

## C1 — SO(2)-invariant quadratic form  →  **KNOWN (textbook)**

**Queries.**
- "Pythagorean theorem proof rotation-invariant quadratic form SO(2) representation
  theory unique bilinear form"

**Findings.** Standard representation theory: for an irreducible representation,
an invariant bilinear form is unique up to scalar (Schur's lemma); for `SO(n)` the
space of invariant symmetric bilinear forms on the tangent space is
**one-dimensional**, spanned by the dot product. So "the rotation-invariant
quadratic form is `x^2+y^2` up to scale" is a textbook fact, not new ground.

**Sources.**
- Berkeley Math 252 notes, "Representation theory week 5: Invariant forms"
  https://math.berkeley.edu/~serganov/math252/notes5.pdf
- "Invariant bilinear forms under the rigid motions of a regular polygon"
  https://arxiv.org/pdf/2103.01517
- Wikipedia, "Bilinear form" https://en.wikipedia.org/wiki/Bilinear_form

**Verdict: KNOWN.** This is the structural backbone of all inner-product proofs and
is folklore. Usable as a building block, never claimable as novel.

---

## C2 — Skew infinitesimal generator (Lie algebra)  →  **PARTIAL (route; trivially adaptable by an expert)**

**Queries.**
- "Pythagorean theorem proof conserved quantity rotation flow Lie group
  infinitesimal generator"
- (plus the C1 query, which covers the invariant-form half)

**Findings.** No write-up was found that proves the *planar Pythagorean theorem*
via the skew-adjointness of the rotation generator `J` (`J^2=-I`,
`B(Ju,v)+B(u,Jv)=0 ⇒ B(u,Ju)=0`). However, every ingredient is standard:
(i) the Lie algebra of an isometry group is skew-adjoint w.r.t. the invariant
metric (textbook Riemannian geometry / Noether); (ii) `so(2)` is spanned by `J`
with `J^2=-I`; (iii) the invariant form is unique (C1). An expert would call the
orthogonality step "obvious skew-adjointness." The searches returned only generic
Lie-theory/Noether material, not this application.

**Sources.**
- Profound Physics, "Noether's Theorem: A Complete Guide"
  https://profoundphysics.com/noethers-theorem-a-complete-guide/
- Berkeley invariant-forms notes (as above) for the uniqueness half.

**Verdict: PARTIAL.** No direct prior art for *this exact packaging*, but the
mechanism is standard and **trivially adaptable**, which caps novelty at
"route/exposition, low confidence." Proceeds to Phase 3 as the best survivor —
with that ceiling stated up front.

---

## C3 — Entropy power inequality  →  **KNOWN (reduces to variance additivity)**

**Queries.**
- "entropy power inequality Gaussian variance additivity Pythagorean theorem proof
  information theory"

**Findings.** "For one-dimensional cases, the EPI **reduces to the additivity of
variances**" (and to additivity of covariances in the Gaussian case). Variance
additivity is explicitly on the exhausted list (a relabeling of core (C)). So the
EPI route is heavier machinery that collapses to an already-exhausted identity in
the only case used; equality conditions (Stam 1959) are well studied.

**Sources.**
- Wikipedia, "Entropy power inequality"
  https://en.wikipedia.org/wiki/Entropy_power_inequality
- Rioul, "Information Theoretic Proofs of Entropy Power Inequalities"
  https://arxiv.org/abs/0704.1751

**Verdict: KNOWN.** Reduces to variance additivity → core (C). Not new.

---

## C4 — Information geometry / Bregman generalized Pythagoras  →  **KNOWN + circular**

**Queries.**
- "information geometry generalized Pythagorean theorem Bregman divergence Amari
  Euclidean special case"

**Findings.** "The most basic Bregman divergence is the **squared Euclidean
distance**"; dually flat manifolds (Amari) admit a *generalized* Pythagorean
theorem that has the Euclidean case as its **base example**. So the framework
**presupposes** squared Euclidean distance; it generalizes Pythagoras rather than
proving it.

**Sources.**
- Amari, "Information geometry of divergence functions"
  https://journals.pan.pl/Content/83037/PDF/19_paper.pdf
- Wikipedia, "Bregman divergence" https://en.wikipedia.org/wiki/Bregman_divergence

**Verdict: KNOWN (and circular for our purpose).** Not usable as an independent
proof of the Euclidean case.

---

## C5 — Functional-equation / area-additivity characterization  →  **KNOWN + obstruction**

**Queries.**
- "characterization Euclidean norm functional equation rectangle additivity area
  proof Pythagorean theorem"

**Findings.** This is core (A) (area), and a well-known obstruction bites:
"*it is not as easy to prove that the area of a square is the sum of the areas of
its pieces … proving the necessary properties is harder than proving the
Pythagorean theorem itself*." So an area-additivity characterization either
reduces to a classical dissection proof or quietly assumes the hard part.

**Sources.**
- Boise State undergraduate thesis, "Pythagorean Theorem Area Proofs"
  https://scholarworks.boisestate.edu/cgi/viewcontent.cgi?article=1009&context=math_undergraduate_theses
- Wikipedia, "Pythagorean theorem"
  https://en.wikipedia.org/wiki/Pythagorean_theorem

**Verdict: KNOWN.** Core (A); no fresh ground.

---

## Landscape note (why the bar is real)

New proofs are still published regularly, and almost all are recombinations of
(A)/(B)/(C):
- arXiv 2507.02896 — "Dissecting Circles to Prove a Square" (2025): area
  decomposition of circular segments → core (A).
  https://arxiv.org/abs/2507.02896
- arXiv 2511.00089 — "Parametric proofs … via ziggurats and pyramids" (2025):
  area/dissection family. https://arxiv.org/pdf/2511.00089
- arXiv 2506.06304 — "Trigonometric Ratios Can Prove the Pythagorean Theorem"
  (2025): non-circular trig, post Jackson–Johnson → core (C).
  https://arxiv.org/abs/2506.06304
- arXiv 2301.06812 — "An uncountable number of proofs of Pythagoras Theorem":
  a continuum of dissection-type pictures, underscoring that many "distinct"
  proofs share one core. https://arxiv.org/pdf/2301.06812

This active stream of (A)/(B)/(C) recombinations is consistent with the project's
honest framing and with my gauntlet result below.

---

## Gauntlet summary

| Cand. | Foundation | Verdict | Closest prior art |
|---|---|---|---|
| C1 | SO(2)-invariant form | **KNOWN** | Schur uniqueness of invariant form (rep. theory) |
| C2 | skew generator (Lie) | **PARTIAL** | skew-adjoint isometry algebra; trivially adaptable |
| C3 | entropy power inequality | **KNOWN** | reduces to variance additivity (exhausted) |
| C4 | information geometry | **KNOWN/circular** | Amari, squared Euclidean = base case |
| C5 | area functional equation | **KNOWN** | dissection (A); area-additivity is the hard part |

**Only C2 survives as PARTIAL**, and only at the level of *route/exposition*. It
proceeds to Phase 3 with its novelty ceiling already capped.
