# Phase 2 — Candidate Trigonometric Proofs

Each pinned to a specific identity, with an upfront self-check: which non-circular facts
it needs, and which known family it resembles. Right triangle: right angle `C`, legs
`a` (opp `A`), `b` (opp `B`), hyp `c`, `A+B=90°`, ratio defs `sinA=a/c, cosA=b/c,
tanA=a/b`.

---

## P-α — Sine addition formula at complementary angles
**Sketch.** The sine **addition** formula `sin(A+B)=sinA cosB+cosA sinB` is provable by
the area method (split a triangle by a cevian; areas add) — no Pythagoras. With `A+B=90°`,
`sin(A+B)=sin 90°=1` (boundary value of opp/hyp). Substituting ratios:
`(a/c)(a/c)+(b/c)(b/c)=1`, i.e. `(a²+b²)/c²=1`. ∎
**Needs (non-circular):** area-proof of the sine addition formula; `sin90°=1`.
**Family resemblance:** **Zimba** (angle-sum formula + special value) — the *dual* of
Zimba (addition + `sin90°` vs subtraction + `cos0`). Likely a Zimba **VARIANT**.

## P-β — Angle-bisector half-angle tangents (**chosen for Phase 4**)
**Sketch.** Bisect angle `A`; the bisector meets `BC` at `D`. Angle-bisector theorem:
`BD/DC=AB/AC=c/b`, with `BD+DC=a`, so `DC=ab/(b+c)`. In right triangle `ACD` (right angle
`C`), `tan(A/2)=DC/AC=a/(b+c)`. Symmetrically `tan(B/2)=b/(a+c)`. Since `A+B=90°`,
`A/2+B/2=45°`, so by the **tangent addition** formula and `tan45°=1`:
```
1 = tan(A/2+B/2) = (tan(A/2)+tan(B/2))/(1 − tan(A/2)tan(B/2)).
```
Substituting and simplifying gives the clean identity (verified by SymPy)
`tan(A/2+B/2) − 1 = (a²+b²−c²)/(c(a+b+c))`, so `1 = 1 + (a²+b²−c²)/(c(a+b+c))` forces
`a²+b²=c²`. ∎
**Needs (non-circular):** angle-bisector theorem (area/similar-triangle proof); ratio
def of `tan`; tangent addition (from area-proved sin/cos addition); **`tan45°=1`** (ratio
of the two equal legs of an isosceles right triangle — needs only that the legs are
equal, **not** the hypotenuse, so unlike `sin45°` it is non-circular); `A+B=90°`.
**Family resemblance:** **KUS 2025** (angle-bisector + half-angle tangents). ⚠ High
collision risk; but uses **no isosceles construction** and the specific lever
`A/2+B/2=45°`, `tan45°=1`.

## P-γ — Projection formula `c = a cosB + b cosA`
**Sketch.** Drop the altitude from `C` to `AB` at `H`. In right triangles `AHC`, `BHC`:
`AH=b cosA`, `HB=a cosB`; `AH+HB=c`, so `c=b cosA+a cosB`. With `cosA=b/c, cosB=a/c`:
`c=(a²+b²)/c`, so `c²=a²+b²`. ∎
**Needs (non-circular):** altitude construction; ratio def of `cos`; segment addition.
**Family resemblance:** this is the **altitude-to-hypotenuse / similar-triangle proof**
(`AH=b²/c, HB=a²/c` are the geometric-mean relations) in cosine clothing — **core (B)
similarity**, almost certainly catalogued and arguably "not really trigonometric."

## P-δ — Weierstrass half-angle substitution — **KILLED (circular)**
**Sketch.** With `t=tan(A/2)`, `sinA=2t/(1+t²)`, `cosA=(1−t²)/(1+t²)`; then
`sin²A+cos²A=1` falls out, giving `(a²+b²)/c²=1`.
**Why it dies:** the factor `1/(1+t²)` comes from `cos²(A/2)=1/(1+tan²(A/2))`, whose only
derivation is `cos²+sin²=1` of the half-angle — the **forbidden** identity. The "1" is
smuggled in. **CIRCULAR.** (Recorded as an instructive death.)

## P-ε — Law of tangents — **KILLED (vacuous)**
**Sketch.** `(a−b)/(a+b)=tan((A−B)/2)/tan((A+B)/2)`; for the right triangle
`(A+B)/2=45°`, `tan45°=1`.
**Why it dies:** substituting the ratio defs makes both sides equal **identically** (a
tautology) — it yields no constraint on `c`. **VACUOUS** (gives nothing). Recorded.

---

## Self-assessment / which survive
- **Survive (non-circular):** P-α (Zimba-variant), **P-β (chosen; KUS-family)**, P-γ
  (similar-triangle proof in cosine form).
- **Die:** P-δ (circular — hidden `sin²+cos²=1`), P-ε (vacuous).

**Chosen for Phase 3–4: P-β.** It is the most self-contained and elegant, has the
cleanest circularity audit (notably the `tan45°` vs `sin45°` distinction), and reduces to
the strikingly clean identity `tan(A/2+B/2)−1=(a²+b²−c²)/(c(a+b+c))`. Its honest weakness
— shared mechanism with KUS 2025 — is confronted head-on in `audits.md`.
