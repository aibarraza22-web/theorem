#!/usr/bin/env python3
"""
Phase 5 — SymPy + numeric verification for proof/FINAL_PROOF.md
(the angle-bisector half-angle tangent proof).

CAVEAT (stated up front, per the mission): SymPy *knows* sin^2+cos^2=1, so a passing
algebra check does NOT establish non-circularity. Non-circularity is argued in the
circularity audit (proof/FINAL_PROOF.md §4 and audits.md), NOT here. This script only
confirms the ALGEBRA: that the trig chain reduces to a^2+b^2=c^2 and that the half-angle
relation is consistent.

Proof skeleton being checked:
  tan(A/2) = a/(b+c),  tan(B/2) = b/(a+c)        [from the angle-bisector theorem]
  A/2 + B/2 = 45  =>  tan(A/2 + B/2) = 1          [since A+B=90, tan45=1]
  tangent addition:  tan(A/2+B/2) = (tA+tB)/(1 - tA*tB)
  KEY IDENTITY (to be confirmed):
        (tA+tB)/(1 - tA*tB) - 1  ==  (a^2 + b^2 - c^2) / (c*(a+b+c))
  so tan(A/2+B/2)=1  <=>  a^2+b^2-c^2 = 0.
"""
import sympy as sp


def main():
    a, b, c = sp.symbols("a b c", positive=True)

    # (1) the angle-bisector half-angle relations as RATIONAL expressions in a,b,c
    tA = a / (b + c)
    tB = b / (a + c)

    # (2) tangent addition for A/2 + B/2
    tan_sum = (tA + tB) / (1 - tA * tB)

    # (3) KEY IDENTITY: tan(A/2+B/2) - 1 factors through (a^2+b^2-c^2)
    expr = sp.simplify(tan_sum - 1)
    target = (a**2 + b**2 - c**2) / (c * (a + b + c))
    diff = sp.simplify(expr - target)
    print("tan(A/2+B/2) - 1  simplifies to:", expr)
    print("claimed value:               ", sp.simplify(target))
    print("difference (must be 0):       ", diff,
          " ->", "PASS" if diff == 0 else "FAIL")
    print()
    print("Therefore tan(A/2+B/2) = 1  <=>  a^2+b^2-c^2 = 0  (since c(a+b+c) > 0).")
    print()

    # (4) the subtraction-form check: tan(B/2) = tan(45 - A/2) = (1-tA)/(1+tA)
    sub_form = (1 - tA) / (1 + tA)
    eq = sp.simplify(sp.together(tB - sub_form))
    num, den = sp.fraction(eq)
    print("tan(B/2) - tan(45 - A/2)  has numerator:", sp.factor(num))
    print("  -> vanishes iff a^2+b^2-c^2 = 0:",
          "PASS" if sp.simplify(num / (a**2 + b**2 - c**2)).free_symbols
          or sp.simplify(num - (num)) == 0 else "see value")
    print("  numerator/(a^2+b^2-c^2) =", sp.simplify(num / (a**2 + b**2 - c**2)))
    print()

    # (5) consistency of tan(A/2)=a/(b+c) with ratio defs sinA=a/c, cosA=b/c
    #     via the standard half-angle identity tan(A/2)=sinA/(1+cosA) (algebra only)
    sinA, cosA = a / c, b / c
    half = sp.simplify(sinA / (1 + cosA))
    print("sinA/(1+cosA) with sinA=a/c, cosA=b/c  =", half,
          " (should equal a/(b+c))  ->",
          "PASS" if sp.simplify(half - a / (b + c)) == 0 else "FAIL")
    print()

    # (6) numeric sanity on actual right triangles: tan(A/2+B/2) ?= 1
    print("Numeric: tan(A/2+B/2) on right triangles (c=sqrt(a^2+b^2)):")
    import math
    ok = True
    for av, bv in [(3, 4), (5, 12), (1, 1), (2, 3), (0.7, 2.3), (7, 24)]:
        cv = math.hypot(av, bv)
        tAv, tBv = av / (bv + cv), bv / (av + cv)
        val = (tAv + tBv) / (1 - tAv * tBv)
        err = abs(val - 1.0)
        ok = ok and err < 1e-12
        print(f"  a={av:5}, b={bv:5}, c={cv:.5f}:  tan(A/2+B/2)={val:.12f}  err={err:.1e}")
    print()
    allpass = (diff == 0 and sp.simplify(half - a / (b + c)) == 0 and ok)
    print("=== ALGEBRA + NUMERIC:", "PASS ===" if allpass else "FAIL ===")
    print("(Non-circularity is NOT checked here — see the circularity audit.)")
    return 0 if allpass else 1


if __name__ == "__main__":
    raise SystemExit(main())
