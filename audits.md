# Phase 3 — Circularity Gauntlet + Collision Gauntlet

For each surviving candidate (P-α, P-β, P-γ): (a) trace every trig fact to a
non-Pythagorean derivation; (b) search for prior art. Verdicts: CIRCULAR / KNOWN /
VARIANT / NO-COLLISION-FOUND. **Tooling caveat:** WebFetch is 403 on all domains, so
full papers are unreadable; collision evidence is **search snippets only**, and snippet
*prose* may paraphrase my query (I rely on it cautiously, weighting the actual paper
links and abstracts).

---

## (a) Circularity audit of the chosen proof P-β

| Fact | Non-circular derivation | Uses `sin²+cos²=1`? |
|---|---|---|
| Angle-bisector theorem `BD/DC=AB/AC` | Areas of the two sub-triangles share the same apex altitude; ratio of areas = ratio of bases = ratio of the adjacent sides (or the Law of Sines via `½ab sinC`). No Pythagoras. | No |
| Ratio def `tan(A/2)=DC/CA` in △ACD | Definition of tangent (opp/adj) in the right sub-triangle `ACD` (right angle at `C`). | No |
| `tan(A/2)=a/(b+c)` | Combine the two above: `DC=ab/(b+c)`, `CA=b`. Pure algebra. | No |
| `A/2+B/2=45°` | `A+B=90°` because a triangle's angles sum to `180°` and `C=90°`. | No |
| **`tan45°=1`** | In a 45–45–90 isosceles right triangle the two **legs are equal**, so `tan45°=opp/adj=leg/leg=1`. **Only equality of the legs is used — not the hypotenuse length.** Contrast `sin45°=leg/hyp`, which needs `hyp=leg·√2` (Pythagoras) and would be **circular**. | No |
| Tangent addition `tan(x+y)=(tanx+tany)/(1−tanx tany)` | From the **area/projection** proofs of the sine and cosine addition formulas, then `tan=sin/cos`; the quotient cancels with **no** appeal to `sin²+cos²=1`. | No |
| Final algebra → `a²+b²=c²` | Rational identity `tan(A/2+B/2)−1=(a²+b²−c²)/(c(a+b+c))` (SymPy-verified). | No |

**Circularity verdict: NON-CIRCULAR.** No step uses `sin²+cos²=1`, the unit circle,
`√(x²+y²)`, or the law of cosines. The one delicate point — needing a value at `45°` — is
handled by `tan45°=1`, which is non-circular precisely because tangent is a ratio of the
two *legs* (equal in a 45–45–90 triangle), never the hypotenuse. (This is the audit's
sharpest observation: `tan45°` is safe where `sin45°`/`cos45°` are not.)

*(P-α circularity: needs the area-proof of the sine addition formula + `sin90°=1`
(boundary value opp/hyp→1) — NON-CIRCULAR. P-γ: needs the altitude + ratio def of cos —
NON-CIRCULAR, but it is the similar-triangle proof. P-δ DIED circular; P-ε DIED vacuous —
see candidates.md.)*

---

## (b) Collision gauntlet

### P-β vs KUS 2025 (arXiv:2506.06304) — **the decisive collision**
**Queries run:**
- `Pythagorean theorem proof "tan" half-angle "a/(b+c)" angle bisector complementary 45 degrees tan45`
- `proof Pythagorean theorem bisect both acute angles half-angle tangent sum 45 degrees non-circular`
- (Phase-1) `Kise Uehara Shinzato 2025 Pythagorean angle bisector theorem tangent half-angle`

**Findings.** KUS's abstract (from snippets) lists three proofs, **two of which use the
angle-bisector theorem** (#2 "isosceles + angle bisector"; #3 "a novel relation from the
angle-bisector theorem, unifying #1,#2"). The targeted searches returned, alongside the
KUS links (`arxiv.org/abs/2506.06304`, `arxiv.org/html/2506.06304v1`), snippet prose
associating **`tan(θ)=a/(b+c)` from the angle bisector**, **the tangent (double-angle)
formula**, and **"when the sum of half-angles equals 45°, `tan45°=1` can be applied"** —
i.e. *exactly the ingredients of P-β*. I treat the prose cautiously (it may echo my
query), but it consistently points at KUS, and the abstract independently confirms
angle-bisector proofs there.

**Equivalence test.** Two trig proofs are "the same" if they use the same key identity +
construction up to relabeling. P-β = {angle-bisector theorem → `tan(half)=a/(b+c)` →
`A/2+B/2=45°`, `tan45°=1` → tangent addition}. This is squarely KUS's angle-bisector /
half-angle-tangent mechanism. P-β uses **no isosceles construction** (a possible
difference from KUS #2), but KUS #3 is explicitly "a novel relation from the
angle-bisector theorem" that **unifies** the approaches — the most likely exact match.

**Verdict for P-β: VARIANT — and, on the available evidence, very likely a DUPLICATE of
KUS 2025 (proof #2/#3).** I could not read the paper (403) to confirm the exact identity,
so I cannot certify "duplicate" with full confidence, but the evidence is strong enough
that **P-β is NOT addable**.

### P-α vs Zimba/Luzia
`sin(A+B)=sin90°=1` is an immediate corollary of the **non-circular sine addition
formula** that Zimba/Luzia already establish; it is the *dual* of Zimba's
`cos(A−A)=cos0=1`. **Verdict: VARIANT (essentially a one-line corollary of Zimba's
framework) — not meaningfully new.**

### P-γ vs the classical similar-triangle proof
`c=a cosB+b cosA` with the altitude reproduces `AH=b²/c`, `HB=a²/c` — the geometric-mean
/ similar-triangle proof (Euclid VI), in cosine notation. **Verdict: KNOWN (core B);**
also debatable whether it is "genuinely trigonometric."

---

## Outcome
- **P-δ, P-ε** died in Phase 2 (circular / vacuous).
- **P-γ** = KNOWN (similar-triangle proof).
- **P-α** = VARIANT (Zimba corollary).
- **P-β** = NON-CIRCULAR and rigorous, but **VARIANT / very likely DUPLICATE of KUS 2025**.

No candidate survives as NON-CIRCULAR **and** NO-COLLISION-FOUND. P-β proceeds to the
full Phase-4 write-up **as the best-constructed survivor, carrying the honest
"likely-duplicate-of-KUS" verdict** — because the rigorous construction + circularity
audit is still worth recording, even though its novelty fails.
