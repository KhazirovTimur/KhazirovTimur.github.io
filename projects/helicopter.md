---
layout: case
ref: helicopter
lang: en
section: projects
order: 1
title: Helicopter Prototype
eyebrow: "Personal project · Unreal Engine 5 · 2025 — now"
summary: "A physics-based helicopter flight model built from real aerodynamic formulas, plus a gimbal-mounted gun turret — in Blueprints and C++."
cover_label: "UE5"
accent: orange
tags: [Vehicles, Physics, "C++", Blueprints]
role: "Solo developer"
engine: "Unreal Engine 5"
platform: "PC"
genre: "Vehicle / flight prototype"
status: "In progress"
stack: [Unreal Engine 5, "C++", Blueprints, Enhanced Input]
permalink: /projects/helicopter/
---

## Goal

Build a believable helicopter flight model and a gimbal-mounted gun turret — a prototype for vehicle gameplay and control tuning.

## Flight model

I wanted a simplified simulation of real helicopter physics rather than an arcade “floating camera”. The model is based on real formulas for **lift, torque and drag**. Atmospheric variables such as temperature and air pressure are treated as constants, which keeps the model stable and tunable while preserving the characteristic behaviour of a helicopter.

## Controls and feel

Controls are standard: WASD for pitch and roll, Q/E for yaw, Shift/Ctrl for altitude. There is no stability assist — the player flies the machine. Most of my attention went into believability: pull the nose up at high speed and the helicopter climbs on its own; build up sideways speed and it turns into the direction of travel. None of this is scripted — it emerges from the formulas.

## Turret

A gimbal-mounted gun turret with its own weapon system, aimed independently of the helicopter’s heading.

## What it demonstrates

- Translating real-world physics into tunable gameplay parameters.
- Vehicle and locomotion prototyping.
- Combining C++ for core logic with Blueprints for fast iteration.
