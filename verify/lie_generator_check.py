#!/usr/bin/env python3
"""
Verification for proof/FINAL_PROOF.md (Project 2): the "skew infinitesimal
generator" route.

Core claims to check:
  J is the 90-degree rotation generator, with J^2 = -I  (two right-angle turns
  = central inversion -- a geometric fact, not Pythagoras).

  Let B be a symmetric bilinear form that is INVARIANT under the rotation group,
  equivalently J is SKEW w.r.t. B:  B(Ju, v) + B(u, Jv) = 0  for all u, v.

  Then:
    (1) B(u, Ju) = 0           [cross term vanishes: orthogonality for free]
    (2) for v = lambda * J u (i.e. v perpendicular to u, length |lambda|*|u|),
        Q(u + v) = Q(u) + Q(v) where Q(x) = B(x,x).   [Pythagoras]

We verify symbolically that (1) and (2) follow from skew-invariance ALONE
(without ever writing B as the coordinate dot product), and separately confirm
that the unique-up-to-scale positive-definite skew-invariant B is the standard
inner product (so Q = c0 * L^2), which is the textbook content the proof leans on.
"""

import sympy as sp


def main():
    print("=== (1)-(2): consequences of skew-invariance ALONE (B abstract) ===\n")
    # Abstract symmetric bilinear form B with entries; impose skew-invariance.
    b11, b12, b22 = sp.symbols("b11 b12 b22", real=True)
    B = sp.Matrix([[b11, b12], [b12, b22]])          # symmetric, abstract
    J = sp.Matrix([[0, -1], [1, 0]])                 # 90-degree generator

    # Skew-invariance condition  B J + (B J)^T = 0  <=>  J^T B + B J = 0 ... we use
    # the bilinear-form convention  Bil(x,y) = x^T B y , skew means  J^T B + B J = 0.
    skew = J.T * B + B * J
    print("Skew-invariance J^T B + B J =\n", skew)
    sol = sp.solve([skew[0, 0], skew[0, 1], skew[1, 0], skew[1, 1]],
                   [b12, b22], dict=True)
    print("Solving skew-invariance for the form entries:", sol)
    # Expect b12 = 0, b22 = b11  -> B = b11 * I  (a scalar multiple of identity).
    assert sol, "no solution found"
    s = sol[0]
    B_inv = B.subs(s)
    print("=> invariant B =\n", B_inv, " (a positive multiple of the identity)\n")

    # Now check (1) and (2) using ONLY that B is skew-invariant (symbolic b11>0).
    ux, uy = sp.symbols("ux uy", real=True)
    u = sp.Matrix([ux, uy])
    Ju = J * u

    def bil(x, y):
        return (x.T * B_inv * y)[0]

    def Q(x):
        return bil(x, x)

    cross = sp.simplify(bil(u, Ju))
    print("(1) B(u, Ju) =", cross, " -> ", "PASS" if cross == 0 else "FAIL")

    lam = sp.symbols("lambda", real=True)
    v = lam * Ju                      # v perpendicular to u (v = lambda * J u)
    lhs = sp.simplify(Q(u + v))
    rhs = sp.simplify(Q(u) + Q(v))
    diff = sp.simplify(lhs - rhs)
    print("(2) Q(u+v) - [Q(u)+Q(v)] for v=lambda*Ju:", diff,
          " -> ", "PASS" if diff == 0 else "FAIL")
    print("    Q(u+v) =", lhs, "   Q(u)+Q(v) =", rhs)
    print()

    print("=== (3) the invariant form IS the dot product (the textbook fact) ===")
    # B_inv = b11 * Identity, so Q(x) = b11*(ux^2+uy^2) = c0 * L(x)^2 with c0=b11.
    Qgen = sp.simplify(Q(u))
    print("Q(u) =", Qgen, "= b11*(ux^2+uy^2)  => c0 = b11 > 0, Q = c0 * L^2.")
    print("This is precisely the Schur/representation-theory uniqueness of the")
    print("SO(2)-invariant symmetric form: it forced B proportional to identity.")
    print()

    print("=== (4) numerical sanity on random right triangles ===")
    import random
    rng = random.Random(2026)
    worst = 0.0
    Jn = [[0.0, -1.0], [1.0, 0.0]]
    for _ in range(100_000):
        uxn, uyn = rng.uniform(-1e3, 1e3), rng.uniform(-1e3, 1e3)
        lamn = rng.uniform(-1e3, 1e3)
        # v = lambda * J u  (perpendicular leg); Q = standard squared length
        vxn = lamn * (Jn[0][0] * uxn + Jn[0][1] * uyn)
        vyn = lamn * (Jn[1][0] * uxn + Jn[1][1] * uyn)
        Qu = uxn**2 + uyn**2
        Qv = vxn**2 + vyn**2
        Quv = (uxn + vxn) ** 2 + (uyn + vyn) ** 2
        denom = Quv if Quv != 0 else 1.0
        rel = abs(Quv - (Qu + Qv)) / denom
        worst = max(worst, rel)
    print(f"max relative error of Q(u+v) - (Q(u)+Q(v)) over 100000 instances: {worst:.3e}")
    okn = worst < 1e-12
    print("  ->", "PASS" if okn else "FAIL", "(threshold 1e-12)\n")

    ok = (cross == 0) and (diff == 0) and okn
    print("=== SKEW-GENERATOR CHECKS:", "PASS ===" if ok else "FAIL ===")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
