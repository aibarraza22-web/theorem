# A Non-Circular Trigonometric Proof of the Pythagorean Theorem
## via the Angle-Bisector Half-Angle Tangents (Project 4)

---

## 0. VERDICT (read first)

**VARIANT — and, on the available evidence, very likely a DUPLICATE of
Kise–Uehara–Shinzato 2025 (arXiv:2506.06304).** The proof below is **rigorous and
genuinely non-circular** (full audit in §4), but its mechanism — the angle-bisector
theorem → half-angle tangents `tan(A/2)=a/(b+c)` → `tan45°=1` — is exactly the
angle-bisector / half-angle-tangent territory of KUS's proofs #2/#3. Search snippets
associate `tan=a/(b+c)`, the angle bisector, and "`tan45°` with summed half-angles" with
that paper, and its abstract confirms two angle-bisector proofs there.

- **Closest prior art:** **KUS 2025** (angle-bisector / tangent half-angle); also
  **Luzia 2015** (half-angle, cosine version).
- **Honest ceiling:** the only possible delta vs KUS is that this uses **no isosceles
  construction** (it bisects *both* acute angles and uses `A/2+B/2=45°` directly). That
  is too thin, and too likely covered by KUS #3 ("a novel relation from the
  angle-bisector theorem, unifying"), to claim "addable."
- **Residual caveat (mandatory):** I **could not read KUS, Luzia, or JJ in full** —
  WebFetch returned **HTTP 403 on every domain** (arXiv, ar5iv, cut-the-knot, Wikipedia,
  ResearchGate). So "duplicate" is an evidence-based inference, not a confirmed match;
  and the print/full-text catalog was not searchable.

The proof is given in full because the **circularity audit** (§4) is the real keeper —
it is what separates a valid trig proof from a fake one — even though the **novelty
fails**. Per the project's framing, an honest DUPLICATE/VARIANT verdict with sources is a
valid deliverable.

---

## 1. Setup and accepted (non-circular) facts

Right triangle `△ABC`, **right angle at `C`**. Sides: `a=BC` (opposite `A`),
`b=CA` (opposite `B`), `c=AB` (hypotenuse). Angles `A=∠BAC`, `B=∠ABC`.

Accepted facts, each with a derivation that does **not** assume `a²+b²=c²`:

- **(F1) Angle sum.** `A+B+C=180°`, `C=90°` ⟹ `A+B=90°`. *(Euclidean angle sum.)*
- **(F2) Ratio definitions.** In a right triangle, `tanθ = opposite/adjacent`
  (from similarity of right triangles — independent of Pythagoras).
- **(F3) Angle-bisector theorem.** A bisector from a vertex divides the opposite side in
  the ratio of the two adjacent sides. *(Proof: the two sub-triangles share the altitude
  from that vertex, so their areas — hence their bases — are in the ratio of the adjacent
  sides; equivalently the area form of the Law of Sines. No Pythagoras.)*
- **(F4) Tangent addition.** `tan(x+y) = (tan x + tan y)/(1 − tan x · tan y)`. *(From the
  area/projection proofs of the sine and cosine addition formulas — neither of which uses
  `sin²+cos²=1` — followed by `tan=sin/cos`; the `cos x cos y` cancels.)*
- **(F5) `tan 45° = 1`.** In a 45–45–90 isosceles right triangle the two **legs are
  equal**; `tan45° = opposite/adjacent = leg/leg = 1`. **This uses only equality of the
  legs, never the hypotenuse**, so it is non-circular. *(Crucial: `sin45°=leg/hyp` would
  need `hyp=leg√2`, i.e. Pythagoras — forbidden. `tan45°` dodges this.)*

**Forbidden and unused:** `sin²+cos²=1`, the unit-circle definition, `√(x²+y²)`, the law
of cosines.

---

## 2. The key lemma (half-angle tangent from the bisector)

**Lemma.** `tan(A/2) = a/(b+c)` and, symmetrically, `tan(B/2) = b/(a+c)`.

*Proof of the first (see figure).* Bisect angle `A`; let the bisector meet the opposite
side `BC` at `D`. By the angle-bisector theorem (F3),
```
BD/DC = AB/AC = c/b,   and   BD + DC = BC = a,   so   DC = a·b/(b+c).
```
The bisector splits `A` into two equal parts, so `∠CAD = A/2`. In triangle `ACD` the
angle at `C` is the original right angle, so `ACD` is right-angled at `C`; by the ratio
definition (F2),
```
tan(A/2) = tan(∠CAD) = (opposite)/(adjacent) = DC/CA = (a·b/(b+c))/b = a/(b+c).
```
The second identity follows by swapping the roles of `A,B` and `a,b` (bisect `B`, meet
`CA` at `E`, `CE = a·b/(a+c)`, `tan(B/2)=CE/CB=b/(a+c)`). ∎

Neither step used `sin²+cos²=1`.

---

## 3. The proof

By (F1), `A+B=90°`, hence `A/2 + B/2 = 45°`. Apply the tangent addition formula (F4) and
`tan45°=1` (F5):
```
1 = tan 45° = tan(A/2 + B/2) = ( tan(A/2) + tan(B/2) ) / ( 1 − tan(A/2)·tan(B/2) ).
```
Substitute the Lemma `tan(A/2)=a/(b+c)`, `tan(B/2)=b/(a+c)`. Clearing denominators (full
algebra in `verify/trig_check.py`) yields the clean identity
```
tan(A/2 + B/2) − 1  =  (a² + b² − c²) / ( c·(a + b + c) ).
```
The left side is `0` (it equals `tan45° − 1 = 0`). Since `c·(a+b+c) > 0`, the right side
is `0` only if its numerator vanishes:
```
a² + b² − c² = 0,    i.e.    a² + b² = c².    ∎
```

**Equivalent one-bisector form.** Since `B/2 = 45° − A/2`, the tangent subtraction
formula with `tan45°=1` gives `tan(B/2) = (1 − tan(A/2))/(1 + tan(A/2))`. Equating to
`b/(a+c)`: `b/(a+c) = (b+c−a)/(b+c+a)`; cross-multiplying gives `b(a+b+c)=(a+c)(b+c−a)`,
which simplifies to `b² = c² − a²`. (SymPy confirms the numerator of the difference is
exactly `a²+b²−c²`.)

---

## 4. Circularity audit (the spine)

| Fact used | Where | Non-circular source | Uses `sin²+cos²=1`? |
|---|---|---|---|
| `A+B=90°` | §3 | angle sum of a triangle (F1) | No |
| `tanθ=opp/adj` | §2 | similar right triangles (F2) | No |
| angle-bisector theorem | §2 | equal-altitude area ratio (F3) | No |
| `tan(A/2)=a/(b+c)` | §2 | F2+F3 + algebra | No |
| tangent addition | §3 | area/projection addition formulas (F4) | No |
| `tan45°=1` | §3 | leg/leg in a 45–45–90 triangle (F5) — **not** leg/hyp | No |
| `a²+b²=c²` | §3 | rational identity, SymPy-verified | (the conclusion) |

**No step assumes the Pythagorean theorem or `sin²+cos²=1`.** The sharp point: every
"special-angle value" used is `tan45°=1`, which depends only on two equal legs — never a
hypotenuse length — so the usual hidden circularity (`sin45°=1/√2`, `cos45°=1/√2`,
`1/(1+t²)` half-angle factors) is avoided. **Core: (C)/trig, non-circular.**

---

## 5. Figure

```
                 A
                 |\
                 | \                 Bisector AD of angle A meets BC at D.
   b = CA        |  \   c = AB       ∠CAD = A/2 ;  △ACD is right-angled at C.
   (adj to A)    |   \               tan(A/2) = DC/CA = a/(b+c).
                 |    \
                 |     \             Symmetrically, bisecting B gives
                 |  A/2 \            tan(B/2) = b/(a+c).
                 |______'\           A/2 + B/2 = 45°, tan45° = 1
                 C   D    B          ⇒ tan(A/2+B/2)=1 ⇒ a²+b²=c².
                  a = CB

      (right angle ⌐ at C)   D lies on CB with  CD = ab/(b+c),  DB = ac/(b+c).
```

---

## 6. Verification (Phase 5 — actually run)

`verify/trig_check.py` (SymPy + numeric) was executed; real output is in
`verify/README.md`. It confirms the **algebra**: `tan(A/2+B/2)−1` simplifies *exactly* to
`(a²+b²−c²)/(c(a+b+c))` (difference from the claimed value `= 0`); the one-bisector form's
numerator factors as `a²+b²−c²`; the half-angle relation is consistent with the ratio
defs; and numerically `tan(A/2+B/2)=1` to `<10⁻¹²` on six right triangles.

**Caveat (stated in the script):** SymPy *knows* `sin²+cos²=1`, so this check certifies
only the algebra — **not** non-circularity. Non-circularity rests on §4, not on SymPy.

---

## 7. Honest novelty statement

Rigorous and non-circular — but its mechanism is the angle-bisector / half-angle-tangent
route that **KUS 2025 already developed** (their proofs #2/#3), and the search evidence
points at an essentially identical construction (`tan(half)=a/(b+c)`, `tan45°`, summed
half-angles). **Verdict: VARIANT, very likely DUPLICATE of KUS 2025; not addable.** The
inability to read the 2025 paper (WebFetch 403) leaves a thin, honestly-stated margin of
doubt, but not enough to claim novelty. See `NOVELTY.md` for the ledger and the referee
pass (which the referee wins).
