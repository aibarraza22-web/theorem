# Phase 6 — Novelty Ledger + Skeptical Referee

Featured proof: **P-β**, the angle-bisector half-angle tangent proof.
Verdict: **VARIANT — very likely DUPLICATE of KUS 2025. Not addable.**

## 1. Novelty ledger

| Idea in P-β | Closest known proof | Exact delta |
|---|---|---|
| `tan(A/2)=a/(b+c)` from the angle-bisector theorem | **KUS 2025** proofs #2/#3 (angle-bisector theorem; half-angle tangents). Snippets associate `tan=a/(b+c)` with arXiv:2506.06304. | **None evident.** Same relation, same tool. |
| `A/2+B/2=45°`, `tan45°=1`, tangent addition | KUS snippet: "when the sum of half-angles equals 45°, `tan45°=1` can be applied." | **None evident** — appears to be in KUS too. |
| No isosceles construction (bisect both acute angles of the right triangle) | KUS #2 uses an isosceles construction; KUS #3 "unifies/extends" via "a novel relation from the angle-bisector theorem." | **Possibly a thin construction difference vs #2**, but **likely subsumed by #3**. |
| Clean identity `tan(A/2+B/2)−1=(a²+b²−c²)/(c(a+b+c))` | not separately attested, but it is just the algebra of the above | presentational, not a new mechanism |

**Net:** no defensible mechanistic delta against KUS 2025.

## 2. Skeptical referee

**Referee critique (i): "this is secretly circular."**
*Answer:* No. Every fact traces to a non-Pythagorean source (audit, `FINAL_PROOF.md` §4):
the angle-bisector theorem via equal-altitude area ratios; `tan` via similar triangles;
the tangent addition formula via the area/projection addition formulas; and — the
delicate point — `tan45°=1` via **leg/leg** in a 45–45–90 triangle, which needs only that
the two legs are equal, **never** the hypotenuse (so it does not smuggle in `sin45°=1/√2`,
i.e. Pythagoras). The candidate **survives** the circularity attack.

**Referee critique (ii): "this is just KUS 2025 (proof #2/#3) / their generated family."**
*Answer (honest, and the referee wins):* The mechanism — angle-bisector theorem →
`tan(half-angle)=side/(sum of other two)` → `tan45°` with complementary half-angles — is
**exactly** KUS's angle-bisector / half-angle-tangent territory. Their abstract lists two
angle-bisector proofs and a "novel relation from the angle-bisector theorem" unifying
them; the targeted searches return `tan=a/(b+c)`, angle bisector, and `tan45°`-with-summed-
half-angles in association with arXiv:2506.06304. My only candidate distinction (no
isosceles construction) is thin and most likely covered by their unifying proof #3. **I
cannot rebut this critique.** Per the project rule, I therefore **downgrade** from any
"addable" hope to **VARIANT / likely DUPLICATE**.

**Critique (iii): "P-α or P-γ would have been newer."**
*Answer:* No. P-α (`sin(A+B)=sin90°=1`) is a one-line corollary of the non-circular
addition formula already used by Zimba/Luzia — not new. P-γ (`c=a cosB+b cosA`) is the
classical similar-triangle proof in cosine notation — known (core B). Neither is a better
novelty bet than P-β; all three live inside already-published families.

## 3. Why this remains a useful (negative) deliverable

The circularity gauntlet has independent value: it produces a **clean, rigorous,
non-circular trig proof** and an audit that pinpoints *where* circularity normally
hides (special-angle values: `tan45°=1` is safe; `sin45°`, `cos45°`, and `1/(1+t²)`
half-angle factors are not — that is what killed candidate P-δ). The collision gauntlet
then honestly places the proof in the literature: the trig frontier (Zimba 2009 → Luzia
2015 → JJ 2024 → KUS 2025) has mined the easy non-circular mechanisms, and P-β lands on
KUS's 2025 angle-bisector route.

**Confidence:** "non-circular" — HIGH (audit is explicit). "Not genuinely new / likely
KUS duplicate" — MODERATE-HIGH, capped only by the inability to read the 2025 paper
(WebFetch 403). Neither residual doubt points toward novelty.
