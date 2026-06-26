#!/usr/bin/env python3
"""Inspect the offset=(0,0) candidate in detail and test generality over (a,b)."""
from explore import verify, pieces_of, lattice, lam
from shapely.affinity import translate


def dump(a, b, d=(0.0, 0.0)):
    C, B0, S0, parts = pieces_of(a, b, d)
    p, q = lattice(a, b)
    print(f"--- legs a={a}, b={b}, c^2={a*a+b*b} ; c-square corners "
          f"(0,0),{p},{(p[0]+q[0],p[1]+q[1])},{q} ---")
    for k, (g, src, (m, n)) in enumerate(sorted(parts, key=lambda t: (t[1], -t[0].area))):
        v = lam(p, q, m, n)
        coords = [(round(x, 4), round(y, 4)) for x, y in g.exterior.coords[:-1]]
        print(f"  piece {k}: src={src:5s} area={g.area:8.4f}  "
              f"translate by -Lambda{(m,n)} = ({-v[0]},{-v[1]})  verts={coords}")
    info = verify(a, b, d)
    print("  verify:", {k: (round(val, 10) if isinstance(val, float) else val)
                         for k, val in info.items()})
    return info


def main():
    print("=== Detailed pieces for the canonical offset d=(0,0), a=3,b=4 ===")
    dump(3.0, 4.0)
    print()
    print("=== Generality test: piece count / validity across many (a,b) at d=(0,0) ===")
    cases = [(3.0, 4.0), (1.0, 2.0), (5.0, 12.0), (2.0, 3.0),
             (2.0 ** 0.5, 3.0), (1.0, 1.0), (1.0, 3.0), (4.0, 5.0), (0.7, 2.3)]
    for a, b in cases:
        info = verify(a, b, (0.0, 0.0))
        print(f"  a={a:7.4f} b={b:7.4f}: pieces={info['npieces']} "
              f"(big={info['ncut_big']}, small={info['ncut_small']})  ok={info['ok']}")


if __name__ == "__main__":
    main()
