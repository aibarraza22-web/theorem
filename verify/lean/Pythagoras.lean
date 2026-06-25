/-
  Formal verification (Lean 4 / mathlib) of the CORE STEP of the proof in
  proof/FINAL_PROOF.md.

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
