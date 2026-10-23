---
layout: case
ref: pioner
lang: en
section: experience
order: 1
title: PIONER
eyebrow: "GFAGAMES · Unreal Engine 5 · 2024 — now"
summary: "Open-world MMO shooter. I implement features directly in Blueprints, build tools for the team, balance the game’s interconnected systems and own weapon mechanics from spec to release."
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
status: "Released December 2025, live service"
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

**PIONER** is an MMO first-person shooter set in an open post-apocalyptic world, with a single-player storyline, PvE and PvP activities, raids and survival elements.

I joined the team in November 2024. The studio has about 70 people and 10 game designers, split roughly evenly between quest design and balance / technical design. I’m in the second group, report to the lead game designer and lead two junior designers. I implement features directly in the engine, build tools for the team, keep interconnected systems in balance and own new mechanics.

## Content and technical work

- Create and tune weapons, armor, consumables and enemies using Data Tables and Primary Data Assets.
- Calculated stats for dozens of enemies, from regular mobs to bosses: damage, health, resistances and movement speed.
- Prototype new mechanics in Blueprints and iterate on them from update to update.
- Before changing anything, dig into the project’s Behavior Trees and C++ systems to see how mechanics connect; fix gameplay bugs in Blueprints.

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

The first version took me a couple of evenings in my own time. Other designers in my department now use the export too, and level designers rely on it when they move loot around and clean up broken spawn points. It surfaced plenty of placement errors that would otherwise have to be found by hand, one spawner at a time.

The first thing the export gave was a picture of the whole map at once. Loot is meant to be uneven: it gathers around points of interest, and the most valuable loot sits in a large PvPvE zone. The heatmap makes it easy to check that the map actually works that way — and to spot areas that are empty or overloaded by mistake:

{% include figure.html src="/assets/img/pioner/loot-heatmap-en.webp" alt="Heatmap of expected loot across the largest map of PIONER, built from the parser’s export" caption="Built from the parser’s export for the largest map: expected loot per map cell. Bright clusters are points of interest and the high-value PvPvE zone. Coordinates and values are left out." %}

## Balancing an open-world economy

In PIONER the core activities are exploring, completing quests and collecting loot. Every so often the player returns to base to repair and upgrade gear, sell loot and store it — and then heads back out. Every number in the game feeds this loop.

{% include loop.html %}

I balance a set of systems that all depend on each other:

- **Combat** — weapons, armor and enemy parameters, including bosses.
- **Progression** — experience curves and equipment progression.
- **Economy** — loot distribution, vendor pricing, crafting and overall resource flow.

A change in one place ripples through the others — for example, weapon damage affects time-to-kill, which affects ammo consumption and ultimately the player’s income. I work through balance spreadsheets, internal playtests and player feedback, and re-tune as live content ships.

Outside of production work, I also put together a sample sheet that balances one weapon category and shows formula approaches I like to use — TTK by distance and a hit-probability model based on spread area versus target size: {% include sample-link.html key="balance_sheet" label="weapon balance sample" %}. It is a showcase of methods, not live game data.

## Hip-fire spread and an honest crosshair

**Problem.** The crosshair grew and shrank as the character moved, but hip-fire spread didn’t depend on movement at all: the player always fired with the same spread. The crosshair was a visual gimmick that told the player nothing.

**Solution.** I spotted this myself and took on the rework. Spread now depends on stance, movement speed and sustained fire, tuned per weapon, as is standard in arcade shooters. The crosshair reads the current spread and shows the actual area a bullet can land in.

**Result.** Hip-fire became a real decision: players see how accurate they are right now, and weapon classes handle differently. The change slotted into the game without issues.

## Readable grenade effects

**Problem.** The game has many grenade types, but their effects got in the way of reading combat. A technical issue let enemy silhouettes show through smoke. Thermite, incendiary and toxic grenades had blurry damage-zone edges that disappeared in tall grass, so players couldn’t tell where not to step.

**Solution.** I proposed fixing the effects to my lead and got the go-ahead. I set the requirements: lingering damage zones need clearly visible edges; effects must be bright enough not to get lost, without cluttering the screen. A junior designer turned them into a spec for the artists, and I oversaw how the finished effects were accepted and integrated.

**Result.** Smoke hides again, and hazard zones read at a glance, even in grass. For me it’s an example of a task I ran through a junior designer: find the problem, get sign-off, delegate it and check the result.

## Features I owned end-to-end

Each of these went the full path — design spec, implementation directly in Blueprints, tuning, and integration into the existing systems without breaking anything that already worked.

- **Automatic reload** — players kept forgetting to reload, because other shooters had taught them to expect auto-reload. I added it to the existing weapon logic.
- **Perk system rework** — a full redesign and re-implementation of the existing perk system, rolled out while keeping the rest of the game fully functional.

## Team and mentoring

- Lead two junior designers: set their tasks, review their design documents, help them own features and share hands-on Unreal Engine experience.
- Write and maintain balance tables and feature specs for engineers, artists and QA.
- Together with a junior designer, reworked the clunky UX of the friends, chat and clan screens.
