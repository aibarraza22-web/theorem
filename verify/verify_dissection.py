#!/usr/bin/env python3
"""
Phase 5 — self-contained rigorous verification of the candidate dissection in
proof/FINAL_PROOF.md (the "corner-anchored 5-piece translation dissection").

The pieces are given here by CLOSED-FORM coordinates in terms of (a,b), a<b
(NOT by tiling intersection), so this script independently checks the explicit
coordinates and isometries stated in the proof. For several (a,b), including
non-integer, it verifies:
  (S1) the 3 big-square pieces + 2 small-square pieces partition the two leg
       squares (areas sum to a^2+b^2; pairwise interior overlap 0; union == the
       two leg squares);
  (T1) applying each piece's translation lands it in the hypotenuse square, the
       5 images tile it (overlap 0; union == hyp square); and area sum == c^2;
  (C1) each translation maps the source vertex set exactly onto the target
       vertex set (vertex-set equality up to ordering).
It also emits verify/dissection.svg.

Pieces (source), a<b:
  x0 = (a^2 - a b + b^2)/b      x1 = (a^2 + b^2)/b = c^2/b
  BIG square  B0 = [0,b] x [0,b]:
    P0 quad (0,0),(0,b),(x0,b),(b,a)          translate (0,0)
    P1 tri  (0,0),(b,0),(b,a)                 translate (-a, b)
    P2 tri  (b,a),(x0,b),(b,b)                translate (-b,-a)
  SMALL square S0 = [b,b+a] x [0,a]:
    P3 quad (b,a),(b+a,a),(b+a,0),(x1,0)      translate (-(a+b), b-a)
    P4 tri  (x1,0),(b,0),(b,a)                translate (-a, b)
All isometries have rotation part = Identity  => motion type: TRANSLATION ONLY.
"""
from shapely.geometry import Polygon, MultiPolygon
from shapely.affinity import translate
from shapely.ops import unary_union


def build(a, b):
    x0 = (a * a - a * b + b * b) / b
    x1 = (a * a + b * b) / b
    pieces = [
        ("P0", "big", [(0, 0), (0, b), (x0, b), (b, a)], (0.0, 0.0)),
        ("P1", "big", [(0, 0), (b, 0), (b, a)], (-a, b)),
        ("P2", "big", [(b, a), (x0, b), (b, b)], (-b, -a)),
        ("P3", "small", [(b, a), (b + a, a), (b + a, 0), (x1, 0)], (-(a + b), b - a)),
        ("P4", "small", [(x1, 0), (b, 0), (b, a)], (-a, b)),
    ]
    return pieces


def vset(poly):
    return sorted((round(x, 9), round(y, 9)) for x, y in poly.exterior.coords[:-1])


def verify(a, b, eps=1e-9):
    assert a < b, "convention a < b"
    c2 = a * a + b * b
    B0 = Polygon([(0, 0), (b, 0), (b, b), (0, b)])
    S0 = Polygon([(b, 0), (b + a, 0), (b + a, a), (b, a)])
    C = Polygon([(0, 0), (b, a), (b - a, a + b), (-a, b)])  # hypotenuse square

    pieces = build(a, b)
    src_polys = [Polygon(v) for _, _, v, _ in pieces]
    tgt_polys = [translate(Polygon(v), xoff=t[0], yoff=t[1]) for _, _, v, t in pieces]

    res = {}
    # (S1) source areas + partition of leg squares
    res["src_area_sum"] = sum(p.area for p in src_polys)
    res["c2"] = c2
    res["src_overlap"] = sum(
        src_polys[i].intersection(src_polys[j]).area
        for i in range(5) for j in range(i + 1, 5))
    src_union = unary_union(src_polys)
    res["src_union_vs_legs"] = src_union.symmetric_difference(unary_union([B0, S0])).area

    # (T1) target tiling of hyp square
    res["tgt_area_sum"] = sum(p.area for p in tgt_polys)
    res["tgt_overlap"] = sum(
        tgt_polys[i].intersection(tgt_polys[j]).area
        for i in range(5) for j in range(i + 1, 5))
    tgt_union = unary_union(tgt_polys)
    res["tgt_union_vs_hyp"] = tgt_union.symmetric_difference(C).area

    # (C1) each translation maps source vertices exactly onto target vertices
    vmismatch = 0
    for (name, _, v, t), tp in zip(pieces, tgt_polys):
        moved = sorted((round(x + t[0], 9), round(y + t[1], 9)) for x, y in v)
        if moved != vset(tp):
            vmismatch += 1
    res["vertex_mismatches"] = vmismatch

    ok = (abs(res["src_area_sum"] - c2) < eps and abs(res["tgt_area_sum"] - c2) < eps
          and res["src_overlap"] < eps and res["tgt_overlap"] < eps
          and res["src_union_vs_legs"] < eps and res["tgt_union_vs_hyp"] < eps
          and vmismatch == 0)
    res["OK"] = ok
    return res, (B0, S0, C, pieces, src_polys, tgt_polys)


def emit_svg(a, b, path="dissection.svg"):
    _, (B0, S0, C, pieces, src_polys, tgt_polys) = verify(a, b)
    colors = ["#e6194B", "#3cb44b", "#4363d8", "#f58231", "#911eb4"]
    # layout: source config (left) and target config (right), shifted
    minx = -a - 1
    W = (b + a) - minx + 2
    shift = W + 2

    def poly_svg(pts, fill, dx=0.0):
        d = " ".join(f"{x+dx:.4f},{-y:.4f}" for x, y in pts)
        return (f'<polygon points="{d}" fill="{fill}" fill-opacity="0.65" '
                f'stroke="black" stroke-width="0.04"/>')

    parts = []
    # source: leg squares outline + colored pieces
    for sq in (B0, S0):
        parts.append(poly_svg(list(sq.exterior.coords[:-1]), "none"))
    for k, sp in enumerate(src_polys):
        parts.append(poly_svg(list(sp.exterior.coords[:-1]), colors[k]))
    # target: hyp square + colored translated pieces
    parts.append(poly_svg(list(C.exterior.coords[:-1]), "none", dx=shift))
    for k, tp in enumerate(tgt_polys):
        parts.append(poly_svg(list(tp.exterior.coords[:-1]), colors[k], dx=shift))

    height = (a + b) + 2
    vb_minx = minx - 1
    vb_miny = -(a + b) - 1
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" '
           f'viewBox="{vb_minx:.2f} {vb_miny:.2f} {2*shift:.2f} {height+2:.2f}">\n'
           f'<text x="{minx:.2f}" y="{1.2}" font-size="0.5">leg squares (a={a}, b={b})</text>\n'
           f'<text x="{minx+shift:.2f}" y="{1.2}" font-size="0.5">hypotenuse square (c^2=a^2+b^2)</text>\n'
           + "\n".join(parts) + "\n</svg>\n")
    with open(path, "w") as f:
        f.write(svg)
    return path


def main():
    print("=== Verification of the corner-anchored 5-piece translation dissection ===\n")
    cases = [(3.0, 4.0), (1.0, 2.0), (5.0, 12.0), (2.0, 3.0),
             (2.0 ** 0.5, 3.0), (0.7, 2.3), (1.0, 1.0000001)]
    allok = True
    for a, b in cases:
        res, _ = verify(a, b)
        allok = allok and res["OK"]
        print(f"a={a:8.4f} b={b:8.4f} c^2={res['c2']:.4f}: "
              f"src_sum={res['src_area_sum']:.6f} tgt_sum={res['tgt_area_sum']:.6f} "
              f"src_ovl={res['src_overlap']:.2e} tgt_ovl={res['tgt_overlap']:.2e} "
              f"src_uni_err={res['src_union_vs_legs']:.2e} tgt_uni_err={res['tgt_union_vs_hyp']:.2e} "
              f"vtx_mismatch={res['vertex_mismatches']}  -> {'PASS' if res['OK'] else 'FAIL'}")
    path = emit_svg(3.0, 4.0)
    print(f"\nSVG written: verify/{path}")
    print("\n=== OVERALL:", "PASS ===" if allok else "FAIL ===")
    return 0 if allok else 1


if __name__ == "__main__":
    raise SystemExit(main())
