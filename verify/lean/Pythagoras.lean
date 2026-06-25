/-
  ==========================================================================
  STATUS: NOT COMPILED. No Lean/lake/elan toolchain exists in this environment
  (verified in Phase 0; see LOG.md). This file is a SKETCH written against
  current mathlib API and was NOT machine-checked. Do not read any "pass" into it.
  ==========================================================================

  Formal verification (Lean 4 / mathlib) of the CORE STEP of the proof in
  proof/FINAL_PROOF.md.

  Covers BOTH Project 1 (orthogonality by reflection symmetry) and Project 2
  (orthogonality by the skew generator J): in either case the abstract endpoint
  is the same, < u, v > = 0  =>  ||u+v||^2 = ||u||^2 + ||v||^2. A `skew_orthogonal`
  lemma below also captures Project 2's Lemma 2 (B(u, Ju) = 0 from skew-adjointness)
  at the abstract inner-product level.

  SCOPE (read this honestly):
  ---------------------------------------------------------------------------
  What IS formalized here: the abstract orthogonality => sum-of-squares
  implication that the whole proof drives toward, namely

        <u, v> = 0   =>   ||u + v||^2 = ||u||^2 + ||v||^2,

  in an arbitrary real inner-product space. In mathlib this is essentially
  `norm_add_sq_real` specialized to the orthogonal case (`inner_eq_zero`).

  What is NOT formalized here: the integral-geometric CONSTRUCTION of the inner
  product B(u,v) = ∫ p_θ(u) p_θ(v) dθ, Lemma 2 (Q = c0·L^2 by rotation
  invariance), and Lemma 3 (orthogonality by reflection symmetry). Those are the
  novel, non-circular content; formalizing the directional-integral construction
  would require building the projection functional and its invariance under the
  rotation/reflection action on the circle, which is a substantial development
  left as future work. The lemma below certifies only that, GIVEN an inner
  product and orthogonality, the Pythagorean identity follows — the uncontested
  algebraic endpoint.

  Build: requires a Lean 4 project with mathlib on the import path
  (`lake new`, add mathlib, then `lake build`).
-/

import Mathlib.Analysis.InnerProductSpace.Basic
import Mathlib.Analysis.InnerProductSpace.PiL2

open RealInnerProductSpace

variable {E : Type*} [NormedAddCommGroup E] [InnerProductSpace ℝ E]

/-- Core step (abstract Pythagoras): in a real inner-product space, if `u` and
`v` are orthogonal then `‖u + v‖^2 = ‖u‖^2 + ‖v‖^2`. This is the algebraic
endpoint that proof/FINAL_PROOF.md reaches after constructing the inner product
by integral geometry (Lemma 1) and proving orthogonality by reflection symmetry
(Lemma 3). -/
theorem pythagoras_core (u v : E) (h : ⟪u, v⟫_ℝ = 0) :
    ‖u + v‖ ^ 2 = ‖u‖ ^ 2 + ‖v‖ ^ 2 := by
  -- Expand ‖u+v‖^2 = ‖u‖^2 + 2⟪u,v⟫ + ‖v‖^2 and kill the cross term.
  rw [norm_add_sq_real]
  rw [h]
  ring

/-- The same statement phrased with the hypothesis as `Inner.inner`-orthogonality,
to match how Lemma 3 delivers it (`B(u,v) = 0`). -/
theorem pythagoras_of_orthogonal (u v : E) (h : ⟪u, v⟫_ℝ = 0) :
    ‖u + v‖ ^ 2 = ‖u‖ ^ 2 + ‖v‖ ^ 2 :=
  pythagoras_core u v h

/-- Concrete instance in the Euclidean plane `EuclideanSpace ℝ (Fin 2)`:
the perpendicular legs (a,0) and (0,b) give c^2 = a^2 + b^2. This mirrors the
SymPy check `Q(v-u) = Q(u)+Q(v)` for u=(a,0), v=(0,b). -/
example (a b : ℝ) :
    let u : EuclideanSpace ℝ (Fin 2) := !₂[a, 0]
    let v : EuclideanSpace ℝ (Fin 2) := !₂[0, b]
    ‖u + v‖ ^ 2 = ‖u‖ ^ 2 + ‖v‖ ^ 2 := by
  intro u v
  have h : ⟪u, v⟫_ℝ = 0 := by
    simp [u, v, EuclideanSpace.inner_eq, Fin.sum_univ_two]
  exact pythagoras_core u v h

/-- Project 2, Lemma 2 at the abstract level: if a linear map `J` is skew-adjoint
for the inner product (`⟪J u, w⟫ + ⟪u, J w⟫ = 0`), then every vector is orthogonal
to its image `J u`. With `J` the right-angle rotation this is "perpendicular legs
are inner-product-orthogonal," obtained from skewness alone — no coordinates.
(SKETCH, NOT COMPILED.) -/
theorem skew_orthogonal (J : E →ₗ[ℝ] E)
    (hskew : ∀ x w : E, ⟪J x, w⟫_ℝ + ⟪x, J w⟫_ℝ = 0) (u : E) :
    ⟪u, J u⟫_ℝ = 0 := by
  have h := hskew u u                      -- ⟪J u, u⟫ + ⟪u, J u⟫ = 0
  rw [real_inner_comm (J u) u] at h        -- ⟪u, J u⟫ + ⟪u, J u⟫ = 0
  linarith
