# Candidate Original Proofs (with critique)

Three drafted candidates. Each is followed by a referee-style critique. The third
is selected and promoted to `FINAL_PROOF.md`.

---

## Candidate I — Variance additivity in L^2(Ω)

**Sketch.** Model the two legs as mean-zero random variables `X, Y` on a
probability space, uncorrelated (`E[XY]=0`). Then
`Var(X+Y) = E[(X+Y)^2] = E[X^2] + 2E[XY] + E[Y^2] = Var(X)+Var(Y)`.
Interpret `sqrt(Var)` as length; orthogonal legs are uncorrelated; done.

**Critique.** *Rejected as the final proof.* The argument is correct in `L^2` but
to make it a statement about a **planar** right triangle one must declare that the
measured side lengths equal the standard deviations and that perpendicularity
equals zero correlation. With no independent justification, this is the
inner-product proof (Family G) with renamed symbols — it fails the
"non-relabeling" test. Its salvage is to make the random object concrete (a random
*direction*), which turns it into Candidate III. Kept as motivation, not as the
deliverable.

---

## Candidate II — Heat-kernel / isotropy argument

**Sketch.** The 2-D heat kernel `K_t(x,y) ∝ exp(-(x^2+y^2)/(4t))` factors as a
product of 1-D kernels and is rotationally symmetric; the exponent's level sets are
"circles," so `x^2+y^2` is the natural squared distance, and orthogonal
displacements add in quadrature.

**Critique.** *Rejected.* The rotational symmetry of the kernel is the
rotation-invariance of `x^2+y^2`, i.e. the theorem itself. Asserting the kernel is
isotropic assumes Pythagoras. Circular. (Logged as the rejected Gaussian/heat
route.)

---

## Candidate III — Mean squared projection over the rotation group (SELECTED)

**Sketch.** For a planar vector `u` and a direction angle `theta`, let
`p_theta(u)` be the **signed length of the orthogonal projection** of `u` onto a
line in direction `theta`. Define
```
Q(u) = ∫_0^{2π} p_theta(u)^2  d_theta ,
B(u,v) = ∫_0^{2π} p_theta(u) p_theta(v)  d_theta  =  (1/4)(Q(u+v) − Q(u−v)).
```
Three lemmas:
- **(Bilinearity)** `p_theta` is linear in its vector argument (orthogonal
  projection onto a line is linear), so `B` is a symmetric bilinear form and
  `Q(u)=B(u,u)`.
- **(Proportionality)** `Q(u) = c0 · L(u)^2`, where `L` is Euclidean length and
  `c0>0` is universal — by rotation invariance of the circle-integral plus
  `Q(λu)=λ^2 Q(u)`.
- **(Orthogonality)** If `u ⟂ v`, the reflection `σ` across the line of `u`
  fixes `u`, sends `v ↦ −v`, and preserves `B`; hence
  `B(u,v)=B(u,−v)=−B(u,v)`, so `B(u,v)=0`.

For a right triangle with legs `u, v` (right angle between them) and hypotenuse
vector `v − u`:
```
c0·c^2 = Q(v−u) = Q(v) − 2B(u,v) + Q(u) = Q(u)+Q(v) = c0·(a^2+b^2),
```
so `a^2+b^2=c^2`.

**Critique.** *Accepted.* Passes non-circularity (no coordinates, no trig
identity, no assumed inner product), non-relabeling (the inner product is
*constructed* by integral geometry and orthogonality is *derived* by reflection
symmetry), and freshness (integral-geometry foundation, absent from Loomis). The
one subtlety — that the reflection acts as a measure-preserving map on the circle
of directions — is handled explicitly in the final write-up. Promoted to
`FINAL_PROOF.md`.
