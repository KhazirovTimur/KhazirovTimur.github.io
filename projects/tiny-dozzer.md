---
layout: case
ref: tiny-dozzer
lang: en
section: projects
order: 3
title: Tiny Dozzer
eyebrow: "Personal project · Unity · Mobile · 2021"
summary: "A casual mobile arcade game about a bulldozer that has to clear a platform of a cube structure before time runs out. Released on Google Play."
cover_label: "Mobile"
accent: green
tags: [Mobile, Arcade, Physics, Level design, Release]
role: "Solo developer"
engine: "Unity"
platform: "Android"
genre: "Arcade"
status: "Released on Google Play (since unpublished)"
stack: [Unity, "C#"]
youtube: "OZtPeIX7RAQ"
links: 
  - { label: "Full playthrough", url: "https://www.youtube.com/watch?v=OZtPeIX7RAQ" }
permalink: /projects/tiny-dozzer/
---

## About
The player drives a bulldozer with an on-screen joystick across a platform surrounded by a moat. Each level is a structure built from cubes, and every last cube has to go over the edge before the countdown ends. The HUD shows how much of the structure is already cleared and how many seconds are left. The run ends if time runs out, if the bulldozer falls into the moat, or if it is caught in a barrel explosion.

## Levels and progression
- 15 levels in three seasons of five: summer, autumn and winter.
- The seasons are mostly cosmetic, with one gameplay change: in winter the platform is icy, friction is lower, and pushed cubes slide further — which helps and hurts at the same time.
- Structures grow from small piles to a castle with walls, a maze and a multi-storey building; bigger levels get more time, from about a minute to two and a half.
- A few joke levels break the pattern: a single cube with red barrels set up like bowling pins, or a structure built as a copy of the player’s own bulldozer.

## Red barrels
Touching a red barrel lights a short fuse. The explosion throws every cube in its radius — a way to clear a big chunk at once, as long as you are not standing next to it. If the blast reaches the bulldozer, it is game over.

## Technical side
- **Accurate progress.** The level only counts as cleared at 100%, so the percentage has to be exact: every cube that leaves the platform is counted once, no matter how it got there — pushed, knocked off by other cubes or thrown by an explosion.
- **Physics tuning.** Mass, friction and the blade’s push were tuned so that structures collapse believably but stay controllable; winter levels reuse the same setup with lower friction.

## Why it matters
A small scope, but the full cycle on my own: idea, physics-based gameplay, 15 handmade levels, models and UI, polish, store page and release — in about a month.
