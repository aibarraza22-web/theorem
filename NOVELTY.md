# Phase 5 — Novelty Ledger + Skeptical Referee

This project's final proof is `proof/FINAL_PROOF.md` (candidate **C2**, the skew
infinitesimal generator). Below: a per-idea novelty ledger against the Phase 2
prior art, then a referee pass that argues the *opposite* of any novelty claim and
answers it honestly.

---

## 1. Novelty ledger

| Key idea | Closest known proof (source) | Exact delta |
|---|---|---|
| **Proportionality** `B(u,u)=c₀·L(u)²`, `B` rotation-invariant (axiom P5) | Inner-product proofs; Project 1's averaged-projection construction; Schur uniqueness of the `SO(2)`-invariant form (Berkeley rep-theory notes https://math.berkeley.edu/~serganov/math252/notes5.pdf ; arXiv 2103.01517 https://arxiv.org/pdf/2103.01517 ) | **None.** Imported verbatim. This is the substantive content and it is fully known (core C). |
| **Uniqueness** of the invariant form = dot product | Schur's lemma for irreducible reps; `SO(n)` has a 1-D space of invariant symmetric forms | **None.** Textbook. |
| **Orthogonality via skew generator** `B(Ju,v)+B(u,Jv)=0 ⇒ B(u,Ju)=0` | Skew-adjointness of the isometry Lie algebra (Noether/Riemannian geometry; https://profoundphysics.com/noethers-theorem-a-complete-guide/ ) | **Thin.** No write-up found that uses this *to prove the planar Pythagorean theorem*; but the fact "`so(2)` is skew w.r.t. the invariant metric" is standard and adaptable in one line. |
| **`J²=−I` from "two right-angle turns = central inversion"** | Elementary congruence geometry | **None.** Folklore. |
| **Overall route** | Project 1 (integral geometry) reached the same `Q(u+v)=Q(u)+Q(v)` via *reflection symmetry*; here via *Lie-algebra skewness* | **Thin/route-level.** Same destination, different last step. |

**Net:** at most a *route/exposition* delta on the orthogonality step. No new
foundation, no new decomposition, no weaker axiom set than known proofs.

---

## 2. Skeptical referee — "this is just core (C) in disguise"

**Referee's thesis.** *The proof is the ordinary inner-product proof. You assume
(P5): squared length is a rotation-invariant quadratic form. That assumption IS the
Pythagorean theorem (the metric comes from an inner product). Everything after is
the one-line expansion `‖u+v‖²=‖u‖²+2⟨u,v⟩+‖v‖²` with `⟨u,v⟩=0`. The "skew
generator" is just a fancy way to say `⟨u,Ju⟩=0`, which in coordinates is
`u·(−u_y,u_x)=0`, an immediate dot-product computation. Nothing here is new.*

**My honest answer.** **The referee is essentially right, and the proof's verdict
already concedes it (NOT NOVEL, core C).** Point by point:

- *"(P5) is the theorem."* Largely yes. (P5) carries the real content — that the
  measured metric is a rotation-invariant quadratic form. I do **not** prove (P5)
  here; I import it from Project 1 / the known integral-geometry construction, and I
  flag it explicitly as borrowed and non-novel. The proof is honestly a *reduction*
  of Pythagoras to (P5), not an independent derivation of the metric.

- *"the skew generator is just `⟨u,Ju⟩=0`."* Correct. Lemma 2 is exactly
  `B(u,Ju)=0`, which in the standard basis is the dot product `u·Ju=0`. The only
  defense is expository: Lemma 2 derives it from skew-adjointness + `J²=−I` *without*
  choosing coordinates or invoking `sin²+cos²=1`. That is a genuine (if minor)
  coordinate-free repackaging, not a new mathematical fact.

- *"so it's the inner-product proof."* Yes — core (C). The honest delta over the
  textbook inner-product proof is (a) the inner product is not *defined* by the
  coordinate formula but characterized as the invariant form, and (b) orthogonality
  is obtained from Lie-algebra skewness rather than a coordinate computation. Both
  are presentation choices. Neither is a new foundation.

**Can I answer the referee well enough to keep a novelty claim?** No — not a
*foundational* one. I therefore **downgrade** to the weakest honest claim:
"plausibly novel exposition/route for the orthogonality step, confidence LOW," and
lead the verdict with **NOT NOVEL**.

---

## 3. Why the negative result is the real deliverable

The prior-art gauntlet (`prior_art.md`) tested five non-exhausted-sounding
foundations and found:

- **C1 SO(2)-invariant form** → KNOWN (Schur, textbook);
- **C2 skew generator** → PARTIAL, route-only, trivially adaptable (chosen, capped);
- **C3 entropy power inequality** → KNOWN (reduces to variance additivity);
- **C4 information geometry** → KNOWN + circular (Euclidean is the base case);
- **C5 area functional equation** → KNOWN (core A; area-additivity is the hard part);
- plus **C6 tropical, C7 p-adic, C8 heat-kernel** killed for no-honest-meaning or
  circularity.

This is consistent, auditable evidence for the project's honest framing: in the
plane, essentially every correct proof reduces to (A) area, (B) similarity, or
(C) bilinearity+orthogonality, and the "fresh" foundations I could generate all
collapse onto (C) or are circular. The valuable, defensible output is therefore the
**documented map of why each candidate is not new**, not a manufactured novelty
claim.

**Confidence in the negative verdict:** MODERATE-HIGH for "no new foundation found";
the residual risk is only that some textbook presents the C2 skew-generator
packaging as folklore (which would harden, not soften, the negative verdict).
