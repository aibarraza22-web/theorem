# Running Log — An Original Proof of the Pythagorean Theorem

This log records decisions, dead ends, and reasoning in chronological order.
Negative results are recorded deliberately: they explain *why* the final proof
took the shape it did.

---

## Entry 0 — Framing the problem (start)

The deliverable is a **new** proof, not a re-skin of an existing one. The central
difficulty, recognized up front, is **circularity**. The Pythagorean theorem is,
at bottom, the statement that the Euclidean metric is the rotation-invariant
quadratic form on the plane. An enormous number of tools one might reach for
(the coordinate distance formula `sqrt(x^2+y^2)`, the inner product
`u1 v1 + u2 v2`, the identity `sin^2 + cos^2 = 1`, the law of cosines) *already
encode* the theorem. Any proof that silently uses one of them proves nothing.

**Design rule adopted:** length/distance must enter the proof through a
definition or set of axioms that is provably *independent* of the coordinate
distance formula, and every nontrivial fact used must pass a circularity audit.

## Entry 1 — Survey first (Phases 1–3)

Wrote `research/01_proof_catalog.md`, `02_history.md`, `03_math_fields.md`.
Cross-referenced Loomis (1927, *The Pythagorean Proposition*, 2nd ed., 367
proofs) and the cut-the-knot collection. Loomis groups everything into four
master classes: **Algebraic** (proofs based on linear/quadratic relations of
the sides), **Geometric** (based on comparison of areas), **Quaternionic**
(vector/dynamic), and what he calls the impossibility of a purely
**trigonometric** proof — a claim now known to be wrong (Zimba 2009; Jackson &
Johnson 2024).

Key observation that shaped Phase 4: among 367+ proofs, the *foundations* that
are barely touched are **integral geometry** (averaging over the group of
directions) and **probability** (second-moment/variance identities). Loomis has
essentially nothing from either. These became the novelty targets.

## Entry 2 — Dead end: the naive "variance additivity" proof

First candidate: random variables with mean zero form an inner-product space
with `<X,Y> = E[XY]`; uncorrelated => orthogonal => `Var(X+Y)=Var(X)+Var(Y)`.
This is real, but on inspection it is **literally the inner-product proof
relabeled**: to connect it to a *geometric* right triangle you must identify the
plane with `R^2` and the norm with `sqrt(x^2+y^2)`, which assumes the theorem.
As a stand-alone geometric proof it is circular or trivial. Rejected as the
final proof, but kept in the catalog as the probabilistic family. (See
`04_novelty_targets.md`.)

## Entry 3 — Dead end: Gaussian isotropy (Herschel–Maxwell)

Second candidate: `exp(-(x^2+y^2)/2) = exp(-x^2/2) exp(-y^2/2)` is the unique
isotropic product density, so `x^2+y^2` is the natural squared radius. **Circular**:
isotropy of `exp(-(x^2+y^2)/2)` *is* the rotation-invariance of `x^2+y^2`, i.e.
Pythagoras. Rejected.

## Entry 4 — Dead end: mean-square projection via `integral of cos^2`

Third candidate (integral geometry): the average squared projection of a segment
over all directions is proportional to its squared length, then expand the
hypotenuse projection. The first version computed
`integral_0^{2pi} cos^2 = pi` and the cross term via the double-angle identity
`cos 2t = 2cos^2 t - 1`. **That identity uses `sin^2+cos^2=1`** — the analytic
twin of Pythagoras — so the route smelled circular. Flagged for repair.

## Entry 5 — Breakthrough: replace all trig identities by *symmetry*

Repaired the integral-geometry proof by removing trigonometry entirely:

1. **Proportionality `Q(u) = c0 * L(u)^2`** where `Q(u) = integral p_theta(u)^2 d_theta`
   follows from *rotation-invariance + quadratic homogeneity of the projection
   map* — no `integral cos^2` needed, no value of the constant needed.
2. **Orthogonality `B(u,v)=0` for perpendicular `u,v`** follows from
   *invariance of the bilinear form under the reflection that fixes `u` and
   sends `v` to `-v`* — no `cos(pi/2)=0`, no trig at all.

This eliminated every Pythagorean-looking analytic identity. The only inputs are
linearity of orthogonal projection, invariance of an integral over the circle
under rotations/reflections, and the Euclidean congruence axioms that make
"rotation", "reflection", and "right angle" available. **This became the final
proof.** See `proof/FINAL_PROOF.md`.

## Entry 6 — Verification (Phase 6)

- `verify/symbolic_check.py` (SymPy): confirms the projection-integral pairing
  `B(u,v) = integral_0^{2pi}(u . e_theta)(v . e_theta) d_theta = pi (u . v)`, hence
  `Q(u)=pi |u|^2`, and that `B` vanishes exactly when `u . v = 0`. This validates
  that the abstractly-constructed pairing really is (a positive multiple of) the
  Euclidean inner product.
- `verify/monte_carlo.py`: (a) random right triangles satisfy `a^2+b^2=c^2` to
  ~1e-12; (b) Monte-Carlo estimate of `B(u,v)` by sampling directions matches
  `pi (u.v)` and is ~0 for perpendicular vectors.
- `verify/lean/Pythagoras.lean`: formalizes the **abstract core step**
  (`<u,v>=0 => ||u+v||^2 = ||u||^2 + ||v||^2`) in Lean 4 / mathlib. Honest
  scope note: the integral-geometric *construction* of the inner product is not
  formalized; only the orthogonality => sum-of-squares implication is.

## Entry 7 — Skeptical referee pass (Phase 7)

See the dedicated "Referee report" section at the bottom of this log. Five
objections raised and addressed; two led to clarifications in `FINAL_PROOF.md`
(the measure-preservation of the reflection on the circle, and the explicit
statement that `p_theta` is *signed*). Proof survived.

---

## Referee report (Phase 7) — attacking my own proof

**Objection R1 (hidden circularity in `p_theta`).** Does defining the signed
projection `p_theta(u) = ` component of `u` along direction `theta` secretly use the
coordinate inner product? *Response:* No. `p_theta(u)` is defined as the signed
length of the orthogonal foot of `u` on the line of direction `theta`, where
"orthogonal" is the right-angle congruence relation of Euclidean geometry and
"signed length" is the ruler/betweenness order on that line. No coordinates, no
`sqrt(x^2+y^2)`. The coordinate expression `u . e_theta` appears only in the
SymPy *sanity check*, never in the proof.

**Objection R2 (the constant `c0` could be 0 or direction-dependent).**
*Response:* `c0 = Q(e)` for a unit vector `e`; `Q(e) = integral p_theta(e)^2 d_theta`
is an integral of a nonnegative continuous function that is not identically zero
(`p_0(e)` for `theta` aligned with `e` equals `L(e)=1`), so `c0>0`. Rotation
invariance (Lemma 2) makes `Q` constant on vectors of equal length, so `c0` is a
single universal positive number, not direction-dependent.

**Objection R3 (does `Q(lambda u)=lambda^2 Q(u)` need similarity theory,
which needs Pythagoras?).** *Response:* It needs only that a homothety with
ratio `lambda>0` scales every length by `lambda` and that projection is linear
(`p_theta(lambda u)=lambda p_theta(u)`). Scaling of length under homothety is a
similarity axiom, independent of Pythagoras (Euclid's theory of proportion /
Hilbert's similarity axioms do not assume I.47).

**Objection R4 (the reflection step assumes the plane is 2-dimensional / that a
reflection fixing `u` sends `v` to `-v`).** *Response:* In the plane, the
reflection across the line spanned by `u` fixes `u` and negates every vector
orthogonal to that line; since `v perp u`, `v` lies in that orthogonal direction,
so `sigma(v) = -v`. This is a property of plane reflections (a congruence /
isometry), not of the metric formula. Stated explicitly in the proof.

**Objection R5 (measure on directions).** *Response:* The integral is over the
circle of directions with its rotation-invariant (arc-length) measure `d_theta`.
Rotations act as rotations of the circle (measure-preserving) and the line
reflection acts as a reflection of the circle `theta -> 2*beta - theta`
(measure-preserving). Both are bijections preserving `d_theta`, so the change of
variables in Lemmas 2 and 3 is valid. Added a sentence making this explicit.

**Verdict:** No surviving circularity or gap. The proof is sound. Its honest
novelty is a *fresh foundation* (integral geometry over the rotation group +
pure symmetry), not a new rearrangement of an old figure. See the Novelty Claim
in `FINAL_PROOF.md`.
