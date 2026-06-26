# Phase 1 — Catalog of KNOWN Non-Circular Trigonometric Proofs

Mechanisms recorded so collisions can be detected. **Tooling honesty (Phase 0):**
WebSearch works; **WebFetch returns HTTP 403 on every domain tried** (arXiv, ar5iv,
cut-the-knot, Wikipedia, ResearchGate) — so I could **not read any full paper**, only
search snippets. Every mechanism below is reconstructed from snippets; any "not in the
literature" claim is capped to "not found in the snippets I could reach."

Convention: right triangle, right angle at `C`, legs `a` (opp. `A`), `b` (opp. `B`),
hypotenuse `c`; `A+B=90°`. Ratio definitions `sinA=a/c, cosA=b/c, tanA=a/b` come from
similar right triangles (non-circular).

---

## The "two trigonometries" firewall (JJ's framing)
There are two developments of trig: one **on the unit circle** `x²+y²=1` (which *is*
Pythagoras — forbidden as input), and one on **ratios in similar right triangles**
(allowed). Forbidden inputs: `sin²+cos²=1`, the unit-circle definition,
`√(x²+y²)`, the law of cosines, and any identity whose only proof routes through these.
The angle-sum/difference formulas are **allowed** *iff* derived geometrically (area or
projection), not from the unit circle.

---

## K-Zimba — Zimba 2009 (*Forum Geometricorum*)
- **Mechanism:** proves the **subtraction formulas** `cos(α−β)=cosα cosβ+sinα sinβ`,
  `sin(α−β)=sinα cosβ−cosα sinβ` for acute angles **geometrically, without** the
  Pythagorean identity. Then sets `β=α`: `cos(α−α)=cos 0 = 1 = cos²α + sin²α`. With
  `cosα=b/c, sinα=a/c` this is `(a²+b²)/c²=1`, i.e. `a²+b²=c²`.
- **Key lever:** subtraction formula at **equal angles**, special value `cos 0 = 1`.
- **Family:** "angle-sum formula (non-circular) + special value."

## K-Luzia — Luzia 2015 (arXiv:1502.06628, *Other trigonometric proofs…*)
- **Mechanism (per snippet):** proves the **addition formula**
  `cos(α+β)=cosα cosβ−sinα sinβ` geometrically (no Pythagoras), descends to the
  **half-angle/double-angle** formula `cosθ = cos²(θ/2) − sin²(θ/2)`, restricts to acute
  angles, `sin/cos` as ratios. (Explicitly notes that *using* Pythagoras would turn this
  into `cosθ=1−2sin²(θ/2)` — the circular form — which he avoids.)
- **Key lever:** addition formula → **cosine half-angle** formula.
- **Family:** "angle-sum formula (non-circular) + half-angle (cosine)."

## K-JJ — Jackson & Johnson 2024 (*Amer. Math. Monthly* 131(9))
- **Mechanism:** builds a right triangle, **reflects to an isosceles triangle**, fills it
  with infinitely many shrinking similar right triangles ("waffle cone"), sums a
  **geometric series** for a side, and applies the **Law of Sines** (proved via the area
  formula `½ab sinC`, non-circular). Insists on using only the similar-triangle "version"
  of trig, never `sin²+cos²=1`.
- **Section 5 — GENERATING METHOD:** "a new method for finding proofs that yield at
  least five more." Per snippets, it is a **scheme** that, by varying the construction
  angle in the Law-of-Sines + reflected-triangle setup, produces a **whole family** of
  proofs. **Anything in that Law-of-Sines/reflected-construction family is NOT new.**
- **Family:** "Law of Sines + reflected/iterated construction (+ a generating scheme)."

## K-KUS — Kise, Uehara, Shinzato 2025 (arXiv:2506.06304, *Trigonometric Ratios Can
Prove the Pythagorean Theorem*)
- **Three proofs (per snippet):**
  1. **isosceles construction + the tangent double-angle formula** `tan2θ=2tanθ/(1−tan²θ)`;
  2. **isosceles construction + the angle-bisector theorem**;
  3. **"deriving a novel trigonometric relation from the angle-bisector theorem,
     thereby unifying and extending" #1 and #2.**
- **Key levers:** tangent double-angle; **angle-bisector theorem**; half-angle tangents.
- **Family:** "angle-bisector / tangent half-angle (+ isosceles construction)."
- **⚠ Collision hazard for this project:** any proof built on the **angle-bisector
  theorem + half-angle tangents** lands in KUS's territory — and I **cannot read KUS**
  (403) to see exactly what #2/#3 are.

---

## Mechanism map (for the collision gauntlet)

| Proof | non-circular identity | special value / construction | family |
|---|---|---|---|
| Zimba | subtraction formula | `cos0=1`, equal angles | angle-sum + value |
| Luzia | addition → cosine half-angle | acute restriction | angle-sum + half-angle |
| JJ | Law of Sines (area) | reflected isosceles + series; **§5 generator** | Law of Sines family |
| KUS #1 | tangent double-angle | isosceles | bisector/tangent |
| KUS #2 | angle-bisector theorem | isosceles | bisector/tangent |
| KUS #3 | "novel relation from angle-bisector" | unifies #1,#2 | bisector/tangent |

**Occupied territory:** subtraction+`cos0` (Zimba); addition+cosine-half-angle (Luzia);
Law of Sines + reflected construction + a generator (JJ §5); tangent double-angle and
**angle-bisector + half-angle tangents** (KUS). A genuinely new mechanism must avoid all
of these — a narrow gap.

### Sources (search-reachable; full text NOT reachable, 403)
- Zimba 2009 — Forum Geometricorum (via snippets).
- Luzia 2015 — https://arxiv.org/abs/1502.06628 (snippet only).
- Jackson–Johnson 2024 — https://www.tandfonline.com/doi/full/10.1080/00029890.2024.2370240 (snippet only).
- Kise–Uehara–Shinzato 2025 — https://arxiv.org/abs/2506.06304 (snippet only).
- Survey "Five or Ten New Proofs…" — https://www.dorinu.ro/wp-content/uploads/2024/11/Five-or-Ten-New-Proofs-of-the-Pythagorean-Theorem.pdf (snippet only).
