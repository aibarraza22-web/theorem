#!/usr/bin/env python3
"""
Exploration: generate Pythagorean-tiling overlay dissections for a right triangle
with legs a,b and find a clean, DISTINCTIVE (non-Perigal) cut pattern.

Construction (the Pythagorean tessellation):
  lattice Lambda = Z*p + Z*q,  p=(b,a), q=(-a,b)   (p,q orthogonal, |p|=|q|=c).
  Tiling motif (a fundamental domain of Lambda):
      B0 = big leg square  = [0,b] x [0,b]            (area b^2)
      S0 = small leg square= [b,b+a] x [0,a]          (area a^2)
  The c-square (hypotenuse square) is ALSO a fundamental domain:
      C(d) = parallelogram(square) with corners d, d+p, d+p+q, d+q,  offset d.

  Cutting C(d) by the tiling edges and translating each piece by a Lambda-vector
  reassembles B0 + S0. Every piece moves by a pure TRANSLATION (a lattice vector).

This script scans offsets d, counts pieces, and reports which squares get cut, so
we can choose a representative distinct from Perigal (Perigal = 5 pieces, only the
big square cut, small square whole).
"""
import itertools
from shapely.geometry import Polygon
from shapely.affinity import translate
from shapely.ops import unary_union


def lattice(a, b):
    p = (b, a)
    q = (-a, b)
    return p, q


def lam(p, q, m, n):
    return (m * p[0] + n * q[0], m * p[1] + n * q[1])


def big_square(b):
    return Polygon([(0, 0), (b, 0), (b, b), (0, b)])


def small_square(a, b):
    return Polygon([(b, 0), (b + a, 0), (b + a, a), (b, a)])


def c_square(d, p, q):
    dx, dy = d
    P = [(dx, dy),
         (dx + p[0], dy + p[1]),
         (dx + p[0] + q[0], dy + p[1] + q[1]),
         (dx + q[0], dy + q[1])]
    return Polygon(P)


def pieces_of(a, b, d, rng=4, eps=1e-9):
    """Return list of (piece_polygon, source, (m,n)) for c-square at offset d."""
    p, q = lattice(a, b)
    C = c_square(d, p, q)
    B0, S0 = big_square(b), small_square(a, b)
    out = []
    for m, n in itertools.product(range(-rng, rng + 1), repeat=2):
        v = lam(p, q, m, n)
        for src, base in (("big", B0), ("small", S0)):
            T = translate(base, xoff=v[0], yoff=v[1])
            inter = C.intersection(T)
            if inter.area > eps:
                # split multipolygons into parts
                geoms = getattr(inter, "geoms", [inter])
                for g in geoms:
                    if g.area > eps and g.geom_type == "Polygon":
                        out.append((g, src, (m, n)))
    return C, B0, S0, out


def verify(a, b, d, verbose=False):
    c2 = a * a + b * b
    C, B0, S0, parts = pieces_of(a, b, d)
    # (1) pieces partition C
    area_sum = sum(g.area for g, _, _ in parts)
    # pairwise overlap
    overlap = 0.0
    for i in range(len(parts)):
        for j in range(i + 1, len(parts)):
            overlap += parts[i][0].intersection(parts[j][0]).area
    # (2) reassemble: translate each piece by -Lambda(m,n)
    p, q = lattice(a, b)
    big_imgs, small_imgs = [], []
    for g, src, (m, n) in parts:
        v = lam(p, q, m, n)
        gg = translate(g, xoff=-v[0], yoff=-v[1])
        (big_imgs if src == "big" else small_imgs).append(gg)
    big_union = unary_union(big_imgs)
    small_union = unary_union(small_imgs)
    big_sym = big_union.symmetric_difference(B0).area
    small_sym = small_union.symmetric_difference(S0).area
    ncut_big = len(big_imgs)
    ncut_small = len(small_imgs)
    info = dict(
        npieces=len(parts), area_sum=area_sum, c2=c2, overlap=overlap,
        big_sym=big_sym, small_sym=small_sym,
        ncut_big=ncut_big, ncut_small=ncut_small,
    )
    ok = (abs(area_sum - c2) < 1e-7 and overlap < 1e-7
          and big_sym < 1e-7 and small_sym < 1e-7)
    info["ok"] = ok
    if verbose:
        print(info)
    return info


def main():
    a, b = 3.0, 4.0
    print(f"Scanning offsets for legs a={a}, b={b}, c=5  (Perigal=5 pieces, small square whole)\n")
    # scan a grid of offsets within one fundamental cell
    best = []
    for i in range(0, 12):
        for j in range(0, 12):
            d = (i * 0.5 - 1.0, j * 0.5 - 1.0)
            info = verify(a, b, d)
            if info["ok"]:
                best.append((info["npieces"], info["ncut_big"], info["ncut_small"], d))
    best.sort()
    seen = set()
    print("valid dissections found (npieces, big-pieces, small-pieces, offset):")
    for npc, nb, ns, d in best:
        key = (npc, nb, ns)
        if key in seen:
            continue
        seen.add(key)
        tag = ""
        if ns >= 2 and nb >= 2:
            tag = "  <-- BOTH squares cut (distinct from Perigal)"
        if npc == 5 and ns == 1:
            tag = "  <-- Perigal-like (5 pieces, small whole)"
        print(f"  n={npc:2d}  big={nb}  small={ns}  offset={({round(d[0],3),round(d[1],3)})}{tag}")


if __name__ == "__main__":
    main()
