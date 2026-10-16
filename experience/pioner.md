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
  - { value: "~3,000", label: "loot spawners exported by my C++ parser" }
  - { value: "300+", label: "zones of the largest map in one pass" }
  - { value: "160+", label: "loot tables traced to every spawn point" }
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

## Tooling: loot parser {#loot-parser}

**Problem.** Loot in PIONER is placed through thousands of spawners scattered across the open world, each with its own spawn rules, respawn timers and loot tables. To answer a simple balance question — *how much of what does a player find in this area?* — a designer had to open spawners one by one in the editor. That doesn’t scale.

**Solution.** I wrote a **C++ tool that walks a level, reads every spawner and resolves its loot logic**, then exports one flat CSV. For each spawner it records:

- zone, spawner class and world coordinates;
- spawn rule (local unique / global) and respawn type and timers;
- every loot table it can roll, with weights and the **expected number of items**.

<div class="data-sample" markdown="0">
<p class="data-sample__title">Output format · names and values are anonymised</p>
<div class="data-sample__scroll"><table>
<thead><tr><th>Zone</th><th>Spawner</th><th>Respawn</th><th>Timer, s</th><th>Loot table</th><th>Weight</th><th>Expected items</th></tr></thead>
<tbody>
<tr><td>Zone_A</td><td>ItemSpawner_T2_07</td><td>After pickup</td><td>300</td><td>Misc_T2</td><td>5</td><td>6.7</td></tr>
<tr><td></td><td></td><td></td><td></td><td>Junk_Rare</td><td>1</td><td>1.3</td></tr>
<tr><td>Zone_B</td><td>Chest_Uncommon_03</td><td>Timer</td><td>600</td><td>Chest_Common_Weapon</td><td>15</td><td>0.15</td></tr>
<tr><td></td><td></td><td></td><td></td><td>Chest_Uncommon_Armor</td><td>25</td><td>0.25</td></tr>
</tbody></table></div>
</div>

**Result.** The loot of the game’s largest map became a spreadsheet: **about 3,000 spawners, 300+ zones and 160+ loot tables** in a single export. Loot can now be filtered, summed and compared by zone, tier or item category — and checked again after every change.

The first thing the export made visible was how unevenly loot is concentrated — a picture you simply can’t get by clicking through spawners in the editor:

{% include figure.html src="/assets/img/pioner/loot-concentration-en.webp" alt="Concentration curve: share of all loot on the map versus share of zones ranked by loot" caption="Built from the parser’s export for the largest map: zones ranked by expected loot. Around 10% of zones hold almost half of all loot — useful when deciding where to add, cut or move spawners." %}

## Balancing an open-world economy

In PIONER the core activities are exploring, completing quests and collecting loot. The player periodically breaks this out to repair and upgrade gear, sell loot and store it — and then heads back out. Every number in the game feeds this loop.

{% include loop.html %}

I balance a set of systems that all depend on each other:

- **Combat** — weapons, armor and enemy parameters, including bosses.
- **Progression** — experience curves and equipment progression.
- **Economy** — loot distribution, vendor pricing, crafting and overall resource flow.

A change in one place ripples through the others — for example, weapon damage affects time-to-kill, which affects ammo consumption and ultimately the player’s income. I work through balance spreadsheets, internal playtests and player feedback, and re-tune as live content ships.

Outside of production work, I also put together a sample sheet that balances one weapon category and shows formula approaches I like to use — TTK by distance and a hit-probability model based on spread area versus target size: {% include sample-link.html key="balance_sheet" label="weapon balance sample" %}. It is a showcase of methods, not live game data.

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
