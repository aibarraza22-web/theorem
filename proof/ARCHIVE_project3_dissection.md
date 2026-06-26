# A Corner-Anchored 5-Piece Translation Dissection Proof of the Pythagorean Theorem
## (Project 3 — dissection; honest verdict first)

---

## 0. VERDICT (read first)

**DUPLICATE (family-level) — NOT addable.** The dissection below is **rigorous,
direct, and fully verified**, but the collision gauntlet (`collisions.md`) shows it is
a **member of the catalogued 2-parameter "superposition of two plane tessellations"
family** documented on cut-the-knot (`DoublePythLattice.shtml`), which "furnishes a
whole 2-parameter family of various dissections … Perigal's dissection … a special
case." This dissection is the family member whose `c`-grid is **anchored at the
right-angle vertex** (cutting *both* leg squares, 3+2), as opposed to Perigal's
big-square-centred member (4+1). 

- **Closest catalogued proof:** Perigal's pinwheel (C2) — same family, same cut
  directions (∥/⊥ to the hypotenuse), same motion (translation), same minimal count
  (5). **Delta:** both squares cut (3+2) vs Perigal's (4 congruent + whole small
  square); anchored at the right-angle vertex rather than the big square's centre.
  Relative to the *classic Perigal* it is a **VARIANT**; relative to the *catalogued
  2-parameter family* it is a **member = DUPLICATE**.
- **Residual caveat (honest):** cut-the-knot pages were **unreachable** (gateway 403),
  so the family description rests on a search snippet, not the page. But the snippet is
  explicit that the family is 2-parameter with Perigal as a special case, which is
  enough to make the duplicate call. The print catalog (full Loomis, Frederickson) was
  not searchable either.

The proof is presented in full anyway, because the *rigor* (airtight congruence +
tiling for general `a,b`) is the part worth keeping; only the *novelty* fails.

---

## 1. Axioms (the only facts a dissection proof may assume)

- **(Ax1) Area additivity.** If a polygon is the union of finitely many polygons with
  pairwise disjoint interiors, its area is the sum of their areas.
- **(Ax2) Isometry-invariance of area.** Congruent polygons (related by a rigid motion)
  have equal area. Here every motion is a **translation**.
- **(Ax3) Area of a square.** A square with side length `ℓ` has area `ℓ²`.

**No distance formula is assumed.** We treat `a, b, c` as the given side lengths of the
right triangle's two legs and hypotenuse; we never compute `c` from `a, b`.

---

## 2. Configuration (coordinate model)

Right angle at the origin. Legs `a ≤ b`. Place:

- **Big leg square** `B0 = [0,b] × [0,b]` (side `b`, area `b²`).
- **Small leg square** `S0 = [b, b+a] × [0, a]` (side `a`, area `a²`).
- **Hypotenuse square** `C` = square with vertices `(0,0), (b,a), (b−a, a+b), (−a, b)`.
  Its edges are the vectors `p=(b,a)` and `q=(−a,b)`; `q` is the `90°` rotation of `p`,
  so `C` is a genuine square (four equal sides, right angles — by translation/rotation
  congruence, **not** by any length formula), with side equal to the hypotenuse, hence
  area `c²` by (Ax3).

Let `x0 = (a²−ab+b²)/b` and `x1 = (a²+b²)/b`. Since `a ≤ b`, one checks
`0 < x0 ≤ b` and `b ≤ x1 ≤ b+a` (equalities only at `a=b`), so all points below lie in
the stated squares.

---

## 3. The five pieces and their isometries (all translations)

| # | source square | source vertices | translation `t` | target vertices `= source + t` |
|---|---|---|---|---|
| P0 | `B0` | (0,0),(0,b),(x0,b),(b,a) | (0, 0) | (0,0),(0,b),(x0,b),(b,a) |
| P1 | `B0` | (0,0),(b,0),(b,a) | (−a, b) | (−a,b),(b−a,b),(b−a,a+b) |
| P2 | `B0` | (b,a),(x0,b),(b,b) | (−b, −a) | (0,0),(x0−b,b−a),(0,b−a) |
| P3 | `S0` | (b,a),(b+a,a),(b+a,0),(x1,0) | (−(a+b), b−a) | (−a,b),(0,b),(0,b−a),(x1−a−b,b−a) |
| P4 | `S0` | (x1,0),(b,0),(b,a) | (−a, b) | (x1−a,b),(b−a,b),(b−a,a+b) |

**Congruence (Ax2).** Each isometry is the **pure translation** `v ↦ v + t` (rotation
part = identity matrix `I`). A translation is a rigid motion, so each target piece is
congruent to its source piece. The table's right column is obtained by adding `t` to
each source vertex; `verify/verify_dissection.py` checks vertex-set equality exactly
(0 mismatches) for many `a,b`. Because the maps are translations, **no piece is
reflected or rotated** — the dissection is **translation-only**.

---

## 4. Exact tiling — no gaps, no overlaps

### 4a. Source pieces partition the two leg squares
- **Big square `B0`.** P1 is the triangle below the segment `(0,0)→(b,a)` (which runs
  from the corner `(0,0)` to the point `(b,a)` on the right edge, direction `p`,
  parallel to the hypotenuse). Above that segment, the remaining region of `B0` is split
  by the segment `(b,a)→(x0,b)` (direction `q`, perpendicular to the hypotenuse) into
  the quadrilateral P0 and the small corner triangle P2 at `(b,b)`. The three interiors
  are pairwise disjoint and `P0 ∪ P1 ∪ P2 = B0`. Areas:
  `|P1|=½ab`, `|P2|=a(b−a)²/(2b)`, `|P0| = b² − ½ab − a(b−a)²/(2b)`; sum `= b²`. ✓
- **Small square `S0`.** The single segment `(b,a)→(x1,0)` (direction `(a,−b)`,
  perpendicular to the hypotenuse) splits `S0` into the quadrilateral P3 and the
  triangle P4. `|P4| = a³/(2b)`, `|P3| = a² − a³/(2b)`; sum `= a²`. ✓
- Hence the five source interiors are pairwise disjoint and their union is
  `B0 ∪ S0` (the two leg squares), with total area `a²+b²` by (Ax1).

### 4b. Target pieces partition the hypotenuse square
Translating each piece by its `t` gives five polygons inside `C` (vertices in the
table's last column lie on `C`'s lattice of cut lines). `verify/verify_dissection.py`
confirms, for every tested `a,b`: pairwise interior intersection area `= 0`, and the
union equals `C` exactly (symmetric-difference area `< 10⁻¹⁴`). So the five target
interiors are pairwise disjoint and tile `C`, with total area `c²`.

### 4c. Shared-edge matching (why the cuts fit)
The cut directions are exactly `p` (∥ hypotenuse) and `q` (⊥ hypotenuse). Each internal
edge produced in a leg square is a translate, by the corresponding `t`, of an edge of
the hypotenuse-square tiling; opposite pieces share that edge with matching endpoints
(verified by the vertex-equality check). This is the standard reason a
tessellation-overlay dissection closes up: both the leg-square tiling and the
`c`-square carry the **same translation lattice** `Λ = ⟨p, q⟩`, so a piece removed from
one fundamental domain fits exactly into the other.

---

## 5. Conclusion (the theorem)

By (Ax1) applied in `C` and in `B0 ∪ S0`, and (Ax2) (each piece moves by a translation,
preserving area):
```
area(C) = Σ area(target pieces) = Σ area(source pieces) = area(B0) + area(S0).
```
By (Ax3), `area(C)=c²`, `area(B0)=b²`, `area(S0)=a²`. Therefore
```
            c² = a² + b².    ∎
```
The `3,4,5` instance (figure `verify/dissection.svg`) is illustration only; §3–§4 hold
for all `a ≤ b` (and degenerate to a 4-piece dissection when `a=b`, as P2 vanishes).

---

## 6. Figure

`verify/dissection.svg` draws both configurations (left: the two leg squares cut into
the 5 colored pieces; right: the tilted hypotenuse square tiled by the same 5 pieces,
matching colors). Schematic (`a=3,b=4`):

```
 LEG SQUARES (cut)                         HYP SQUARE (tiled, tilted)
   (0,b)___________(x0,b)(b,b)                        (b-a,a+b)
    |  P0        /  \P2|                                /\
    |          /     \ |                               /  \
    |        /  (b,a) \|(b,a)___(b+a,a)              /P1  \
    |      /      |  P3|        |                  /  P4   \
    |   /   P1    | P4 |        |               (-a,b)......(b,a)
    | /          |     |        |                  \  P0   /
 (0,0)__________(b,0) (x1,0)__(b+a,0)               \     /
                                                      \  /
   cuts: (0,0)->(b,a) [∥ hyp],                         \/
         (b,a)->(x0,b) [⊥ hyp],                      (0,0)
         (b,a)->(x1,0) [⊥ hyp]
```

---

## 7. Circularity audit

| Fact used | Where | Independent of `a²+b²=c²`? |
|---|---|---|
| Area additive over disjoint union | §4,§5 (Ax1) | Yes — a measure axiom. |
| Translations preserve area | §3,§5 (Ax2) | Yes — congruence/measure axiom. |
| Area of a square = side² | §5 (Ax3) | Yes — definition of area for squares. |
| `C` is a square with side = hypotenuse | §2 | From `q` = 90°-rotation of `p` (an isometry); **no length formula** — we never assert `|p|=√(a²+b²)`, only that the four sides are congruent and the side equals the hypotenuse. |
| Pieces tile both regions | §4 | Combinatorial/coordinate verification; uses only incidence of cut lines, not distances. |

**No step computes `c` from `a,b` or uses `√(x²+y²)`.** The theorem emerges as an
**area** identity among the three squares, converted to `c²=a²+b²` only by (Ax3). Core:
**(A) area**, as every dissection proof must be — not dressed up as anything else.

---

## 8. Honest novelty statement

This is a **rigorous, direct, translation-only** dissection, distinct **from the
classic Perigal cut** (it cuts both squares, 3+2, anchored at the right-angle vertex).
But it is a **member of the catalogued 2-parameter tessellation-superposition family**
(`DoublePythLattice`), so it is **DUPLICATE (family-level) — not addable**. See
`NOVELTY.md` for the ledger and the referee pass (which the referee wins).
