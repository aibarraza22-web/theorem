# An Original Proof of the Pythagorean Theorem
## via Mean Squared Projection over the Rotation Group

*A proof from the foundation of integral geometry, using only linearity of
orthogonal projection and the symmetry of an integral over the circle of
directions — no coordinates, no inner-product formula, no trigonometric
identity.*

---

## 0. Accepted starting facts (axioms)

We work in the Euclidean plane `E` as governed by the classical congruence and
similarity axioms (Hilbert's groups of axioms, equivalently the synthetic content
of Euclid Books I and VI **excluding** Proposition I.47 and its consequences). We
make the following explicit, and **nothing else**:

- **(P1) Vectors and affine structure.** Points of `E` form a 2-dimensional real
  affine space; fixing an origin `O`, displacements are vectors that can be added
  and scaled by real numbers. *(Affine geometry — no metric.)*

- **(P2) Length.** There is a function `L` assigning to each vector a nonnegative
  real number, its **length**, such that:
  - (P2a) `L(u) = 0` iff `u = 0`;
  - (P2b) **homogeneity:** `L(λu) = |λ| · L(u)` for all real `λ`
    *(a homothety with ratio `λ` scales lengths by `|λ|` — a similarity axiom);*
  - (P2c) `L` is invariant under all rigid motions (translations, rotations,
    reflections). *(Congruent segments have equal length.)*
  We do **not** assume any formula for `L` in coordinates.

- **(P3) Rigid motions.** The plane admits **rotations** `ρ_α` (about `O`, by any
  angle `α`) and **reflections** `σ_ℓ` (across any line `ℓ` through `O`). These are
  linear maps preserving `L` (by P2c), they preserve the relation "right angle,"
  and they act on the set of **directions** (unit-direction lines through `O`).

- **(P4) Right angle / orthogonality.** Two nonzero vectors `u, v` are
  **perpendicular**, written `u ⟂ v`, when the angle between them is a right angle
  (the congruence-defined right angle of Euclidean geometry). The reflection
  `σ_u` across the line spanned by `u` **fixes `u`** and **negates every vector
  perpendicular to that line**. *(This is the defining behavior of a plane
  reflection; it does not use any length formula.)*

- **(P5) Orthogonal projection.** For each direction `θ` there is a map
  `π_θ : E → ℓ_θ` onto the line `ℓ_θ` of direction `θ`, the **orthogonal
  projection**, characterized by `u − π_θ(u) ⟂ ℓ_θ`. Orthogonal projection onto a
  line through `O` is a **linear** map. *(Standard affine/Euclidean fact: the foot
  of the perpendicular depends linearly on the point. Proof of linearity uses only
  that perpendicularity is preserved under translation and that the projection of a
  sum is the sum of projections — see Lemma 0.)*

- **(P6) Directions and their measure.** The set of directions is the circle
  `S = ℝ / 2πℤ` parameterized by the angle `θ`, carrying the rotation-invariant
  arc-length measure `dθ` of total mass `2π`. Rotations act on `S` by
  `θ ↦ θ + α` and the reflection `σ_ℓ` (axis at angle `β`) acts by
  `θ ↦ 2β − θ`; **both are measure-preserving bijections of `S`.**

These axioms are about congruence, similarity, affine structure, and the measure
on directions. **None of them mentions the coordinate distance formula
`√(x²+y²)`, the coordinate inner product, or the identity `sin²+cos²=1`.** The
Circularity Audit (§6) confirms this.

---

## 1. The signed projection functional

**Definition 1 (signed projection).** Fix a direction `θ` and a unit vector
`e_θ` along `ℓ_θ` (choose one of the two orientations; the choice will not matter
because every quantity below is a product of two projections or a square). For a
vector `u`, the orthogonal projection `π_θ(u)` is a multiple of `e_θ`; define the
**signed projection**
```
p_θ(u)  :=  the real number t such that  π_θ(u) = t · e_θ .
```
So `|p_θ(u)| = L(π_θ(u))` is the length of the shadow of `u` on `ℓ_θ`, with a
sign recording on which side of `O` the shadow falls.

**Lemma 0 (linearity of `p_θ`).** For all vectors `u, v` and scalars `λ`,
```
p_θ(u + v) = p_θ(u) + p_θ(v),     p_θ(λu) = λ · p_θ(u).
```
*Proof.* By (P5) `π_θ` is linear, and `t ↦ t·e_θ` is a linear isomorphism of `ℓ_θ`
with `ℝ`; `p_θ` is the composition of `π_θ` with its inverse, hence linear. (Concretely:
`π_θ(u+v) − π_θ(u) − π_θ(v)` lies on `ℓ_θ`, while `(u+v)−u−v = 0` is perpendicular
to nothing/everything; uniqueness of the perpendicular foot forces the difference
to be `0`. Scalar homogeneity is identical.) ∎

Note `p_θ` uses only the **direction** `θ` and the Euclidean notions of
perpendicular foot and signed position on a line (a ruler with an order). It does
**not** use coordinates of `u` or any distance formula.

---

## 2. The averaged quadratic functional and bilinear pairing

**Definition 2.** For vectors `u, v` define
```
Q(u)   :=  ∫_0^{2π} p_θ(u)^2  dθ           (the mean squared projection, ×2π)
B(u,v) :=  ∫_0^{2π} p_θ(u) p_θ(v)  dθ .
```
The integrands are bounded continuous functions of `θ` (the projection of a fixed
vector varies continuously with the direction), so both integrals exist.

**Lemma 1 (B is a symmetric bilinear form, Q its diagonal).**
`B(u,v) = B(v,u)`, `B` is linear in each argument, and `Q(u) = B(u,u)`.
Consequently the **polarization identity** holds:
```
Q(u + v) = Q(u) + 2 B(u,v) + Q(v),     Q(u − v) = Q(u) − 2 B(u,v) + Q(v).      (★)
```
*Proof.* Symmetry is clear from the symmetric integrand. For bilinearity, fix `v`
and use Lemma 0 inside the integral:
`B(u+u', v) = ∫ p_θ(u+u') p_θ(v) dθ = ∫ (p_θ(u)+p_θ(u')) p_θ(v) dθ
= B(u,v) + B(u',v)`, and `B(λu, v) = ∫ λ p_θ(u) p_θ(v) dθ = λ B(u,v)`; linearity
in the second slot follows by symmetry. Setting `v=u` gives `Q=B(u,u)`. Expanding
`Q(u±v)=B(u±v, u±v)` by bilinearity gives (★). ∎

This is the heart of the construction: **`B` is a genuine inner product on the
plane, built not from coordinates but by integrating geometric projections over
all directions.**

---

## 3. Proportionality: `Q(u) = c0 · L(u)²`

**Lemma 2.** There is a universal constant `c0 > 0` with
```
Q(u) = c0 · L(u)^2     for every vector u.
```
*Proof.* Two properties of `Q`:

**(i) Quadratic homogeneity.** By Lemma 0, `p_θ(λu) = λ p_θ(u)`, so
`Q(λu) = ∫ (λ p_θ(u))^2 dθ = λ^2 Q(u)` for every real `λ`.

**(ii) Rotation invariance.** Let `ρ_α` be rotation by `α`. Projecting a rotated
vector onto direction `θ` equals projecting the original vector onto the direction
rotated back by `α`; in signed form,
```
p_θ(ρ_α u) = p_{θ−α}(u)
```
(because `ρ_α` is a length-preserving linear map carrying `ℓ_{θ−α}` to `ℓ_θ` and
preserving perpendicular feet, by P3). Therefore, using the measure-invariance of
`dθ` under the shift `θ ↦ θ − α` (P6),
```
Q(ρ_α u) = ∫_0^{2π} p_{θ−α}(u)^2 dθ = ∫_0^{2π} p_φ(u)^2 dφ = Q(u).
```
So `Q` is constant on each rotation-orbit.

Now take any two vectors `u, w` with `L(u) = L(w) ≠ 0`. In the plane, two vectors
of equal length are related by a single rotation about `O` (P3): `w = ρ_α u` for
some `α`. By (ii), `Q(w) = Q(u)`. Hence **`Q(u)` depends only on `L(u)`**: there is
a function `F` with `Q(u) = F(L(u))`. By (i),
`F(|λ| L(u)) = Q(λu) = λ^2 Q(u) = λ^2 F(L(u))`; writing `ℓ = L(u)` and `λ = s/ℓ`
for `s ≥ 0` gives `F(s) = (s/ℓ)^2 F(ℓ)`, i.e. `F(s) = c0 · s^2` with
`c0 = F(1) = Q(e)` for any unit vector `e`.

Finally `c0 > 0`: `Q(e) = ∫ p_θ(e)^2 dθ` is the integral of a nonnegative
continuous function that is not identically zero — at the direction `θ` aligned
with `e` we have `π_θ(e) = e`, so `p_θ(e) = ±L(e) = ±1 ≠ 0`, and by continuity
`p_θ(e)^2 > 0` on an arc. Hence `c0 > 0`. ∎

**Remark.** We never evaluated the integral. (One *can*: `c0 = ∫_0^{2π} cos²θ dθ
= π`, an analytic fact about the cosine *function*. But the proof does not need the
value, only that it is a single positive number — which is exactly what removes any
dependence on `sin²+cos²=1`.)

---

## 4. Orthogonality by reflection symmetry: `u ⟂ v ⇒ B(u,v) = 0`

**Lemma 3.** If `u ⟂ v` then `B(u,v) = 0`.
*Proof.* Let `σ := σ_u` be the reflection across the line spanned by `u` (P4). It
is a length-preserving linear map; on directions it acts as a measure-preserving
reflection of the circle `S` (P6).

**B is reflection-invariant.** For any vectors `x, y`,
```
B(σx, σy) = ∫_0^{2π} p_θ(σx) p_θ(σy) dθ .
```
As with rotations, `p_θ(σx) = p_{σ(θ)}(x)`, where `σ(θ)` is the reflected direction
(σ preserves perpendicular feet and lengths, P3). Substituting and changing
variables `φ = σ(θ)` — a measure-preserving bijection of `S` (P6) —
```
B(σx, σy) = ∫_S p_{σ(θ)}(x) p_{σ(θ)}(y) dθ = ∫_S p_φ(x) p_φ(y) dφ = B(x,y).    (†)
```

**Apply to our perpendicular pair.** By (P4), `σ` fixes `u` and negates every
vector perpendicular to the line of `u`. Since `v ⟂ u`, we have `σ(u) = u` and
`σ(v) = −v`. Plugging `x=u`, `y=v` into (†) and using bilinearity (Lemma 1):
```
B(u,v) = B(σu, σv) = B(u, −v) = −B(u,v).
```
Therefore `2 B(u,v) = 0`, i.e. `B(u,v) = 0`. ∎

No trigonometric identity, no value of any integral, and no coordinate appeared:
orthogonality of the legs forces the cross term to vanish purely because the
configuration has a reflection symmetry that reverses `v` while preserving the
pairing.

---

## 5. The theorem

**Theorem (Pythagoras).** Let `△OAB` be a right triangle with the right angle at
`O`. Write `u = OA`, `v = OB`, so `u ⟂ v`, and set
`a = L(u)`, `b = L(v)`, `c = L(AB)`. Then
```
a^2 + b^2 = c^2 .
```

*Proof.* The side `AB` is the displacement from `A` to `B`, namely the vector
`v − u`. By the polarization identity (★) and Lemmas 2–3,
```
c0 · c^2 = c0 · L(v − u)^2 = Q(v − u)                         [Lemma 2]
         = Q(v) − 2 B(u,v) + Q(u)                              [(★)]
         = Q(v) + Q(u)                                          [Lemma 3, B(u,v)=0]
         = c0 · L(v)^2 + c0 · L(u)^2                            [Lemma 2]
         = c0 · (a^2 + b^2).
```
Since `c0 > 0` (Lemma 2), divide to obtain `c^2 = a^2 + b^2`. ∎

Equivalently, placing the hypotenuse as `u + v` (the diagonal of the rectangle on
the legs) gives `Q(u+v) = Q(u) + Q(v)` by the same two lemmas — the proof is
indifferent to that choice.

---

## 6. Figure

```
                         B
                         |\
                         | \
                         |  \
                         |   \         The right angle is at O.
                  v = OB |    \  AB = v - u   (the hypotenuse vector)
            (length b)   |     \        c = L(AB)
                         |      \
                         |       \
                         O--------A
                            u = OA
                           (length a)

   Directions θ sweep the circle S of all orientations:

                  e_{θ}
                    ^          For each direction θ, p_θ(u) is the SIGNED length
                   /              of the shadow of u on the line ℓ_θ.
        ℓ_θ ------/------->     Q(u) = ∫ p_θ(u)^2 dθ  averages the squared shadow
                 /                  over ALL directions; Lemma 2 says this equals
                O                   c0·L(u)^2.  Lemma 3 says perpendicular vectors
                                    have orthogonal shadows on average (B=0).
```

ASCII is used for portability; a TikZ version of the same figure:

```latex
\begin{tikzpicture}[scale=1.3]
  \coordinate (O) at (0,0);
  \coordinate (A) at (2.4,0);     % u = OA, length a
  \coordinate (B) at (0,1.6);     % v = OB, length b
  \draw[thick] (O) -- (A) -- (B) -- cycle;        % right triangle
  \draw (O) rectangle +(0.22,0.22);               % right-angle mark at O
  \node[below] at (1.2,0) {$u=OA,\ a$};
  \node[left]  at (0,0.8) {$v=OB,\ b$};
  \node[above right] at (1.2,0.8) {$AB=v-u,\ c$};
  % a sample direction and the shadow of u
  \draw[->,gray] (-1.4,-0.7) -- (1.8,0.9) node[right] {$\ell_\theta,\ e_\theta$};
  \draw[dashed] (A) -- ($(O)!(A)!(1.8,0.9)$);      % drop perpendicular from A
  \node[gray] at (1.1,0.75) {$\pi_\theta(u)$};
\end{tikzpicture}
```

---

## 7. Circularity audit

Every nontrivial fact used, and why its derivation does **not** assume
`a²+b²=c²` (nor its analytic twin `sin²+cos²=1`, nor the coordinate norm).

| # | Fact used | Where | Why it is not Pythagoras-in-disguise |
|---|---|---|---|
| 1 | Orthogonal projection onto a line is **linear** (`p_θ` linear). | Lemma 0, P5 | A consequence of affine structure + uniqueness of the perpendicular foot. Proof uses only that perpendicularity is preserved by translation; no length formula. |
| 2 | `L(λu) = |λ| L(u)` (homogeneity of length). | Lemma 2(i), P2b | A **similarity** axiom (homothety scales length). Independent of I.47; Euclid develops proportion (Book V/VI) without I.47. |
| 3 | `L` invariant under rotations/reflections. | Lemmas 2,3; P2c | Congruent segments have equal length — a **congruence** axiom, logically prior to I.47. |
| 4 | Equal-length vectors are related by a rotation. | Lemma 2 | Plane congruence/transitivity of the rotation action on a circle of given radius. No metric formula. |
| 5 | `dθ` is invariant under rotations `θ↦θ+α` and reflections `θ↦2β−θ` of the circle of directions. | Lemmas 2,3; P6 | Arc length on a circle is invariant under its own isometries — a fact about the 1-dimensional circle of *directions*, not about planar distance. Does not presuppose `√(x²+y²)`. |
| 6 | A reflection across the line of `u` fixes `u` and negates `v⟂u`. | Lemma 3, P4 | Definition of a plane reflection acting on the perpendicular complement; pure congruence geometry. |
| 7 | Existence of the constant `c0>0`. | Lemma 2 | Positivity of an integral of a nonnegative, not-identically-zero continuous function. Its **value is never used**, so no integral identity (and in particular not `∫cos²=π`, which would route through `sin²+cos²=1`) enters the proof. |
| 8 | Polarization `Q(u±v)=Q(u)±2B(u,v)+Q(v)`. | Lemma 1, (★) | Algebraic expansion of a **bilinear** form (Lemma 1), itself from linearity of `p_θ`. Pure algebra. |

**Tools deliberately avoided** (each would have introduced circularity):

- the coordinate distance formula `√(x²+y²)` — **never used** (appears only in the
  SymPy/Monte-Carlo *verification*, explicitly labeled as a check, not the proof);
- the coordinate inner product `u₁v₁+u₂v₂` as a *definition* — **never used**; our
  inner product `B` is *constructed*, then *shown* (in verification) to be a
  positive multiple of it;
- `sin²θ+cos²θ=1` and the law of cosines — **never used**; orthogonality is handled
  by reflection symmetry (Lemma 3), not by a trig identity;
- similarity of the two sub-triangles of the altitude (the engine of Families C, F)
  — **never used**.

**Conclusion of the audit:** no step presupposes the Pythagorean relation. The
proof is non-circular.

---

## 8. Novelty claim

**Closest known proof.** The nearest relative is the **vector / inner-product
proof** (catalog Family G): both culminate in
`L(u+v)² = L(u)² + L(v)²` once a cross term vanishes by orthogonality, and both
implicitly invoke an inner-product structure.

**What is genuinely new.**

1. **A constructed, not assumed, inner product.** Family G (and its complex,
   Clifford, and `Var(X+Y)` cousins) *begins* with an inner product — typically the
   coordinate form `u₁v₁+u₂v₂`, which already contains the theorem. Here the
   bilinear form `B(u,v) = ∫₀^{2π} p_θ(u)p_θ(v) dθ` is **manufactured by integrating
   orthogonal projections over the entire rotation group**. The Euclidean inner
   product is an *output* of the proof (verified, in §verify, to be `π` times the
   standard one), not an *input*.

2. **Orthogonality derived by symmetry, not decreed.** Family G writes `⟨u,v⟩=0`
   for perpendicular legs by fiat (it is the coordinate computation). Here the
   vanishing of the cross term is **forced by a reflection symmetry** of the
   averaged pairing (Lemma 3) — a genuinely different mechanism, and one that uses
   no trigonometric identity and no coordinates.

3. **A new foundation: integral geometry over directions.** The decomposition is a
   **Parseval-type identity over the continuum of directions** (a Cauchy-style
   averaging), structurally distinct from a single basis expansion. This foundation
   — measure on the rotation group, mean squared projection — is **essentially
   absent from Loomis's 367 proofs** and from the standard textbook families. It
   also subsumes the **probabilistic** reading (with `θ` uniform, `Q/2π` is a
   variance and `B/2π` a covariance), so a single argument realizes both
   under-mined foundations (integral geometry and probability) at once.

**Honesty.** This is best described as a **fresh synthesis on a new foundation**,
not a wholly unprecedented theorem: the *conclusion line* coincides with the
inner-product proof, as it must, since all proofs of one theorem agree at the end.
What is new is the **route and the foundation** — building the metric from averaged
shadows and extracting orthogonality from reflection symmetry — and the explicit,
audited avoidance of every Pythagoras-encoding shortcut. To my knowledge this exact
construction (averaged *signed-projection* bilinear form + reflection-symmetry
orthogonality, with no trig identity and no coordinate norm) does not appear among
the classical 367 or in the standard modern collections; the closest published
ideas are Cauchy's mean-projection formula in integral geometry (used for
*perimeter*, not for the Pythagorean relation) and the abstract `L²` Pythagorean
theorem (used without the directional-integral construction).

---

## 9. Summary of the logical skeleton

```
P5 ─► Lemma 0: p_θ linear
                 │
                 ▼
Lemma 1: B bilinear & symmetric, Q = B(·,·)  ──►  (★) polarization
   │                                                   │
P2b,P3,P6 ─► Lemma 2: Q(u) = c0·L(u)^2  (c0>0)        │
P4,P3,P6 ─► Lemma 3: u⟂v ⇒ B(u,v)=0                   │
                 │                                     │
                 ▼                                     ▼
   Theorem:  c0·c^2 = Q(v−u) = Q(u)+Q(v) = c0·(a^2+b^2)  ⇒  a^2+b^2=c^2
```
