# Phase 1 — Reference Catalog of KNOWN Dissection Proofs

Built so collisions can be checked (Phase 3). For each: piece count, the cut lines,
and the motion type (translation only / translation+rotation / with reflection).
Sources are from web search (full cut-the-knot pages were **not reachable** — the
gateway denies CONNECT to cut-the-knot.org, HTTP 403; see LOG.md Phase 0). So
descriptions of cut-the-knot pages rest on search snippets, not the pages themselves.

Right triangle: legs `a ≤ b`, hypotenuse `c`, `a²+b²=c²`. "Leg squares" = squares on
the legs (areas `a²`, `b²`); "hyp square" = square on the hypotenuse (`c²`).

---

## A. Area-counting / pinwheel (cut the HYP square)

### A1. Zhao Shuang "hsuan-thu" (xian-tu) / Chinese (Han era; comm. 3rd c. CE)
- **Pieces:** hyp square = 4 right triangles (legs `a,b`) + 1 central square side `(b−a)`. **5 pieces.**
- **Cut lines:** the four triangles are the right triangle itself, placed pinwheel
  inside the `c`-square; cut lines are the triangles' hypotenuses (= sides of the
  `c`-square's inscribed tilt).
- **Motion:** rotation (the 4 triangles are rotations of each other by 90°).
- **Logic:** `c² = 4·(½ab) + (b−a)²`. Primarily an **area identity**, not a literal
  leg-square→hyp-square rearrangement.

### A2. Bhaskara "Behold!" (12th c. CE)
- Essentially identical to A1: hyp square = 4 triangles + central `(b−a)²`. **5 pieces**, rotation.

### A3. Liu Hui "out–in complementary" (263 CE)
- **Pieces:** small number (commonly rendered as 3–5) by cutting the two leg squares
  and sliding/rotating fragments to fill the hyp square ("out-in" = remove protruding
  bits, fill concavities).
- **Cut lines:** along triangle edges/altitude segments of the figure.
- **Motion:** translation + rotation. Exact piece set varies by reconstruction.

---

## B. The two-leg-squares (bride's chair) cut into the hyp square

### B1. Thābit ibn Qurra (9th c. CE)
- **Configuration:** the two leg squares joined at the right-angle vertex (the
  "bride's chair" hexagon). Two cuts each equal to the hypotenuse detach two triangles
  congruent to the original.
- **Pieces:** **3** (a central piece + 2 triangles).
- **Cut lines:** two segments equal/parallel to the hypotenuse.
- **Motion:** **rotation** (each detached triangle rotates ~90° about a square corner).

### B2. (a+b)² two-square / Euclid-adjacent rearrangement
- A square of side `(a+b)` filled two ways: `{4 triangles + c²}` vs
  `{4 triangles + a² + b²}`. **Area identity**, 5 regions. Motion: rotation. (This is
  the algebraic twin of A1.)

---

## C. Tessellation / superposition (cut either side) — the family this project lands in

### C1. al-Nayrizi tessellation (9th c. CE) / "Pythagoras by Tessellation"
- Overlay the **Pythagorean tiling** (two squares of sides `a,b`, each touching four
  of the other size) with a grid of `c`-squares.
- **Pieces:** the `c`-square ∩ tiling tiles. With the standard alignment, **5 pieces**.
- **Cut lines:** edges of the Pythagorean tiling = sides of the leg squares and their
  translates; equivalently lines **parallel and perpendicular to the hypotenuse**.
- **Motion:** **translation only** (both the tiling and the `c`-grid are translation
  lattices; pieces move by lattice vectors).

### C2. Henry Perigal pinwheel (1873; discovered ~1830)
- **The classic translation dissection.** Cut the **larger** leg square (`b²`) by two
  lines **through its centre**, one parallel and one perpendicular to the hypotenuse,
  into **4 congruent** quadrilaterals; the **smaller** leg square (`a²`) stays
  **whole** and slides to the centre. **5 pieces = 4 + 1; small square uncut.**
- **Motion:** **translation only.**
- **Relation to C1:** Perigal is the special alignment of the tessellation overlay in
  which the `c`-grid is centred on the big squares.

### C3. **"Superposition of two plane tessellations" — a 2-PARAMETER FAMILY**
  (cut-the-knot, `DoublePythLattice.shtml`)
- Per search snippet: this proof **"furnishes a whole 2-parameter family of various
  dissections of squares on the legs of a right triangle that combine into a square on
  its hypotenuse,"** and **"Perigal's dissection could be obtained from this proof by
  combining all squares of the same size in natural quartets."**
- **Meaning:** sliding the `c`-grid by an arbitrary offset `(dx,dy)` over the
  Pythagorean tiling yields a **continuum (2-parameter family) of valid
  translation-only dissections**; Perigal is one special point. Piece counts vary with
  the offset (5 and up).
- **This is the crucial catalog entry for Phase 3:** any single tessellation-overlay
  dissection — including a corner-anchored one that cuts *both* squares — is a *member
  of this catalogued family*.
- Related cut-the-knot pages (titles only; pages unreachable, 403):
  `PythLattice.shtml`, `MiquelPlens.shtml` ("A Variant of Proof by Tessellation"),
  `PerigalII.shtml` ("A Proof Perigal and All Others After Him Missed"),
  `PythHexLattice.shtml`, `DancingSquares` (hinged).

---

## D. Rectangle/step ("P-slide") and other Loomis entries

### D1. Step / P-slide ("two squares to one")
- Convert each leg square to a rectangle (or the joined leg-squares hexagon) and use a
  staircase/P-slide. **~5 pieces** in general; **translation + rotation/reflection**.
- Catalogued generally (Frederickson, *Dissections: Plane & Fancy*, ch. on the
  Pythagorean theorem; web review confirms emphasis on **minimum-piece** dissections).

### D2. Epstein / Nelsen / Loomis miscellany
- Loomis (1927) catalogs 367 proofs incl. many dissections; Nelsen, *Proofs Without
  Words*, collects pictorial dissections. Specific low-piece dissections beyond the
  above were **not individually reachable** in my searchable sources.

---

## Known minimum piece counts (so "distinctive" has meaning)

- **Two unequal squares → one square: 5 pieces** is the classic count, achieved by
  **Perigal (translation-only)** and by the P-slide. 5 is the benchmark minimum for
  `a≠b`; **4 pieces** only in the degenerate `a=b` case.
- So a *clean translation-only 5-piece* dissection is **already at the known minimum**,
  and any such dissection produced by a grid-overlay sits inside the catalogued
  **2-parameter tessellation family (C3)**.

**Implication for Phase 2–3:** the room for a genuinely *uncatalogued* clean direct
dissection is small. Translation dissections collapse into family C3; low-piece
rotation dissections collapse into A1/A2/B1. The collision check must therefore test
*family membership*, not just piece count.

---

### Sources (search-reachable)
- Pythagorean tiling — Wikipedia: https://en.wikipedia.org/wiki/Pythagorean_tiling
- Perigal — Wikipedia: https://en.wikipedia.org/wiki/Henry_Perigal
- cut-the-knot index (snippets only; pages 403): https://www.cut-the-knot.org/pythagoras/
- DoublePythLattice (2-parameter family; snippet): https://www.cut-the-knot.org/pythagoras/DoublePythLattice.shtml
- Frederickson, *Dissections: Plane & Fancy* (MAA review): https://old.maa.org/press/maa-reviews/dissections-plane-fancy
- Frederickson ch.4 updates: https://www.cs.purdue.edu/homes/gnf/book/Booknews/ch4.html
- "An uncountable number of proofs of Pythagoras": https://arxiv.org/pdf/2301.06812
