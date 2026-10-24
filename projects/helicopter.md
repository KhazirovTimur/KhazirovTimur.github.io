---
layout: case
ref: helicopter
lang: en
section: projects
order: 1
title: Helicopter Prototype
eyebrow: "Personal project · Unreal Engine 5 · 2025"
summary: "A physics-based helicopter flight model built from real aerodynamic formulas, plus a nose turret that tracks where the camera looks — C++ core, Blueprint content."
cover_label: "UE5"
accent: orange
tags: [Vehicles, Physics, "C++", Blueprints]
role: "Solo developer"
engine: "Unreal Engine 5"
platform: "PC"
genre: "Vehicle / flight prototype"
status: "Completed"
stack: [Unreal Engine 5, "C++", Blueprints, Enhanced Input]
youtube: "_W8JCll1D7o"
links: 
  - { label: "Flight video", url: "https://www.youtube.com/watch?v=_W8JCll1D7o" }
permalink: /projects/helicopter/
---

## About the prototype
The goal was a believable helicopter flight model and a nose gun turret for it. The prototype is deliberately narrow: no sound, interface or level art, only flight and shooting. The goal was reached, so the prototype is complete.

All code and classes are my own. The AH-64 model comes from the Vigilante asset pack, the map is Unreal’s default landscape.

What it demonstrates:
- translating real-world physics into tunable gameplay parameters;
- knowing what to simplify: dropping rotor torque kept the controls readable without losing the helicopter feel;
- a C++ core with Blueprint content, the setup designers work with on real projects.

## Flight model and controls
A simplified simulation of real helicopter physics rather than an arcade “floating camera”. Rotor thrust, lift and drag are computed from real formulas.

<div class="data-sample data-sample--fit" markdown="0">
<p class="data-sample__title">Flight model parameters</p>
<div class="data-sample__scroll"><table>
<thead><tr><th>Parameter</th><th>How it works</th></tr></thead>
<tbody>
<tr><td>Mass</td><td>Tunable</td></tr>
<tr><td>Rotor thrust</td><td>Tunable</td></tr>
<tr><td>Rotor drag</td><td>Tunable</td></tr>
<tr><td>Body drag</td><td>Separate coefficients for the front, side and vertical axes</td></tr>
<tr><td>Air temperature and pressure</td><td>Constants, which keeps the model stable and tunable</td></tr>
<tr><td>Main rotor reactive torque</td><td>Left out to keep the controls readable</td></tr>
</tbody></table></div>
</div>

WASD for pitch and roll, Q/E for yaw, Shift/Ctrl for altitude, mouse for the camera. There is no stability assist: the player flies the machine. Pull the nose up at speed and the helicopter climbs on its own; build up sideways speed and it turns into the direction of travel. None of this is scripted, it emerges from the formulas.

## Turret
Hold the right mouse button to free the camera; the turret tries to aim at the point the camera is looking at. It has realistic limits: ±90° horizontally and −30°/+10° vertically. Shots are physical projectiles with travel time, not instant hits.

## Architecture
Base classes are in C++: the helicopter with its flight model and the turret. A specific machine is a Blueprint on top: the AH-64 and its turret only set their own characteristics. A new helicopter or turret is a data change, not new code.
