---
layout: case
ref: bot-arena
lang: en
section: projects
order: 2
title: Bot Arena
eyebrow: "Personal project · Unity"
summary: "A horde shooter inspired by Call of Duty: Zombies — waves of enemies, three arenas, an in-game shop and a grenade rocket jump."
cover: "https://i.ytimg.com/vi/DEvdwnNBFe0/hqdefault.jpg"
cover_label: "Unity"
accent: teal
tags: [Shooter, Core loop, AI, "C#"]
role: "Solo developer"
engine: "Unity"
platform: "PC"
genre: "Wave-based horde shooter"
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

Build a complete, playable shooter on my own in Unity — from enemy AI and wave spawning to the economy that ties the session together.

## Core loop

Inspired by *Call of Duty: Zombies*: kill enemies, earn points, spend them on better equipment. Enemies attack in waves, and every wave is harder than the previous one.

{% include loop.html %}

## Features

- **Three arenas.** The player can teleport between them, but only between waves — a deliberate choice that makes the break between waves a planning moment.
- **Shops on every arena** — health regeneration, weapon upgrades and a unique weapon to buy.
- **Dash and grenade** with unlimited uses and short cooldowns, so movement and crowd control are always available.
- **Grenade rocket jump** — the grenade’s blast can launch the player, adding a movement skill to an offensive tool.
- **Enemy AI** with wave-based spawning.
