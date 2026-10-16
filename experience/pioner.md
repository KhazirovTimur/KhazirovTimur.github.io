---
layout: case
ref: pioner
lang: en
section: experience
order: 1
title: PIONER
eyebrow: "GFAGAMES · Unreal Engine 5 · 2024 — now"
summary: "Open-world multiplayer survival shooter. I implement features directly in Blueprints, build tools for the team, balance the game’s interconnected systems and own weapon mechanics from spec to release."
cover: "https://cdn.cloudflare.steamstatic.com/steam/apps/3105890/header.jpg"
cover_label: "UE5"
accent: orange
tags: [Blueprints, "C++", Tools, Balance, Economy]
role: "Game Designer (Balance / Technical)"
company: GFAGAMES
period: "Nov 2024 — Present"
engine: "Unreal Engine 5"
platform: "PC (Steam)"
genre: "Open-world MMO shooter"
status: "Released, live"
links:
  - { label: "Steam page", url: "https://store.steampowered.com/app/3105890/PIONER/" }
highlights:
  - { value: "7", label: "interconnected systems under my balance" }
  - { value: "C++", label: "loot parser tool built for the team" }
stack: [Unreal Engine 5, Blueprints, "C++", Gameplay Tags, Enhanced Input, Data Tables, Primary Data Assets, Behavior Trees, Excel / Google Sheets, Jira, Confluence, Git]
loop:
  - { title: "Explore", text: "open world, quests, enemies" }
  - { title: "Loot", text: "weapons, gear, resources" }
  - { title: "Return to base", text: "repair, upgrade, craft" }
  - { title: "Trade & store", text: "vendors, stash" }
redirect_from:
  - /experience/pioner_balance/
  - /experience/pioner_weapon_balance/
permalink: /experience/pioner/
---

## Overview

**PIONER** is a multiplayer first-person shooter set in an open post-apocalyptic world, with a single-player storyline, PvE and PvP activities, raids and survival elements.

I joined the team in November 2024 as a game designer focused on balance and technical design. My work combines hands-on implementation in the engine, tools that speed up production, balancing the game’s interconnected systems and owning new gameplay mechanics.

## Content and technical work

- Created and tuned weapons, armor, consumables and enemies using Data Tables and Primary Data Assets.
- Prototyped and iterated on new mechanics in Blueprints as ongoing live content.
- Worked inside existing Behavior Trees and C++ systems to understand how mechanics interact before changing them, and fixed gameplay issues via Blueprints.

## Tooling: loot parser

Checking loot distribution manually in the editor doesn’t scale for an open world. I wrote a **C++ tool that parses the loot logic and exports spawn-point data to CSV**, so loot can be reviewed and balanced in spreadsheets across the whole map at once.

## Balancing an open-world economy

In PIONER the core activities are exploring, completing quests and collecting loot. The player periodically breaks this out to repair and upgrade gear, sell loot and store it — and then heads back out. Every number in the game feeds this loop.

{% include loop.html %}

I balance a set of systems that all depend on each other:

- **Combat** — weapons, armor and enemy parameters, including bosses.
- **Progression** — experience curves and equipment progression.
- **Economy** — loot distribution, vendor pricing, crafting and overall resource flow.

A change in one place ripples through the others — for example, weapon damage affects time-to-kill, which affects ammo consumption and ultimately the player’s income. I work through balance spreadsheets, internal playtests and player feedback, and re-tune as live content ships.

## Features I owned end-to-end

Each of these went the full path — design spec, implementation directly in Blueprints, tuning, and integration into the existing systems without breaking anything that already worked.

- **Hip-fire spread system** — turned hip-fire accuracy into a per-weapon, tunable parameter, so every weapon class has its own handling and aiming down sights remains a meaningful choice.
- **Dynamic crosshair** — a crosshair that reflects the current spread, so the player reads weapon accuracy at a glance.
- **Automatic reload** — reload behaviour integrated into the existing weapon logic.
- **Perk system rework** — a full redesign and re-implementation of the existing perk system, rolled out while keeping the rest of the game fully functional.

## Team and mentoring

- Mentored junior designers: reviewed their design documents, helped them own features and shared hands-on Unreal Engine experience.
- Wrote and maintained balance tables and feature specs for engineers, artists and QA.
- Supported social systems and the social interface.
