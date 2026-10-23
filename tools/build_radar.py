#!/usr/bin/env python3
"""Regenerate _includes/radar.html (the home page skill radar) from skills_list in _data/ui.yml.

Usage: python3 tools/build_radar.py
Works for any number of axes; the first skill sits at the top, the rest go clockwise.
"""
import math, os
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
C, R, LABEL_R = 210.0, 151.2, 169.2  # centre, radius of 10/10, radius of the labels


def pt(i, n, r):
    a = 2 * math.pi * i / n
    return C + r * math.sin(a), C - r * math.cos(a)


def svg(skills):
    n = len(skills)
    poly = lambda pts: " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    out = []
    for lvl in (2, 4, 6, 8, 10):
        out.append(f'<polygon class="ring" points="{poly(pt(i, n, R * lvl / 10) for i in range(n))}"/>')
    for i in range(n):
        x, y = pt(i, n, R)
        out.append(f'<line class="ax" x1="{C:.1f}" y1="{C:.1f}" x2="{x:.1f}" y2="{y:.1f}"/>')
    vals = [pt(i, n, R * s["v"] / 10) for i, s in enumerate(skills)]
    out.append(f'<g class="grow"><polygon class="shape" points="{poly(vals)}"/>')
    out += [f'<circle class="pt" cx="{x:.1f}" cy="{y:.1f}" r="5"/>' for x, y in vals]
    out.append("</g>")
    for i, s in enumerate(skills):
        x, y = pt(i, n, LABEL_R)
        dx = x - C
        anchor = "middle" if abs(dx) < 20 else ("start" if dx > 0 else "end")
        y -= 4
        if anchor == "middle":
            y += -22 if y < C else 22
        out.append(f'<text x="{x:.1f}" y="{y:.1f}" text-anchor="{anchor}">{s["name"]}</text>'
                   f'<text class="v" x="{x:.1f}" y="{y + 20:.1f}" text-anchor="{anchor}">{s["v"]}/10</text>')
    label = ", ".join(f'{s["name"]} {s["v"]} of 10' for s in skills)
    return (f'<svg class="radar" viewBox="-110 -20 640 460" role="img" aria-label="Skill radar: {label}">'
            + "".join(out) + "</svg>")


def main():
    with open(os.path.join(ROOT, "_data/ui.yml"), encoding="utf-8") as f:
        ui = yaml.safe_load(f)
    html = ('{%- if include.lang == "ru" -%}' + svg(ui["ru"]["skills_list"]) + "{%- else -%}"
            + svg(ui["en"]["skills_list"]) + "{%- endif -%}")
    with open(os.path.join(ROOT, "_includes/radar.html"), "w", encoding="utf-8") as f:
        f.write(html)


if __name__ == "__main__":
    main()
