---
layout: case
ref: bot-arena
lang: en
section: projects
order: 2
title: Bot Arena
eyebrow: "Personal project · Unity · 2023"
summary: "An arena shooter against endless waves of drones, inspired by Call of Duty: Zombies. Three arenas with shops and weapons, tunable enemy aggression and a wave system."
cover: "https://i.ytimg.com/vi/DEvdwnNBFe0/hqdefault.jpg"
cover_label: "Unity"
accent: teal
tags: [Shooter, Enemy AI, Wave design, "C#"]
role: "Solo developer"
engine: "Unity"
platform: "PC"
genre: "Arena shooter"
status: "Completed"
youtube: "DEvdwnNBFe0"
links:
  - { label: "Gameplay video", url: "https://www.youtube.com/watch?v=DEvdwnNBFe0" }
  - { label: "Source on GitHub", url: "https://github.com/KhazirovTimur/BotArena" }
stack: [Unity, "C#", NavMesh, ScriptableObjects]
loop:
  - { title: "Fight", text: "survive a wave of enemies" }
  - { title: "Earn", text: "get points for kills" }
  - { title: "Upgrade", text: "spend points in arena shops" }
  - { title: "Next wave", text: "each wave is harder" }
redirect_from:
  - /projects/bot_arena/
permalink: /projects/bot-arena/
---

## Goal
Build a complete, playable shooter on my own in Unity — enemy AI, waves, economy and weapons — in about a month. Most of the environment and weapon art comes from the Asset Store; the drone enemies, gameplay and code are mine.

## Core loop
Kill drones, pick up the cells they drop, spend them in the arena shops, survive the next, harder wave.

{% include loop.html %}

## Enemy AI: taking turns
An arena shooter becomes unreadable when every enemy shoots at once. Bot Arena has an aggression controller: only a limited number of drones may attack at the same time, the rest queue up. The queue is sorted by each drone’s attack strength and distance to the player, and a new drone gets permission no more often than once per second. The limit grows with every wave, so pressure rises without becoming unreadable.

Each drone runs a small state machine: spawn, chase, attack from a static position, death. Whether a drone chases or takes up a firing position is a chance set in a ScriptableObject config, so the mix of rushers and shooters is tuned without code. Ranged drones lead their shots: they predict where the player will be from the player’s speed and the projectile’s travel time.

## Waves and difficulty
Difficulty comes down to a handful of parameters. Every wave adds 5 enemies and 10% enemy health, allows one more drone alive at a time and raises the attacker limit by 0.2. Between waves there is a 15-second break; teleports between arenas work only during it, so the break becomes a planning moment.

## Arenas, shops and weapons
- **Three arenas**, each with its own shops: health restore, a 10% weapon damage upgrade and a weapon to buy.
- **Four weapons:** pistol, rifle, sniper rifle and shotgun. Shots are either instant raycasts or physical projectiles, with recoil per weapon; bullets and effects come from object pools.
- **Dash and grenade** with short cooldowns. The grenade’s blast can launch the player — a rocket jump that turns an attack into a movement skill.

## Where I’d take it next
The scaling only makes the same drones tougher and more numerous. A full game needs variety: new enemy types and elites whose share grows over time, the way Call of Duty: Zombies does it.
