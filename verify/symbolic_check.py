#!/usr/bin/env python3
"""
Symbolic verification (SymPy) for the integral-geometry proof in
proof/FINAL_PROOF.md.

The proof NEVER uses coordinates; this script introduces coordinates ONLY to
verify that the abstractly-constructed pairing

        B(u, v) = integral_0^{2pi} p_theta(u) p_theta(v) d_theta

equals  pi * (standard Euclidean inner product of u and v).

In coordinates, with e_theta = (cos theta, sin theta), the signed projection of
a vector u = (ux, uy) is

        p_theta(u) = u . e_theta = ux cos theta + uy sin theta.

We confirm:
  (1)  B(u, v) = pi * (ux*vx + uy*vy)          -> B = pi * <u,v>_Euclid
  (2)  Q(u) = B(u, u) = pi * (ux^2 + uy^2)     -> Q = pi * L(u)^2  (Lemma 2, c0 = pi)
  (3)  u . v = 0  =>  B(u, v) = 0              (Lemma 3, orthogonality)
  (4)  Polarization: Q(u+v) - 2 B(u,v) - Q(u) - Q(v) == 0   (the identity (star))
  (5)  The Pythagorean conclusion at the symbolic level:
       with u . v = 0,  Q(v - u) == Q(u) + Q(v).

None of this is the proof; it is a machine check that the proof's objects behave
as claimed.
"""

import sympy as sp


def main():
    theta = sp.symbols("theta", real=True)
    ux, uy, vx, vy = sp.symbols("ux uy vx vy", real=True)

    e = sp.Matrix([sp.cos(theta), sp.sin(theta)])
    u = sp.Matrix([ux, uy])
    v = sp.Matrix([vx, vy])

    p_u = (u.T * e)[0]              # signed projection p_theta(u)
    p_v = (v.T * e)[0]              # signed projection p_theta(v)

    def integrate_full_circle(expr):
        return sp.integrate(expr, (theta, 0, 2 * sp.pi))

    B = sp.simplify(integrate_full_circle(p_u * p_v))
    Qu = sp.simplify(integrate_full_circle(p_u**2))
    Qv = sp.simplify(integrate_full_circle(p_v**2))

    dot = ux * vx + uy * vy
    Lu2 = ux**2 + uy**2
    Lv2 = vx**2 + vy**2

    print("=== Symbolic check of the projection-integral pairing ===\n")

    print("B(u,v) = integral_0^{2pi} p_theta(u) p_theta(v) dtheta")
    print("       =", B)
    check1 = sp.simplify(B - sp.pi * dot)
    print("B(u,v) - pi*(u.v) =", check1, " -> ", "PASS" if check1 == 0 else "FAIL")
    print()

    print("Q(u) = B(u,u) =", Qu)
    check2 = sp.simplify(Qu - sp.pi * Lu2)
    print("Q(u) - pi*L(u)^2 =", check2, " -> ", "PASS" if check2 == 0 else "FAIL")
    print("  => constant c0 in Lemma 2 equals pi (value never used in the proof).")
    print()

    # (3) Orthogonality: substitute a concrete perpendicular pair u=(a,0), v=(0,b)
    a, b = sp.symbols("a b", positive=True)
    B_perp = B.subs({ux: a, uy: 0, vx: 0, vy: b})
    B_perp = sp.simplify(B_perp)
    print("Orthogonality (Lemma 3): for u=(a,0), v=(0,b) [u.v=0],")
    print("B(u,v) =", B_perp, " -> ", "PASS" if B_perp == 0 else "FAIL")
    print()

    # (4) Polarization identity (star)
    Quv = integrate_full_circle((p_u + p_v) ** 2)
    pol = sp.simplify(Quv - (Qu + 2 * B + Qv))
    print("Polarization Q(u+v) - [Q(u) + 2B(u,v) + Q(v)] =", pol,
          " -> ", "PASS" if pol == 0 else "FAIL")
    print()

    # (5) Pythagoras at the symbolic level for a perpendicular pair
    sub = {ux: a, uy: 0, vx: 0, vy: b}
    p_u_s = p_u.subs(sub)
    p_v_s = p_v.subs(sub)
    Q_vmu = sp.simplify(integrate_full_circle((p_v_s - p_u_s) ** 2))   # Q(v-u) = c0 c^2
    Q_u_s = sp.simplify(integrate_full_circle(p_u_s**2))
    Q_v_s = sp.simplify(integrate_full_circle(p_v_s**2))
    lhs = sp.simplify(Q_vmu)            # = pi * c^2
    rhs = sp.simplify(Q_u_s + Q_v_s)    # = pi * (a^2 + b^2)
    print("Pythagoras via the functional (u=(a,0), v=(0,b)):")
    print("  Q(v-u) =", lhs, "  (= pi * c^2)")
    print("  Q(u)+Q(v) =", rhs, "  (= pi * (a^2 + b^2))")
    final = sp.simplify(lhs - rhs)
    print("  Q(v-u) - [Q(u)+Q(v)] =", final, " -> ", "PASS" if final == 0 else "FAIL")
    print("  Dividing by c0=pi:  c^2 = a^2 + b^2.")
    print()

    all_pass = all(x == 0 for x in [check1, check2, B_perp, pol, final])
    print("=== ALL SYMBOLIC CHECKS:", "PASS ===" if all_pass else "FAIL ===")
    return 0 if all_pass else 1


if __name__ == "__main__":
    raise SystemExit(main())
