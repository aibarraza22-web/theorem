# Phase 1 — Candidate Routes (search-first project)

Goal: brainstorm routes biased AWAY from the known-exhausted list, with an upfront
self-assessment of which core each likely reduces to —
(A) area/dissection, (B) similarity/scaling, (C) bilinearity+orthogonality
(inner products, vectors, trig, integral geometry, probability/variance,
determinant/Gram) — and what, if anything, might be genuinely fresh.

Candidates killed on sight (obviously (A)/(B)/(C) or no honest meaning) are marked
KILL. Survivors proceed to the Phase 2 prior-art gauntlet (`prior_art.md`).

> Note on the previous project (Project 1, archived in `proof/ARCHIVE_*`): its
> "mean squared projection over the rotation group" proof was an *integral-geometry*
> (Cauchy/Crofton) construction of the rotation-invariant inner product. That
> foundation is now on the exhausted list; none of the candidates below may reuse
> it as novel ground. The recurring lesson it taught — that "Pythagoras = the
> measured length-squared is the rotation-invariant quadratic form" — is the
> yardstick against which I judge each candidate's freshness.

---

## C1 — SO(2)-invariant quadratic form (representation theory)
**Sketch.** The squared-length function is a quadratic form on `R^2` invariant
under the rotation group `SO(2)`. By Schur-type uniqueness, the space of
`SO(2)`-invariant symmetric bilinear forms is 1-dimensional; the invariant form is
`x^2+y^2` up to scale. Pythagoras is then the orthogonal-additivity of that unique
form.
**Self-assessment.** Core **(C)**. Fresh? *Thin* — this is the structural reason
behind every inner-product proof, but it might be a cleaner "foundation." **Risk:
textbook.** Proceed to gauntlet.

## C2 — Skew infinitesimal generator (Lie algebra of rotations)
**Sketch.** Let `J` be the generator of the rotation one-parameter group: rotation
by a right angle. Two right-angle turns equal central inversion, so **`J^2 = -I`**
(a purely geometric fact, no metric formula). The rotation-invariant form `B`
makes `J` **skew**: `B(Ju,v)+B(u,Jv)=0`. Hence `B(u,Ju)=0` for every `u` — the
cross term vanishes "for free" — and since a vector perpendicular to `u` is exactly
`λJu`, `Q(u+λJu)=Q(u)+Q(λJu)`, i.e. `a^2+b^2=c^2`.
**Self-assessment.** Core **(C)**. Fresh? *Route/exposition only* — the
orthogonality comes from skew-adjointness of the isometry Lie algebra, a different
*mechanism* than a coordinate dot product or an average over the group. **Risk:
the skew-adjointness fact is standard differential geometry.** Proceed to gauntlet;
this is the most promising for a clean rigorous write-up.

## C3 — Entropy power inequality (information theory)
**Sketch.** For independent `X,Y`, the entropy power `N(·)=e^{2h(·)}/(2πe)`
satisfies `N(X+Y) ≥ N(X)+N(Y)`, with **equality iff Gaussian**. For 1-D Gaussians
`N = Var`, so equality gives `Var(X+Y)=Var(X)+Var(Y)`. Interpret legs as
independent Gaussian coordinates; the equality case is Pythagoras.
**Self-assessment.** Core **(C)** (reduces to variance additivity, explicitly on
the exhausted list). The EPI is heavier machinery but collapses to the same
identity in the only case used. **Likely KNOWN/relabeling.** Proceed to gauntlet to
confirm.

## C4 — Information geometry / Bregman "generalized Pythagorean theorem"
**Sketch.** A dually flat manifold (Amari) satisfies a generalized Pythagorean
relation `D(p‖q)=D(p‖r)+D(r‖q)` for a Bregman divergence `D`. Take `D` = squared
Euclidean distance to recover the classical theorem.
**Self-assessment.** Core **(C)**, and **circular for our purpose**: squared
Euclidean distance is the *base example* the framework generalizes, so it
presupposes the result. Proceed to gauntlet to document the circularity.

## C5 — Functional-equation / area-additivity characterization
**Sketch.** Characterize the area function by additivity + congruence-invariance +
scaling, then derive `a^2+b^2=c^2` as the unique consistent assignment.
**Self-assessment.** Core **(A)**. Fresh? No — and a known subtlety bites:
*proving area is additive on the relevant dissections is itself harder than
Pythagoras*. Proceed to gauntlet to cite the obstruction.

## C6 — Tropical / max-plus geometry
**Sketch.** Re-interpret "length" in the `(max,+)` semiring and look for a
Pythagorean analogue.
**Self-assessment.** **KILL.** In tropical geometry the natural "distance" is an
`L^∞`/max object; the honest statement degenerates to `max(a,b)` relations, *not*
`a^2+b^2=c^2`. No honest meaning for the theorem; not a proof of it.

## C7 — p-adic / valuation-theoretic
**Sketch.** Replace the real absolute value by a `p`-adic valuation and seek a
Pythagorean identity.
**Self-assessment.** **KILL.** The `p`-adic "norm" is non-archimedean
(ultrametric); there is no right-triangle/Euclidean content. No honest meaning.

## C8 — Heat-kernel / Brownian isotropy
**Sketch.** The 2-D heat kernel factors `∝ e^{-x^2/4t} e^{-y^2/4t}` and is
rotationally symmetric, so `x^2+y^2` is the natural squared radius.
**Self-assessment.** **KILL (circular).** Rotational symmetry of
`e^{-(x^2+y^2)/4t}` *is* the rotation-invariance of `x^2+y^2`, i.e. the conclusion.
(Project 1 already rejected the Gaussian-isotropy version for exactly this reason.)

## C9 — Optimization / projection theorem (KKT)
**Sketch.** The foot of the perpendicular from a point to a line minimizes
distance; first-order optimality gives orthogonality, then Pythagoras.
**Self-assessment.** Core **(C)** — this *is* the Hilbert-space projection theorem.
**KNOWN.** Listed for completeness; not pursued.

---

## Survivors into the Phase 2 gauntlet
C1, C2, C3, C4, C5 (C6, C7, C8, C9 killed above). Best a-priori shot at a clean,
rigorous, defensibly-fresh *route*: **C2 (skew generator)**, with C1 as its
structural backbone.
