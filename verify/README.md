# Verification

> **Project 2 (current `proof/FINAL_PROOF.md` — skew-generator proof):** see the
> "Project 2 verification" section at the bottom. The checks below the line are
> from Project 1 (archived integral-geometry proof) and still run/pass.

---

## Project 2 verification — `lie_generator_check.py` (SymPy + numeric)  ✅ PASS

Run: `python3 verify/lie_generator_check.py`. Real output (2026-06-25):

```
Solving skew-invariance for the form entries: [{b12: 0, b22: b11}]
=> invariant B = Matrix([[b11, 0], [0, b11]])  (a positive multiple of the identity)
(1) B(u, Ju) = 0  ->  PASS
(2) Q(u+v) - [Q(u)+Q(v)] for v=lambda*Ju: 0  ->  PASS
Q(u) = b11*(ux**2 + uy**2)   => c0 = b11 > 0, Q = c0 * L^2.
max relative error of Q(u+v) - (Q(u)+Q(v)) over 100000 instances: 5.547e-16  -> PASS
=== SKEW-GENERATOR CHECKS: PASS ===
```

This confirms, from skew-invariance `JᵀB + BJ = 0` **alone** (B abstract):
the invariant form is forced to `b₁₁·I` (Schur uniqueness, the textbook backbone of
axiom P5); `B(u,Ju)=0` (Lemma 2, exact); `Q(u+v)=Q(u)+Q(v)` for `v=λJu` (the
theorem, exact); and numeric sanity on 100,000 random right triangles to ~5.5e-16.

**Lean (`lean/Pythagoras.lean`): NOT COMPILED.** No Lean/lake/elan toolchain exists
in this environment (Phase 0). The file is a sketch (now including a
`skew_orthogonal` lemma for Project 2's Lemma 2) written against current mathlib
API; it was **not** machine-checked and nothing should be read as passing.

---

## Project 1 verification (archived proof) — still runs

Three independent checks of the archived integral-geometry proof. That proof uses
**no coordinates**; these checks introduce coordinates purely as a measuring/sanity
device.

## 1. Symbolic check — `symbolic_check.py` (SymPy)  ✅ PASS

Confirms the proof's *objects* behave as the lemmas claim, by computing the
direction-integral in coordinates (`p_θ(u) = u·(cos θ, sin θ)`):

- `B(u,v) = ∫₀^{2π} p_θ(u)p_θ(v) dθ = π·(u·v)` — the constructed pairing is `π`
  times the Euclidean inner product (validates Lemma 1 + the identification used
  in the Novelty claim).
- `Q(u) = π·L(u)²` — validates Lemma 2 (`c0 = π`; the proof never uses this value).
- `B(u,v) = 0` for a perpendicular pair — validates Lemma 3.
- Polarization identity `Q(u+v) = Q(u)+2B(u,v)+Q(v)` — validates (★).
- `Q(v−u) = Q(u)+Q(v)` for `u⟂v` — the Pythagorean conclusion at the symbolic level.

Run: `python3 verify/symbolic_check.py`  → `ALL SYMBOLIC CHECKS: PASS`
(SymPy version used: 1.14; install with `pip install sympy`.)

## 2. Numerical Monte-Carlo — `monte_carlo.py` (stdlib only)  ✅ PASS

- **(A)** 200,000 random right triangles (right angle built by a 90° rotation,
  lengths measured only at the end): `max relative error of a²+b²−c² ≈ 7.5e-16`
  (threshold 1e-12). PASS.
- **(B)** Monte-Carlo of `B(u,v)` by sampling directions: matches `π·(u·v)`,
  including `≈ 0` for perpendicular pairs and `≈ 18.85` for the nonzero-dot case
  `u=(1,2), v=(3,1.5)` (`u·v=6`, `π·6≈18.85`). PASS.

Run: `python3 verify/monte_carlo.py`  → `OVERALL: PASS`

## 3. Formal verification — `lean/Pythagoras.lean` (Lean 4 / mathlib)  ⚠️ PARTIAL

**What is formalized:** the abstract core step
`⟪u,v⟫ = 0 ⇒ ‖u+v‖² = ‖u‖² + ‖v‖²` in a real inner-product space (via mathlib's
`norm_add_sq_real`), plus a concrete `EuclideanSpace ℝ (Fin 2)` instance for the
perpendicular legs `(a,0), (0,b)`.

**What is NOT formalized:** the novel content — the integral-geometric
*construction* of the inner product (Lemma 1), proportionality by rotation
invariance (Lemma 2), and orthogonality by reflection symmetry (Lemma 3).
Formalizing the directional-integral construction and its invariance under the
rotation/reflection action on the circle is substantial and left as future work.

**Build status in this environment:** no Lean toolchain (`lean`/`lake`/`elan`) is
installed in the container, so the file was **not compiled here**. It is written
against current mathlib API (`Mathlib.Analysis.InnerProductSpace.Basic`,
`norm_add_sq_real`, `EuclideanSpace.inner_eq`) and is expected to build in a
standard `lake` project with mathlib on the import path. This is reported
honestly rather than claimed as machine-checked.

## Summary

| Check | Tool | Scope | Status |
|---|---|---|---|
| Symbolic identities | SymPy | all lemma identities (in coords) | ✅ PASS |
| Random right triangles | Python stdlib | `a²+b²=c²`, err ~1e-16 | ✅ PASS |
| Pairing `B≈π(u·v)` | Python stdlib | Lemmas 2–3 numerically | ✅ PASS |
| Core orthogonality step | Lean 4 / mathlib | abstract endpoint only | ⚠️ written, not built (no toolchain) |
