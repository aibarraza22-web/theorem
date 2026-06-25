#!/usr/bin/env python3
"""
Numerical Monte-Carlo sanity backstop for proof/FINAL_PROOF.md.

Two independent checks:

  (A) Random right triangles satisfy a^2 + b^2 = c^2 to high precision.
      We build a right angle WITHOUT assuming the distance formula in the
      construction's logic: pick a vertex O, pick a leg direction, take the
      perpendicular direction (rotate by 90 degrees), place A and B, and measure
      side lengths with the Euclidean norm only at the END as the empirical
      'ruler'. (Coordinates here are a measuring device, not the proof.)

  (B) Monte-Carlo estimate of the projection-integral pairing
          B(u,v) = integral_0^{2pi} p_theta(u) p_theta(v) dtheta
      by sampling directions theta uniformly. We confirm
          B_hat(u,v)  ~  pi * (u . v)
      and in particular B_hat ~ 0 for perpendicular u, v. This is the numerical
      shadow of Lemmas 2 and 3.

Uses only the Python standard library (math, random) so it runs anywhere.
"""

import math
import random


def rot90(vx, vy):
    """Rotate a 2D vector by +90 degrees (a rigid motion; no distance formula)."""
    return (-vy, vx)


def norm(vx, vy):
    """Euclidean length used only as the empirical ruler at the end."""
    return math.hypot(vx, vy)


def check_random_right_triangles(trials=200_000, seed=12345):
    rng = random.Random(seed)
    worst = 0.0
    for _ in range(trials):
        # Right angle at O = origin. One leg along a random direction with random
        # positive length; the other leg along the perpendicular direction.
        ang = rng.uniform(0, 2 * math.pi)
        a = rng.uniform(1e-3, 1e3)
        b = rng.uniform(1e-3, 1e3)
        ex, ey = math.cos(ang), math.sin(ang)
        fx, fy = rot90(ex, ey)                 # perpendicular leg direction
        u = (a * ex, a * ey)                   # OA, length a
        v = (b * fx, b * fy)                   # OB, length b  (u perpendicular to v)
        A, B = u, v
        AB = (B[0] - A[0], B[1] - A[1])        # hypotenuse vector v - u
        a_meas = norm(*u)
        b_meas = norm(*v)
        c_meas = norm(*AB)
        rel = abs(a_meas**2 + b_meas**2 - c_meas**2) / (c_meas**2)
        worst = max(worst, rel)
    return worst


def estimate_B(u, v, samples=2_000_000, seed=999):
    """Monte-Carlo of B(u,v) = integral_0^{2pi} p_theta(u) p_theta(v) dtheta.

    With theta uniform on [0,2pi), the integral = 2pi * E[p_theta(u) p_theta(v)].
    p_theta(w) = w . (cos theta, sin theta).
    """
    rng = random.Random(seed)
    acc = 0.0
    for _ in range(samples):
        t = rng.uniform(0, 2 * math.pi)
        ct, st = math.cos(t), math.sin(t)
        pu = u[0] * ct + u[1] * st
        pv = v[0] * ct + v[1] * st
        acc += pu * pv
    return (2 * math.pi) * acc / samples


def main():
    print("=== (A) Random right triangles: a^2 + b^2 = c^2 ===")
    worst = check_random_right_triangles()
    print(f"max relative error over 200000 random right triangles: {worst:.3e}")
    okA = worst < 1e-12
    print("  ->", "PASS" if okA else "FAIL", "(threshold 1e-12)\n")

    print("=== (B) Monte-Carlo of the pairing B(u,v) ~ pi*(u.v) ===")
    cases = [
        ((3.0, 0.0), (0.0, 4.0), "perpendicular legs (u.v=0)"),
        ((1.0, 2.0), (3.0, 1.5), "generic, nonzero dot"),
        ((2.0, 1.0), (-1.0, 2.0), "another perpendicular pair (u.v=0)"),
    ]
    okB = True
    for u, v, label in cases:
        Bhat = estimate_B(u, v)
        dot = u[0] * v[0] + u[1] * v[1]
        target = math.pi * dot
        err = abs(Bhat - target)
        tol = 0.05 * (abs(target) + 1.0)   # MC tolerance, scales with magnitude
        good = err < tol
        okB = okB and good
        print(f"  {label:28s}: B_hat={Bhat:+.4f}  pi*(u.v)={target:+.4f} "
              f" (u.v={dot:+.2f})  ->  {'PASS' if good else 'FAIL'}")
    print()
    print("=== OVERALL:", "PASS ===" if (okA and okB) else "FAIL ===")
    return 0 if (okA and okB) else 1


if __name__ == "__main__":
    raise SystemExit(main())
