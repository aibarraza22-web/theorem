# Phase 1 — Catalog of Known Proofs of the Pythagorean Theorem

**Statement.** In a right triangle with legs of length `a`, `b` and hypotenuse
`c` (the side opposite the right angle), `a^2 + b^2 = c^2`.

This catalog groups the known proofs into **families** and gives at least one
worked representative per family. The organizing references are:

- **E. S. Loomis, *The Pythagorean Proposition* (1st ed. 1907; 2nd ed. 1927)** —
  367 proofs, sorted into four master classes: **Algebraic** (109), **Geometric**
  (255), **Quaternionic / vector** (4), and **"Dynamic"** (mechanical), plus
  Loomis's (incorrect) assertion that no purely **trigonometric** proof is
  possible.
- **Cut-the-Knot** (A. Bogomolny) — an online collection that as of the mid-2020s
  lists 100+ distinct proofs, including modern ones (Zimba; Jackson–Johnson) that
  postdate Loomis.

A recurring theme, important for Phase 4, is which *foundation* a family rests
on. Most of Loomis's 367 rest on **area** or **proportion (similarity)**; very
few rest on **integral geometry** or **probability**.

---

## Family A — Dissection / rearrangement (equal-area by cut-and-move)

The squared-quantities are read as literal areas of squares; one shows the two
small squares can be cut and rearranged into the big square.

**A1. Chinese *gougu* / Zhao Shuang's "hsuan-thu" (xian-tu) diagram.**
Inside a square of side `c` place four copies of the right triangle (legs `a,b`)
as pinwheel; the central tilted square has side `c`. Two readings:

- Outer square side `(a+b)`, area `(a+b)^2 = 4*(1/2 ab) + c^2`. Expand:
  `a^2 + 2ab + b^2 = 2ab + c^2`, so `a^2 + b^2 = c^2`.
- Equivalent rearrangement of the four triangles inside an `(a+b)`-square leaves
  either one `c^2` square, or two squares `a^2` and `b^2`. Same conclusion.

This is the worked representative of the family. It is the proof attached to the
*Zhoubi Suanjing* commentary.

**A2. Bhaskara's "Behold!" proof (12th c.).** Identical pinwheel dissection of the
`c`-square into four triangles plus a central `(b-a)`-square:
`c^2 = 4*(1/2 ab) + (b-a)^2 = 2ab + b^2 - 2ab + a^2 = a^2 + b^2.` Bhaskara
reputedly wrote only "Behold!" beside the figure.

**A3. The `(a+b)^2` square decomposition (algebra of the same picture).** Purely
algebraic version of A1: a square of side `a+b` is decomposed two ways and the
areas equated, as above. This is the bridge to Family D (algebraic).

---

## Family B — Euclidean area proof (shearing, *Elements* I.47)

**B1. Euclid I.47, the "windmill" / "bride's chair".** On each side of the right
triangle erect a square. Drop the altitude from the right angle `C` to the
hypotenuse and extend it across the hypotenuse-square, splitting it into two
rectangles. Show (by SAS-congruent triangles and the "triangle is half a
parallelogram on the same base and between the same parallels" shear lemma) that
the square on leg `a` equals the rectangle under its half of the hypotenuse, and
likewise for `b`. Summing the two rectangles gives the hypotenuse square:
`a^2 + b^2 = c^2`. This is the canonical synthetic proof; it uses **no theory of
proportion**, only congruence and equal-area-under-shear.

---

## Family C — Similar triangles / altitude-to-hypotenuse (proportion)

**C1. Altitude proof (Euclid VI; "the shortest proof").** Drop the altitude from
the right angle to the hypotenuse, foot `H`, splitting `c` into segments `p`
(adjacent to `a`) and `q` (adjacent to `b`), `p+q=c`. The two sub-triangles are
each similar to the whole (equal angles). Hence `a/c = p/a` and `b/c = q/b`, i.e.
`a^2 = c p`, `b^2 = c q`. Add: `a^2 + b^2 = c(p+q) = c^2`.

**C2. The "Einstein" proof (similarity by scale-invariance of area).** Often
attributed to a teenage Einstein. The area of a right triangle is `f(angle)*h^2`
for a shape-determined constant `f` depending only on the acute angle, where `h`
is the hypotenuse, because all right triangles with a given acute angle are
similar and area scales as the square of any chosen linear measure. The altitude
splits the triangle into two smaller right triangles *similar to the original*
with hypotenuses `a` and `b`. Areas add: `f*c^2 = f*a^2 + f*b^2`, so
`c^2 = a^2 + b^2`. (This is C1 dressed in dimensional-analysis language; the
working content is still similarity.)

---

## Family D — Algebraic proofs

**D1. Garfield's trapezoid (1876).** Place the right triangle and a congruent copy
to form a right trapezoid with parallel sides `a` and `b` and height `a+b`. Its
area computed two ways:
`(1/2)(a+b)(a+b) = 2*(1/2 ab) + (1/2)c^2`. Multiply by 2:
`(a+b)^2 = 2ab + c^2`, giving `a^2 + b^2 = c^2`. Uses only the trapezoid area
formula. (James A. Garfield, then a U.S. Representative; published in the *New
England Journal of Education*.)

**D2. Incircle-radius proof.** For a right triangle the inradius is
`r = (a + b - c)/2` and the area is `r*s` with semiperimeter `s=(a+b+c)/2`, while
also area `= (1/2)ab`. Equating `(1/2)ab = r s = ((a+b-c)/2)((a+b+c)/2)
= ((a+b)^2 - c^2)/4` gives `2ab = (a+b)^2 - c^2 = a^2+2ab+b^2-c^2`, hence
`a^2+b^2=c^2`.

---

## Family E — Trigonometric proofs (must avoid circularity)

The folklore (Loomis) was that trigonometry *cannot* prove the theorem because
the trig identities `sin^2+cos^2=1` already encode it. The modern proofs are
careful to build the needed trig facts *without* that identity.

**E1. Zimba (2009).** Derives the subtraction formulas
`cos(a-b)=cos a cos b + sin a sin b` and `sin(a-b)=sin a cos b - cos a sin b`
from independent geometric/analytic means (not from `sin^2+cos^2=1`), then sets
`a=b` to obtain `cos 0 = 1 = cos^2 a + sin^2 a`, i.e. the Pythagorean identity,
and hence the theorem. **Non-circularity:** the angle-difference formulas are
established without assuming the Pythagorean identity, so deriving it is a genuine
implication, not a tautology.

**E2. Jackson & Johnson (2023 talk; 2024 *American Mathematical Monthly*).** Two
New Orleans high-school students. Using the **Law of Sines** and an infinite
geometric series built from a "waffle-cone" of repeatedly reflected right
triangles, they compute the hypotenuse and recover `a^2+b^2=c^2`. **Non-circularity:**
they restrict to acute right-triangle configurations and develop the Law of Sines
and the limiting sum *without* invoking the Pythagorean identity, so no step
presupposes the result. The paper gives several variants and notes which classical
proofs are genuinely trigonometric vs. disguised area proofs.

---

## Family F — Calculus / differential proofs

**F1. Differentiating the side relation.** Fix one leg `a`; let the other leg `x`
vary, so the hypotenuse `y = y(x)` is a function of `x`. Increasing `x` by `dx`
increases `y` by `dy`; a similar-triangles infinitesimal argument gives
`dy/dx = x/y`, i.e. `y dy = x dx`. Integrate: `y^2/2 = x^2/2 + C`. At `x=0`,
`y=a`, so `C=a^2/2` and `y^2 = x^2 + a^2`. Setting `x=b` gives `c^2=a^2+b^2`.
(The infinitesimal relation `dy/dx=x/y` itself rests on similar triangles, so this
proof's foundation is really Family C; the calculus is bookkeeping.)

---

## Family G — Vector / inner-product proofs

**G1. `||u+v||^2` expansion.** Let the legs be vectors `u`, `v` from the right-angle
vertex with `u . v = 0`. Then
`||u+v||^2 = (u+v).(u+v) = ||u||^2 + 2 u.v + ||v||^2 = ||u||^2 + ||v||^2.`
With `||u||=a`, `||v||=b`, `||u+v||` the third side, this is `a^2+b^2=c^2`.
**Caution (circularity):** this is a *proof* only if the inner product / norm is
defined independently of the coordinate formula `sqrt(x^2+y^2)`; if one simply
*defines* `||x|| = sqrt(x1^2+x2^2)` the statement is the definition unrolled. The
honest version takes `<.,.>` as an abstract positive-definite symmetric bilinear
form and `perp` as `<u,v>=0`; then G1 is a one-line identity but the *geometric*
content (that this norm is the one measured by a ruler) is exactly what must be
argued elsewhere. This subtlety is the seed of Phase 4.

---

## Family H — Complex-number proof

**H1. `|z|^2 = z * conj(z)`.** Identify the plane with `C`. Put the right angle at
`0`, legs `z = a` (real axis) and `w = b i` (imaginary axis). Hypotenuse
`z - w = a - b i`, and `|a - b i|^2 = (a-bi)(a+bi) = a^2 + b^2`. Same circularity
caveat as G1: `|z|^2 = (Re z)^2 + (Im z)^2` is the coordinate norm in disguise.

---

## Family I — Quaternionic / "dynamic" (Loomis's small classes)

**I1. Quaternion / Clifford-algebra version.** In a Clifford algebra with
orthonormal `e1, e2` (`e_i e_j + e_j e_i = 2 delta_ij`), a leg-sum `a e1 + b e2`
squares to `(a e1 + b e2)^2 = a^2 e1^2 + b^2 e2^2 + ab(e1 e2 + e2 e1)
= a^2 + b^2` because the cross terms cancel by anticommutation and `e_i^2=1`. The
defining relation of the algebra *is* the orthonormality, so this is the
inner-product proof inside an algebraic skin.

**I2. "Dynamic"/mechanical proofs.** Loomis records arguments using a balance or
fluid/centroid equilibrium (e.g., a triangle of forces). These are physical
realizations of the area or vector identities; they persuade but do not add a new
mathematical foundation.

---

## Family J — Probabilistic / measure-theoretic (modern, under-represented)

**J1. Variance additivity.** Mean-zero random variables on a probability space
form an inner-product space with `<X,Y> = E[XY] = Cov(X,Y)`. If `X,Y` are
**uncorrelated** (`Cov=0`, e.g. independent), `Var(X+Y)=Var(X)+Var(Y)`. This is
the L^2 Pythagorean theorem; restricting to a 2-dimensional subspace of indicator
combinations recovers the planar statement. **Caveat:** as a *geometric* proof it
collapses to G1 unless one supplies an independent reason the L^2 norm is the
measured length — see Phase 4. (Cut-the-knot lists a probabilistic proof in this
spirit.)

**J2. Integral-geometry / mean-projection (rare).** Average the squared
orthogonal projection of a segment over all directions; the average is
proportional to the squared length, and the hypotenuse projection splits
additively over perpendicular legs. This **integral-geometry foundation is almost
absent from Loomis** and is the basis for the new proof in this project (see
`proof/FINAL_PROOF.md`).

---

## Cross-reference summary

| Family | Foundation | Loomis class | Representative |
|---|---|---|---|
| A Dissection | area (cut & move) | Geometric | gougu / Bhaskara |
| B Euclid I.47 | area (shear) | Geometric | windmill |
| C Similarity | proportion | Geometric/Algebraic | altitude; "Einstein" |
| D Algebraic | area + algebra | Algebraic | Garfield; incircle |
| E Trigonometric | angle-sum / Law of Sines | (Loomis: "impossible") | Zimba; Jackson–Johnson |
| F Calculus | similarity + integration | — | `y dy = x dx` |
| G Vector | inner product | Quaternionic/vector | `||u+v||^2` |
| H Complex | inner product (over C) | — | `|z|^2` |
| I Quaternion/dynamic | algebra / mechanics | Quaternionic/Dynamic | Clifford square |
| J Probabilistic / integral-geom. | second moments / averaging over directions | **absent** | variance; mean projection |

**Takeaway for Phase 4:** Families A–D dominate Loomis (area/proportion). The
*foundations* essentially missing from the 367 are **integral geometry** and
**probability**. That gap is where a genuinely new proof can live.
