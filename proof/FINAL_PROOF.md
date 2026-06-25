# Pythagoras via the Skew Infinitesimal Generator of Rotation
## (Project 2 — search-first; honest verdict at the end)

> **Read the verdict first (§7).** This is a *complete and non-circular* proof, but
> its novelty is deliberately capped. The prior-art gauntlet (`prior_art.md`) shows
> its substance is known. What follows is the best-constructed survivor (candidate
> **C2**), presented rigorously, with an explicit accounting of which step is new
> (thin) and which is borrowed.

---

## 0. Accepted starting facts (axioms)

Work in the Euclidean plane as a 2-dimensional real vector space with a fixed
origin `O`. We accept exactly:

- **(P1)** *(Linear structure.)* Vectors add and scale over `ℝ`; `dim = 2`.

- **(P2)** *(Rotations and the generator `J`.)* Rotations about `O` form a
  one-parameter group `{ρ_t}` of **linear** maps. Let `J := ρ_{90°}` be rotation by
  a right angle. Rotating by `90°` twice is rotation by `180°`, which is the
  **central inversion** `x ↦ −x`. Hence
  ```
  J^2 = −I.
  ```
  *(This is a congruence fact — "two right-angle turns is a half-turn is the
  point-reflection through `O`" — and uses no length formula.)*

- **(P3)** *(Length.)* There is a length function `L` on vectors with `L(u)=0 ⇔
  u=0`, homogeneity `L(λu)=|λ|L(u)`, and invariance under all rigid motions
  (rotations and reflections). No coordinate formula for `L` is assumed.

- **(P4)** *(Perpendicularity via the right-angle rotation.)* Two nonzero vectors
  are **perpendicular**, `u ⟂ v`, exactly when `v` is parallel to `Ju`, i.e.
  `v = λ·Ju` for some scalar `λ ≠ 0`. *(This is the definition of "right angle" in
  terms of the congruence `J`; it does not presuppose any metric formula. It agrees
  with the Euclidean right angle because `J` is the congruence that turns a
  direction into the perpendicular one.)*

- **(P5)** *(Proportionality input — BORROWED, see the honesty note.)* Squared
  measured length is a **rotation-invariant quadratic form**: there is a symmetric
  bilinear form `B` and a constant `c₀ > 0` with
  ```
  B(u,u) = c₀ · L(u)^2   for all u,     and   B(ρ_t u, ρ_t v) = B(u,v)  for all t.
  ```

**Honesty note on (P5).** (P5) is the genuine content of the Pythagorean theorem
("the measured metric comes from a rotation-invariant inner product"), and it is
**not new**. It is established by the integral-geometry construction of Project 1
(archived as `proof/ARCHIVE_project1_integral_geometry.md`): set
`B(u,v) = ∫₀^{2π} p_θ(u)\,p_θ(v)\,dθ` with `p_θ` the signed projection onto
direction `θ`; that `B` is bilinear and rotation-invariant, and `B(u,u)=π·L(u)^2`
by rotation invariance + quadratic homogeneity (so `c₀=π`). Equivalently, average
any positive-definite seed form over `{ρ_t}` (the Weyl/Hurwitz trick). We **import**
(P5) rather than re-derive it, and we **do not claim it as novel** — it is exactly
the known integral-geometry / inner-product core. This proof's only non-standard
move is the *orthogonality* step below.

---

## 1. The rotation generator is skew with respect to `B`

**Lemma 1.** `B(Ju, v) + B(u, Jv) = 0` for all `u, v`.

*Proof.* By (P5), `B` is invariant under every rotation `ρ_t`: `B(ρ_t u, ρ_t v) =
B(u,v)`. The family `t ↦ B(ρ_t u, ρ_t v)` is therefore constant in `t`. Differentiate
at `t=0`. Writing `G` for the infinitesimal generator (`d/dt ρ_t |_{t=0} = G`, so
`ρ_t = exp(tG)`), the product rule gives
```
0 = d/dt B(ρ_t u, ρ_t v)|_{t=0} = B(Gu, v) + B(u, Gv).
```
The generator `G` and the right-angle rotation `J` are the same one-parameter
group's infinitesimal and finite members; both are skew for `B` (the displayed
identity holds with `G`, and `J = ρ_{90°}` is in the group, so conjugation/invariance
by `J` likewise gives `B(Ju,Jv)=B(u,v)`; combined with `J^2=−I` this yields the
same skew relation for `J`). Concretely, from `B(Ju,Jv)=B(u,v)` apply it to
`(u, Jv)`: `B(Ju, J(Jv)) = B(u, Jv)`, i.e. `B(Ju, −v) = B(u,Jv)` using `J^2=−I`,
so `−B(Ju,v) = B(u,Jv)`, which is the claim. ∎

*(The middle paragraph is only to connect the finite map `J` to the skew relation;
the clean one-liner is the last sentence: `J^2=−I` plus `J`-invariance of `B` gives
`B(Ju,v) = −B(u,Jv)`.)*

**Lemma 2 (orthogonality for free).** `B(u, Ju) = 0` for every `u`.

*Proof.* Put `v = u` in Lemma 1: `B(Ju, u) + B(u, Ju) = 0`. Since `B` is symmetric,
`B(Ju, u) = B(u, Ju)`, so `2·B(u, Ju) = 0`, giving `B(u, Ju) = 0`. ∎

This is the heart of the route: **perpendicular vectors are `B`-orthogonal because
the rotation generator is skew-adjoint.** No coordinates, no `sin²+cos²=1`, no trig
identity — only `J^2=−I` and invariance of `B`.

---

## 2. The theorem

**Theorem (Pythagoras).** Let `△OAB` have its right angle at `O`. Set
`u = OA`, `v = OB` with `u ⟂ v`, and `a = L(u)`, `b = L(v)`, `c = L(AB)`. Then
`a² + b² = c²`.

*Proof.* By (P4), `v = λ·Ju` for some scalar `λ`. Write `Q(x) := B(x,x) = c₀ L(x)²`
(by (P5)). The hypotenuse is `AB = v − u`. Expanding the quadratic form by
bilinearity (P5) and symmetry,
```
Q(v − u) = Q(v) − 2·B(u, v) + Q(u).
```
The cross term: `B(u, v) = B(u, λ Ju) = λ·B(u, Ju) = 0` by Lemma 2. Hence
```
c₀ · c²  =  Q(v − u)  =  Q(u) + Q(v)  =  c₀ · a²  +  c₀ · b² .
```
Divide by `c₀ > 0`: `a² + b² = c²`. ∎

*(Using the diagonal `u + v` instead of `v − u` gives the same result, since the
cross term vanishes either way.)*

---

## 3. Figure

```
            B
            |\
            | \
   v = λ·Ju |  \   AB = v − u   (hypotenuse, length c)
   (len b)  |   \
            |    \
            O-----A
              u = OA  (length a)

   J turns a direction by a right angle:

        Ju ↑              u ⟂ v  means  v points along Ju  (axiom P4).
           |              The invariant form B makes J skew (Lemma 1),
           |  u           so B(u, Ju) = 0 (Lemma 2): the cross term in
   --------O------>       Q(u+v) dies, leaving Q(u+v) = Q(u) + Q(v).

   Two right-angle turns return the reverse direction:  J(Ju) = −u   (J² = −I).
```

TikZ version:

```latex
\begin{tikzpicture}[scale=1.4]
  \coordinate (O) at (0,0);
  \coordinate (A) at (2.2,0);          % u
  \coordinate (B) at (0,1.5);          % v = lambda * J u  (here lambda*|u| = b)
  \draw[thick] (O)--(A)--(B)--cycle;
  \draw (O) rectangle +(0.2,0.2);      % right angle at O
  \draw[->,gray] (O)--(0,0.9) node[left]{$Ju$};
  \draw[->] (O)--(A) node[below right]{$u$};
  \node[left] at (0,1.2){$v=\lambda Ju$};
  \node[above right] at (1.1,0.75){$v-u,\ c$};
\end{tikzpicture}
```

---

## 4. Verification (Phase 4 — actually run)

`verify/lie_generator_check.py` (SymPy + a numeric loop) was executed; real output
is reproduced in `verify/README.md`. It confirms, from skew-invariance **alone**
(with `B` left abstract):

- solving `J^T B + B J = 0` forces `B = b₁₁·I` (a positive multiple of the identity
  — the Schur/representation-theory uniqueness, the textbook backbone of (P5));
- `B(u, Ju) = 0` (Lemma 2) — **PASS**, exact;
- `Q(u+v) − [Q(u)+Q(v)] = 0` for `v = λ·Ju` (the Theorem) — **PASS**, exact;
- numeric sanity on 100,000 random right triangles: max relative error
  `5.5×10⁻¹⁶` — **PASS**.

No Lean toolchain is installed in this environment, so the Lean file
(`verify/lean/Pythagoras.lean`, the abstract orthogonality endpoint) is labeled
**NOT COMPILED** and is not claimed to pass. (Phase 0 honesty: see `LOG.md`.)

---

## 5. Circularity audit

| # | Fact used | Where | Why it is not Pythagoras-in-disguise |
|---|---|---|---|
| 1 | `J^2 = −I` | P2 | "Two `90°` rotations = the `180°` half-turn = central inversion `x↦−x`." Pure congruence; no length formula. |
| 2 | `u ⟂ v ⇔ v = λJu` | P4 | Definition of right angle via the congruence `J`. Independent of any metric formula. |
| 3 | `L` homogeneous & rigid-motion invariant | P3 | Congruence + similarity axioms; logically prior to I.47. |
| 4 | `B` invariant ⇒ `J` skew (`B(Ju,v)=−B(u,Jv)`) | Lemma 1 | Differentiate/transport the invariance of `B`; uses `J^2=−I` (fact 1). No coordinates, no `sin²+cos²=1`. |
| 5 | `B(u,Ju)=0` | Lemma 2 | Symmetry of `B` + skewness (fact 4). One line of algebra. |
| 6 | `B(u,u)=c₀L(u)²`, `B` bilinear & rotation-invariant | **P5 (imported)** | The known integral-geometry/inner-product core; constructed in Project 1 by averaging signed projections. **Borrowed, not claimed new.** Its own non-circularity is audited in the Project-1 file. |

**Tools deliberately avoided:** the coordinate distance formula `√(x²+y²)`, the
coordinate inner product `u₁v₁+u₂v₂` *as a definition*, `sin²+cos²=1`, the law of
cosines, and similar-triangle ratios. None appears in §1–§2. (The coordinate
identity appears only inside the SymPy check, clearly labeled as verification.)

**Where the real weight sits:** in (P5). The orthogonality machinery (§1–§2) is
genuinely coordinate-free and trig-free, but it only *converts* (P5) into the
theorem. (P5) is the substantive, non-novel input.

---

## 6. Novelty ledger (summary; full version in `NOVELTY.md`)

| Idea in this proof | Closest known proof (Phase 2) | Exact delta |
|---|---|---|
| `B(u,u)=c₀L(u)²` (proportionality) | Project 1 integral geometry; inner-product proofs | **none** — imported verbatim as (P5) |
| invariant form is unique = dot product | Schur uniqueness for `SO(2)` (Berkeley notes; arXiv 2103.01517) | none — textbook |
| orthogonality via skew generator `B(u,Ju)=0` | skew-adjointness of the isometry Lie algebra (Noether/Riemannian geometry) | **thin** — repackages orthogonality as Lie-algebra skewness instead of Project 1's *reflection symmetry*; no source found for *this exact application*, but trivially adaptable |

---

## 7. Final verdict (pick the honest one)

**NOT NOVEL (foundationally).** This proof reduces to core **(C)**
(bilinearity + orthogonality). Its substantive step (P5) is the known
integral-geometry / inner-product content (Project 1; Schur uniqueness of the
`SO(2)`-invariant form). The only non-standard element is the *exposition* of
orthogonality via the skew infinitesimal generator (`J^2=−I`,
`B(Ju,v)+B(u,Jv)=0 ⇒ B(u,Ju)=0`).

- **Closest prior art:** (i) Schur/representation-theory uniqueness of the
  `SO(2)`-invariant symmetric bilinear form
  (https://math.berkeley.edu/~serganov/math252/notes5.pdf;
  https://arxiv.org/pdf/2103.01517); (ii) skew-adjointness of the Lie algebra of an
  isometry group (standard Riemannian geometry / Noether); (iii) Project 1's
  averaged-projection construction of `B` (archived in this repo).
- **The most I will claim:** *PLAUSIBLY NOVEL only as a route/exposition* for the
  orthogonality step — **confidence LOW**. I found no write-up proving the planar
  theorem via the skew rotation generator, but the mechanism is textbook and an
  expert would adapt it in one line, so this does not rise to a novel *foundation*.
- **Unchecked risk W:** an undergraduate text or lecture note may present exactly
  this skew-generator packaging; my search did not exhaust the textbook literature
  (it is hard to query for "obvious" folklore). If found, the verdict drops to a
  flat NOT NOVEL with that source.

**Bottom line.** Honest ceiling: this is a clean, rigorous, non-circular *new
exposition* of a *known* (core-(C)) proof — not a genuinely new foundation. Per the
project's framing, the valuable output here is the **documented negative result**:
the four other candidate foundations (entropy power, information geometry, area
functional equations, plus the killed tropical/`p`-adic/heat-kernel routes) were
each shown to be KNOWN, circular, or meaningless, and the survivor's novelty is
honestly thin. See `LOG.md` for the dead ends and `NOVELTY.md` for the referee pass.
