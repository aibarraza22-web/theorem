# Phase 3 — Mathematical Fields Connected to the Theorem

For each field: the **precise connection**, and a note on whether it could seed a
*genuinely fresh* (non-circular, non-relabeling) proof. "Circular" below means the
field's standard development already encodes `a^2+b^2=c^2` (typically as the
definition of the Euclidean norm or as `sin^2+cos^2=1`).

---

### 1. Euclidean & synthetic geometry
**Connection.** The theorem is *Elements* I.47; it is equivalent, over the other
axioms, to the **parallel postulate** (it fails in hyperbolic/spherical geometry,
where `cosh c = cosh a cosh b` resp. `cos c = cos a cos b` replace it). So
Pythagoras is a *signature of flatness*.
**Fresh-proof potential.** High but well-mined; the congruence/shear route (I.47)
is classical. Its **congruence and reflection axioms**, used *without* the area
machinery, are exactly what the new proof borrows (symmetry, not area).

### 2. Theory of similarity / proportion
**Connection.** Altitude-to-hypotenuse proof (Euclid VI): sub-triangles similar to
the whole give `a^2=cp, b^2=cq`. Area scales as (length)^2.
**Fresh-proof potential.** Low — heavily used (Families C, F). Any "new" proof
that secretly uses similarity of the two sub-triangles is a C-relabeling.

### 3. Area / measure theory
**Connection.** All dissection and shear proofs (Families A, B, D) equate areas;
"square of a length" is literally an area. Measure additivity under disjoint union
is the engine.
**Fresh-proof potential.** Saturated. But *measure on the space of directions*
(rather than on the plane) is essentially untouched — see field 17.

### 4. Trigonometry
**Connection.** `sin^2 + cos^2 = 1` is the Pythagorean theorem on the unit circle;
the **law of cosines** `c^2 = a^2 + b^2 - 2ab cos C` is the general triangle
identity that *reduces* to Pythagoras at `C = 90°`.
**Fresh-proof potential.** Dangerous (circularity) but proven possible (Zimba;
Jackson–Johnson) if the needed identities are built without `sin^2+cos^2=1`. The
new proof deliberately **avoids all trig identities**, replacing them by symmetry.

### 5. Analytic / coordinate geometry
**Connection.** Distance formula `d=sqrt((Δx)^2+(Δy)^2)` *is* Pythagoras in
coordinates.
**Fresh-proof potential.** None as a foundation: using the distance formula to
"prove" the theorem is circular. Coordinates are fine only as a *verification*
device (see SymPy/Monte-Carlo), not as the proof's basis.

### 6. Linear algebra & inner-product spaces
**Connection.** `||u+v||^2 = ||u||^2 + 2<u,v> + ||v||^2`; orthogonality
`<u,v>=0` gives the theorem (Family G). The theorem is the abstract identity for
any real inner product.
**Fresh-proof potential.** Moderate but the danger is defining `<u,v>=u1 v1+u2 v2`
(circular). The new proof **constructs** the inner product by integrating
projections, so it does not assume the coordinate form — this is the crux of its
novelty.

### 7. Hilbert spaces (infinite-dimensional Pythagoras)
**Connection.** **Parseval/Plancherel**: `||f||^2 = sum |<f,e_n>|^2` over an
orthonormal basis is the infinite-dimensional Pythagorean theorem; orthogonal
decompositions `H = M ⊕ M^perp` give `||x||^2 = ||P x||^2 + ||(I-P)x||^2`.
**Fresh-proof potential.** Conceptually it generalizes rather than reproves the
planar case; but the **projection viewpoint** (norm^2 = sum of squared projections)
directly inspires the integral-geometry proof (sum over a *continuum* of
directions instead of a discrete basis).

### 8. Vector calculus
**Connection.** Gradient/divergence in orthogonal coordinates; arc length
`ds^2 = dx^2 + dy^2` is an infinitesimal Pythagoras.
**Fresh-proof potential.** Low; `ds^2=dx^2+dy^2` is the metric, assumed.

### 9. Complex analysis
**Connection.** `|z|^2 = z conj(z) = (Re z)^2 + (Im z)^2` (Family H); rotations are
multiplication by `e^{i theta}`, `|e^{i theta}|=1`.
**Fresh-proof potential.** Low (circular as above); but the **rotation group**
`{e^{i theta}}` as a measure space of directions feeds the new proof.

### 10. Differential equations
**Connection.** The relation `y dy = x dx` (Family F) is an ODE whose solution is
`y^2 - x^2 = const`; more deeply, isotropy + a heat/diffusion semigroup forces a
quadratic form.
**Fresh-proof potential.** The naive ODE proof reduces to similarity. A genuinely
DE-based proof would need an independent reason for the isotropy of the
generator — hard to make non-circular (see `04_novelty_targets.md`, rejected
Gaussian route).

### 11. Number theory
**Connection.** **Pythagorean triples** `(m^2-n^2, 2mn, m^2+n^2)`; Fermat's Last
Theorem is the `n>2` non-existence statement; sums of two squares (Fermat's
Christmas theorem) and Gaussian integers `Z[i]`.
**Fresh-proof potential.** None for the *geometric* theorem (these study integer
solutions of an assumed relation), but rich for generalizations.

### 12. Abstract algebra — Clifford / geometric algebra, quaternions
**Connection.** Clifford relation `e_i e_j + e_j e_i = 2 delta_ij` makes
`(a e_1 + b e_2)^2 = a^2 + b^2` (Family I1). Quaternion norm is multiplicative.
**Fresh-proof potential.** Low: the defining relation *is* orthonormality
(Pythagoras built in).

### 13. Differential geometry — metric tensor, law of cosines
**Connection.** The metric tensor `g_{ij}`; in an **orthonormal frame**
`g_{ij}=delta_{ij}` and `|v|^2 = sum (v^i)^2`. The **law of cosines is the
non-orthogonal generalization**: `|v|^2 = g_{ij} v^i v^j` with off-diagonal `g`.
Pythagoras = diagonal metric = orthonormal frame exists = flat + a chosen
orthonormal basis.
**Fresh-proof potential.** Moderate, but "orthonormal" presupposes the norm.
Useful mainly to *frame* what the theorem really asserts (diagonalizability of the
metric / existence of an isotropic quadratic form).

### 14. Probability & statistics
**Connection.** For **independent** (or merely uncorrelated) `X,Y`:
`Var(X+Y) = Var(X) + Var(Y)` — the Pythagorean theorem in `L^2(Ω)` with
`<X,Y>=Cov(X,Y)`. The **ANOVA / regression decomposition**
`SS_total = SS_explained + SS_residual` is `||y||^2 = ||hat y||^2 + ||y - hat y||^2`,
orthogonality of fitted values and residuals — Pythagoras again. Conditional
expectation `E[X | G]` is the `L^2` orthogonal projection.
**Fresh-proof potential.** **High as a foundation, but with a trap:** to make it a
*geometric* proof you must connect the `L^2` norm to measured length. Done naively
it relabels Family G. **Done well** — by realizing the random object as a *uniform
random direction* and the "variance" as the mean squared projection — it becomes
the integral-geometry proof and is genuinely new. (This is the chosen route.)

### 15. Fourier analysis
**Connection.** Plancherel `||f||_2 = ||hat f||_2` is Pythagoras for the Fourier
orthonormal system; the theorem is "energy is preserved across an orthonormal
change of basis."
**Fresh-proof potential.** A reformulation, not an independent proof of the planar
case; but reinforces the "sum of squared projections" intuition.

### 16. Information geometry
**Connection.** The **generalized Pythagorean theorem for Bregman/KL divergence**:
for `p, q, r` with `r` the projection of `q` onto a flat submanifold containing
`p`, `D(p||q) = D(p||r) + D(r||q)`. A non-Euclidean echo of orthogonal
decomposition.
**Fresh-proof potential.** It *generalizes* the idea but cannot prove the metric
case without the metric; interesting for the "what is Pythagoras really" essay,
not a clean new planar proof.

### 17. Integral geometry / geometric probability  ← **the under-mined field**
**Connection.** **Cauchy's formula**: the length/perimeter of a convex curve equals
(up to a constant) the average of its projected widths over all directions; the
**mean squared projection** of a segment over all directions is proportional to its
squared length. Measure lives on the **space of directions/lines** (the rotation
group), not on the plane.
**Fresh-proof potential.** **Highest and least exploited.** Averaging the *squared*
projection over the rotation group builds a rotation-invariant quadratic form whose
diagonal is (proportional to) squared length and whose off-diagonal vanishes for
perpendicular vectors *by reflection symmetry*. This yields `c^2=a^2+b^2` without
coordinates, without `sin^2+cos^2=1`, and without similarity of sub-triangles. It
is essentially **absent from Loomis's 367**. **Chosen foundation.**

---

## Ranking for novelty (input to Phase 4)

1. **Integral geometry over the rotation group** — freshest, non-circular: **chosen.**
2. **Probability / second moments** — same mathematical core when the random
   object is a uniform direction; unify with #1.
3. Differential equations (isotropy) — appealing but hard to de-circularize.
4. Information geometry / Hilbert / Fourier — generalizations, not independent
   planar proofs.
5. Coordinate geometry, Clifford algebra, trig (standard) — circular as
   foundations; usable only for verification or as cautionary contrasts.
