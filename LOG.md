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

---
---

# PROJECT 2 — Search-first novelty attempt (supersedes Project 1's novelty claim)

A second, stricter pass. The brief: treat **novelty as the hard part**, earn every
claim against the literature, and accept that a well-documented **negative result**
is a success. Crucially, it flags that Project 1's integral-geometry proof
**accidentally rediscovered Cauchy/Crofton integral geometry** — now an exhausted
foundation. Project 1's files are archived under `proof/ARCHIVE_project1_*` and its
novelty claim is retracted to "route-level at best."

## P2 · Entry 0 — Phase 0 tooling check (HONEST)

Actually tested, not assumed:
- **Web search: YES** — works (returned live results incl. 2025 arXiv papers).
- **WebFetch: YES** — available.
- **SymPy: YES** — `sympy 1.14.0`, runs (executed `verify/lie_generator_check.py`).
- **Lean/lake/elan: NO** — none installed (`command -v` all empty). Therefore the
  Lean file is labeled **NOT COMPILED** and claimed to pass *nothing*. (Project 1's
  README said "written, not built"; I am keeping that and making it louder, to avoid
  the contradiction the brief warns about.)

Novelty-confidence ceiling is NOT capped by tooling (web search works), but IS
capped by what the searches found.

## P2 · Entry 1 — Candidates (see `candidates.md`)

Generated 9 routes, biased off the exhausted list. Killed on sight: tropical
(C6, no honest meaning — degenerates to `max(a,b)`), p-adic (C7, ultrametric, no
Euclidean content), heat-kernel isotropy (C8, circular — isotropy = the conclusion),
projection-theorem/KKT (C9, = Hilbert projection, known). Survivors to gauntlet:
C1 SO(2)-invariant form, C2 skew generator, C3 entropy power inequality, C4
information geometry, C5 area functional equation.

## P2 · Entry 2 — Prior-art gauntlet (see `prior_art.md`) — the decisive step

Ran real web searches (queries + URLs logged in `prior_art.md`). Results:
- **C1 → KNOWN.** Schur/representation-theory: the `SO(2)`-invariant symmetric form
  is unique up to scale = the dot product. Textbook.
- **C3 → KNOWN.** "In 1-D the EPI reduces to additivity of variances" — i.e. core
  (C), already exhausted.
- **C4 → KNOWN + circular.** Amari: squared Euclidean distance is the *base example*
  the generalized (Bregman) Pythagorean theorem generalizes; it presupposes the
  Euclidean case.
- **C5 → KNOWN.** Core (A); and area-additivity on the needed dissections is
  *harder than Pythagoras itself* (cited obstruction).
- **C2 → PARTIAL (route only).** No write-up found proving the *planar* theorem via
  the skew rotation generator, BUT every ingredient (skew-adjoint isometry algebra,
  `J²=−I`, invariant-form uniqueness) is standard and trivially adaptable.

**Conclusion of the gauntlet:** every fresh-sounding foundation collapses onto core
(A)/(B)/(C) or is circular. Only C2 survives, and only as exposition.

## P2 · Entry 3 — Dead ends (candid)

- *Hoping EPI would be "more than" variance additivity:* it isn't, in the 1-D case
  that maps to the plane. Dead end.
- *Hoping information geometry gives an independent Euclidean proof:* it can't — the
  Euclidean case is its definitional seed. Dead end (circular).
- *Hoping the skew-generator route would be a new FOUNDATION:* it is core (C); the
  substantive proportionality step (P5) is the same invariant-form content as
  Project 1 and the inner-product proofs. I could not de-circularize the
  proportionality without re-importing averaging/projection. So C2's genuine delta
  shrank to "orthogonality via Lie-skewness instead of reflection symmetry" — thin.

## P2 · Entry 4 — Construction + verification

Built C2 fully and rigorously in `proof/FINAL_PROOF.md` (axioms, Lemmas 1–2,
theorem, figure, circularity audit). Verified in `verify/lie_generator_check.py`:
symbolic (exact) + numeric (5.5e-16 on 100k random instances) — **PASS** (real
output pasted in `verify/README.md`). Lean sketch updated with a `skew_orthogonal`
lemma but **NOT COMPILED**.

## P2 · Entry 5 — Referee + verdict (see `NOVELTY.md`)

Referee argued "this is just the inner-product proof; (P5) IS the theorem and
`B(u,Ju)=0` is `u·Ju=0`." **The referee is right**, and the verdict concedes it.

**FINAL VERDICT (Project 2): NOT NOVEL (foundationally).** The proof reduces to core
(C); its substance (P5) is known integral-geometry/inner-product content; its only
non-standard element is a coordinate-free *exposition* of orthogonality via the skew
generator — **PLAUSIBLY NOVEL only as a route, confidence LOW**. Closest prior art:
Schur uniqueness of the `SO(2)`-invariant form + skew-adjointness of the isometry
Lie algebra + Project 1's averaged-projection construction. Unchecked risk: a
textbook may already present the skew-generator packaging as folklore (would harden
the negative verdict).

**Meta-lesson:** the honest, defensible deliverable here is the *negative result and
its audit trail* — a map of why five candidate foundations are each KNOWN, circular,
or meaningless — not a manufactured novelty claim. This is recorded as a success per
the project's own framing.

---
---

# PROJECT 3 — A dissection "addable to the catalog" (search-first, collision-driven)

Goal: a DIRECT, rigorous dissection (every cut a line of the figure) that is **not
already catalogued**. The collision check is the heart. Project-2 deliverables sharing
filenames were archived as `ARCHIVE_project2_*` / `proof/ARCHIVE_project2_skew_generator.md`.

## P3 · Entry 0 — Phase 0 tooling (HONEST)
- **Web search: YES** (live results, incl. 2025 arXiv dissection papers).
- **WebFetch: PARTLY.** Works for many sites, but **cut-the-knot.org is unreachable** —
  the agent gateway denies CONNECT (HTTP 403; confirmed via `$HTTPS_PROXY/__agentproxy/status`,
  `recentRelayFailures: connect_rejected … www.cut-the-knot.org:443`). This is a
  network-policy block I cannot bypass. **Consequence:** cut-the-knot evidence is from
  **search snippets only**, so any "not catalogued" claim is capped to "not found in
  sources I could actually read," and cut-the-knot's own variant pages
  (`MiquelPlens`, `PerigalII`, `DoublePythLattice`) I could see only as snippets.
- **SymPy: YES** (1.14). **Shapely: YES** (2.1.2, after `pip install`). **numpy:** not
  needed. **SVG:** emitted by hand-written XML (no lib).
- Lean: irrelevant here (no formalization attempted for a dissection).

## P3 · Entry 1 — Catalog (known_dissections.md)
Recorded Zhao/Bhaskara (5, rotation), Liu Hui, Thābit (3, rotation), al-Nayrizi/Perigal
(5, translation), and — critically — the cut-the-knot **2-parameter
tessellation-superposition family** (`DoublePythLattice`). Known minimum for `a≠b` is
**5 pieces** (Perigal/P-slide). So a clean translation 5-piece dissection is already at
the minimum and lives in the tessellation family.

## P3 · Entry 2 — Candidate generation (candidates.md, verify/explore.py)
Wrote a Shapely generator that overlays a `c`-grid on the Pythagorean tiling for general
`(a,b)` and extracts pieces. **Sanity check passed:** the generator reproduces Perigal
exactly (offset (1.5,2.0): big→4 congruent, small whole). Scanning offsets found:
- offset **(0,0)** → 5 pieces, **both squares cut (3+2)** — candidate **K1**;
- offset (1,−1) → 6 pieces (3+3); (−0.5,−1) → 6 (4+2); etc.
K1 was appealing: minimal count (5) like Perigal but a different cut (both squares).

## P3 · Entry 3 — Rigor + verification (verify/verify_dissection.py, dissection.svg)
Derived **closed-form general-`(a,b)`** piece coordinates (`x0=(a²−ab+b²)/b`,
`x1=(a²+b²)/b`) and verified independently (not via the tiling intersection):
for `a,b ∈ {(3,4),(1,2),(5,12),(2,3),(√2,3),(0.7,2.3),(≈1,1)}` — areas sum to `c²` on
both sides, pairwise overlap 0, unions equal the leg squares / hyp square
(symmetric-difference `<10⁻¹⁴`), and every translation maps source vertices onto target
vertices exactly (0 mismatches). **All PASS.** SVG emitted. So K1 is a *correct, direct,
translation-only* dissection.

## P3 · Entry 4 — Collision gauntlet (collisions.md) — the decisive step
Real searches. The killer finding (snippet of `DoublePythLattice.shtml`): the
"superposition of two plane tessellations" proof **"furnishes a whole 2-parameter
family of various dissections … Perigal a special case."** K1 is generated by exactly
this overlay; it is the **right-angle-vertex-offset member** of that family. So K1 is a
member of an **explicitly catalogued 2-parameter family** → **DUPLICATE (family-level)**.
Against the *classic Perigal special case* it is a VARIANT (3+2 vs 4+1), but that does
not lift it out of the family. Could not read the cut-the-knot pages directly (403).

## P3 · Entry 5 — Dead ends / candidates that died
- **K2 = Perigal** (recovered): outright DUPLICATE (it's literally Perigal).
- **K5 = Thābit** (3-piece rotation): outright DUPLICATE.
- **K3,K4** (6-piece offsets): also members of family C3; non-minimal; DUPLICATE-family.
- **Altitude-rectangle idea** (split hyp square into two similar-triangle rectangles,
  then rectangle→square P-slides): abandoned — the rectangle-to-square step is
  case-dependent on the aspect ratio (no clean general-`a,b` proof) and the sub-steps
  are themselves catalogued (Frederickson). Would not have been cleaner or newer.
- **General observation:** every clean *direct* dissection I could construct collapses
  into a catalogued family (tessellation/Perigal, or Zhao/Bhaskara/Thābit, or P-slide).

## P3 · Entry 6 — Verdict
**DUPLICATE (family-level): K1 is a member of the catalogued 2-parameter
tessellation-superposition family (cut-the-knot `DoublePythLattice`); closest famous
member is Perigal.** Not addable. The rigorous, machine-verified construction is kept as
a correct worked dissection. Honesty caps: cut-the-knot pages unreadable (403); print
catalog (full Loomis / Frederickson) not searchable — but neither gap points toward
novelty. Per the mission, a documented DUPLICATE **with the source** is a valid,
honest deliverable.

---
---

# PROJECT 4 — A non-circular trigonometric proof (the live frontier)

Goal: a non-circular trig proof using a mechanism NOT in {Zimba 2009, Luzia 2015,
Jackson–Johnson 2024 + their §5 generator, Kise–Uehara–Shinzato 2025}. Project-3
deliverables sharing filenames archived as `ARCHIVE_project3_*`.

## P4 · Entry 0 — Phase 0 tooling (HONEST, and consequential)
- **Web search: YES.** **SymPy: YES** (1.14, ran `verify/trig_check.py`).
- **WebFetch: NO — HTTP 403 on EVERY domain tried** (arxiv.org, ar5iv.org,
  ar5iv.labs.arxiv.org, cut-the-knot.org, en.wikipedia.org, researchgate.net).
  Confirmed it is global, not site-specific. **Consequence:** I could not read a single
  full paper (Zimba/Luzia/JJ/KUS). All mechanisms and all collision evidence come from
  **search snippets only**, and snippet *prose* sometimes paraphrases the query, so I
  weight the paper links/abstracts over the prose. Every "not in literature" claim is
  capped to "not found in reachable snippets."

## P4 · Entry 1 — Catalog (known_trig_proofs.md)
Reconstructed mechanisms: Zimba = subtraction formula + `cos0=1`; Luzia = addition →
cosine half-angle; JJ = Law of Sines + reflected isosceles + series, **+ a §5 generating
family**; KUS 2025 = three proofs (tan double-angle + isosceles; **angle bisector** +
isosceles; **novel relation from the angle bisector** unifying them). Occupied territory
is broad.

## P4 · Entry 2 — Candidates (candidates.md)
Six routes. **Two died immediately:** P-δ Weierstrass `t=tan(A/2)` is **CIRCULAR** (the
`1/(1+t²)` factor is `cos²(A/2)=1/(1+tan²)`, which is `sin²+cos²=1` smuggled in); P-ε law
of tangents is **VACUOUS** (tautology on the right triangle). Survivors: P-α (sine
addition at complement → `sin90°=1`), **P-β (angle-bisector half-angle tangents)**, P-γ
(projection formula `c=a cosB+b cosA`).

## P4 · Entry 3 — The proof I actually like (P-β) and its clean identity
Bisect both acute angles: `tan(A/2)=a/(b+c)`, `tan(B/2)=b/(a+c)` (angle-bisector theorem
+ ratio def). `A/2+B/2=45°`, `tan45°=1`, tangent addition ⇒ the strikingly clean
`tan(A/2+B/2)−1 = (a²+b²−c²)/(c(a+b+c))` (SymPy-verified, exact). So `tan45°=1` forces
`a²+b²=c²`. **Circularity audit clean** — key insight: `tan45°=1` is non-circular
(leg/leg) whereas `sin45°`/`cos45°` are circular (need the hypotenuse). This is the
keeper.

## P4 · Entry 4 — Collision gauntlet (audits.md) — the proof is NOT new
Targeted searches (`tan a/(b+c) angle bisector tan45`, `bisect both acute angles half
angle 45`) return KUS 2025 (arXiv:2506.06304) and snippet prose with **exactly P-β's
ingredients**: `tan=a/(b+c)` from the angle bisector, the tangent formula, and "`tan45°`
when the half-angles sum to 45°." Combined with KUS's abstract (two angle-bisector
proofs + a unifying "novel relation"), **P-β is very likely KUS's proof #2/#3.** Could
not read the paper to confirm (403). P-α = Zimba corollary (VARIANT); P-γ = classical
similar-triangle proof (KNOWN). **No survivor is NO-COLLISION.**

## P4 · Entry 5 — Dead ends (candid)
- Hoped the **half-angle / Weierstrass** route was a fresh mechanism → it is **circular**
  (hidden `sin²+cos²=1`). Genuinely instructive death.
- Hoped **bisecting both acute angles + tan45** was distinct from KUS's *isosceles*
  angle-bisector proof → snippets indicate KUS already cover the `tan=a/(b+c)`+`tan45`
  idea; the no-isosceles distinction is too thin and likely subsumed by KUS #3.
- Hoped **P-α** (`sin(A+B)=sin90°=1`) might count as new → it is a one-line corollary of
  the non-circular addition formula = morally Zimba.
- Mollweide/Newton routes die on `sin45°`/`cos45°` (circular); law of tangents vacuous.

## P4 · Entry 6 — Verdict
**VARIANT — very likely DUPLICATE of KUS 2025; not addable.** The featured proof (P-β) is
**rigorous and genuinely non-circular** (its audit and the `tan45°` insight are the real
deliverable), but its mechanism is KUS's 2025 angle-bisector / half-angle-tangent route.
Honesty caps: WebFetch 403 → could not read KUS/Luzia/JJ in full; verdict is
evidence-based, not a confirmed line-by-line match. Per the mission, an honest
DUPLICATE/VARIANT verdict with sources is a valid deliverable.
