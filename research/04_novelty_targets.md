# Phase 4 — Choosing a Novelty Target

## The criterion for "genuinely new"

A new proof must satisfy three tests:

1. **Non-circular.** It must not use any tool whose standard construction already
   contains `a^2+b^2=c^2` — in particular not the coordinate distance formula
   `sqrt(x^2+y^2)`, not the coordinate inner product `u1v1+u2v2` taken as a
   *definition* of length, and not `sin^2+cos^2=1`.
2. **Non-relabeling.** It must not be an existing proof wearing new vocabulary
   (e.g., "variance" for "squared length" with everything else identical to the
   inner-product proof).
3. **Fresh foundation, decomposition, or route.** It should draw on a field that
   is *under-represented* among the 367+ known proofs, or combine known pieces in
   a way not previously used.

From Phase 3, the under-represented foundations are **integral geometry** and
**probability**. I evaluate the candidate routes below.

---

## Candidate 1 — Probabilistic variance additivity (evaluated, then absorbed)

**Idea.** `Var(X+Y) = Var(X)+Var(Y)` for uncorrelated `X,Y`; this is Pythagoras
in `L^2(Ω)`.

**Verdict — circular/relabeling as stated.** To turn the abstract `L^2` identity
into a statement about a *planar right triangle* you must identify the plane with
a 2-D subspace of `L^2` and the measured length with the `L^2` norm. Without an
independent reason that the `L^2` norm equals ruler-length, this is exactly the
inner-product proof (Family G) with "variance" substituted for "squared length."
Fails test 2. **However**, it is rescued if the random variable is chosen
concretely as the **projection of a fixed vector onto a uniformly random
direction** — then "variance" becomes "mean squared projection," an
*integral-geometry* quantity with independent geometric meaning. So Candidate 1 is
not discarded; it is **absorbed into Candidate 3**.

## Candidate 2 — Gaussian isotropy (Herschel–Maxwell) (rejected)

**Idea.** `exp(-(x^2+y^2)/2)=exp(-x^2/2)exp(-y^2/2)` is the unique rotationally
invariant product density, so `x^2+y^2` is the natural squared radius.

**Verdict — circular.** The rotational invariance of `exp(-(x^2+y^2)/2)` is the
rotational invariance of the quadratic form `x^2+y^2`, which *is* the Pythagorean
statement. Asserting isotropy assumes the conclusion. **Rejected.**

## Candidate 3 — Integral geometry: mean squared projection over directions (CHOSEN)

**Idea.** For a vector `u` in the plane and a direction `theta`, let `p_theta(u)`
be the **signed length of the orthogonal projection** of `u` onto a line of
direction `theta`. Average the *square* over all directions:
`Q(u) := integral_0^{2pi} p_theta(u)^2 d_theta` and, by polarization, the bilinear
pairing `B(u,v) := integral_0^{2pi} p_theta(u) p_theta(v) d_theta`.

Then (proved rigorously in `proof/FINAL_PROOF.md`):

- `B` is **bilinear and symmetric** because orthogonal projection onto a line is a
  linear map and the integrand is a product of two such projections.
- `Q(u) = c0 * L(u)^2` for a universal constant `c0>0`, by **rotation invariance +
  quadratic homogeneity** (no value of the integral, no `integral cos^2`, needed).
- `B(u,v) = 0` whenever `u perp v`, by **invariance of `B` under the reflection
  that fixes `u` and negates `v`** (no `cos(pi/2)=0`, no trig).

Hence for perpendicular legs `u,v` and hypotenuse vector `u+v` (or `v-u`):
`c0 * L(u+v)^2 = Q(u+v) = Q(u) + 2B(u,v) + Q(v) = Q(u)+Q(v) = c0(L(u)^2+L(v)^2)`,
so `c^2 = a^2 + b^2`.

**Why this passes all three tests.**

1. *Non-circular.* The only ingredients are: linearity of orthogonal projection
   (affine geometry), invariance of a circle-integral under rotations and
   reflections (the rigid-motion group, i.e. Euclidean congruence axioms), and
   quadratic homogeneity of length under scaling. None of these is the coordinate
   distance formula, the coordinate inner product, or `sin^2+cos^2=1`. The
   dedicated *Circularity audit* in the final proof verifies each fact. The
   coordinate inner product appears **nowhere** in the proof — only in the SymPy
   sanity check, clearly labeled as verification.
2. *Non-relabeling.* Unlike Family G, the inner product is **not assumed**; it is
   **manufactured** by integrating geometric projections over the rotation group.
   The orthogonality of legs is not used as `<u,v>=0`-by-fiat; it is *derived* to
   force `B(u,v)=0` via a reflection symmetry. The decomposition `Q(u+v)=...` over
   a *continuum* of directions (a Parseval-over-the-circle) is structurally
   different from a single inner-product expansion in a fixed basis.
3. *Fresh foundation.* Integral geometry over the rotation group is essentially
   absent from Loomis's 367 and from the standard textbook families. It is also
   the honest home of the probabilistic idea (Candidate 1): with `theta` uniform,
   `B(u,v)/(2pi) = E[p_theta(u) p_theta(v)]` is a covariance and `Q(u)/(2pi)` a
   variance, so this single proof realizes *both* under-mined foundations at once.

**Closest existing proof (for the honesty of the novelty claim).** The nearest
relative is the inner-product proof (Family G) — both end with
`||u+v||^2=||u||^2+||v||^2`. The genuine novelty is the **route to the inner
product and to orthogonality**: a Cauchy-style averaging over directions plus a
reflection-symmetry argument, rather than a coordinate definition. This is best
described honestly as a **fresh synthesis on a new foundation**, not an
unprecedented theorem. The final proof's *Novelty claim* states exactly this.

**Decision.** Build Candidate 3. Keep Candidates 1 and 2 documented as the
probabilistic absorption and the rejected isotropy route, respectively.
