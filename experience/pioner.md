---
layout: case
ref: pioner
lang: en
section: experience
order: 1
title: PIONER
eyebrow: "GFAGAMES · Unreal Engine · 2024 — now"
summary: "Open-world MMO shooter. I balance the game’s interconnected systems and economy, take new ideas from spec to release, and implement features in Blueprints."
cover: "https://cdn.cloudflare.steamstatic.com/steam/apps/3105890/header.jpg"
cover_label: "UE"
accent: orange
tags: [Blueprints, "C++", Tools, Balance, Economy]
role: "Game Designer (Balance / Technical)"
company: GFAGAMES
period: "Nov 2024 — Present"
engine: "Unreal Engine"
platform: "PC (Steam)"
genre: "Open-world MMO shooter"
status: "Released December 2025, live service"
links:
  - { label: "Steam page", url: "https://store.steampowered.com/app/3105890/PIONER/" }
highlights:
  - { value: "~3,000", label: "loot spawners exported by my C++ parser" }
  - { value: "~7 mo", label: "to rebalance the entire game with a colleague, down to every number" }
  - { value: "50+", label: "enemy types whose stats I calculated" }
stack: [Unreal Engine, Blueprints, "C++", Gameplay Tags, Enhanced Input, Data Tables, Primary Data Assets, Behavior Trees, Excel / Google Sheets, Jira, Confluence, Git]
loop:
  - { title: "Explore", text: "open world, quests, enemies" }
  - { title: "Loot", text: "weapons, gear, resources" }
  - { title: "Return to base", text: "repair, upgrade, craft" }
  - { title: "Trade & store", text: "vendors, stash" }
redirect_from:
  - /experience/pioner_balance/
  - /experience/pioner_weapon_balance/
chain:
  - { title: "Enemy lives longer", text: "more shots fired, more return fire" }
  - { title: "Wear", text: "weapons and armor lose durability; dying drains all gear" }
  - { title: "Repairs", text: "fixing gear costs more resources" }
  - { title: "Economy", text: "the player’s resource flow shifts" }
permalink: /experience/pioner/
---

## Overview

**PIONER** is an MMO first-person shooter set in an open post-apocalyptic world, with a full single-player campaign and a wide range of PvP and co-op PvE activities.

I joined the team in November 2024. The studio has about 70 people and 10 game designers, split roughly evenly between quests and balance / tech design. I’m in the second group, report to the lead game designer and lead two junior designers. I tune and balance almost every game system, work on new ideas, prototype and implement some of the mechanics, and build new tools for the team when needed.

## Balance and economy

In PIONER the core activities are exploring, completing quests and collecting loot. Every so often the player returns to base to repair and upgrade gear, sell loot and store it, then sets out on the next run. Every number in the game feeds this loop.

{% include loop.html %}

The game’s systems pull on each other: combat, progression, loot, crafting, the economy. A change in one place ripples through the others. Here is how raising an enemy’s health can affect the economy:

{% include chain.html label="Chain of effects" %}

### Open-world economy

The main goal is for this loop to feel good, with the player able to upgrade something in their gear after every run. We got there through iterations: adjust the numbers, playtest, adjust again. After updates we also watch player feedback: if players run short of a resource, such as rags, we tune it. Crafting is a big part of the economy on its own: the game has a huge number of recipes, every weapon and armor piece can be upgraded twice, from T1 to T3, plus countless consumables.

### Combat balance

PIONER has both PvP and PvE, so every weapon has to work in both and still feel distinct. For that I introduced a weapon power score calculated from effective TTK and effective DPS. It is the main reference but not the only one: I look at TTK and DPS on their own as well. This gives weapons a character:

<div class="power" markdown="0">
<p class="power__f"><b>Effective TTK</b> + <b>Effective DPS</b> → <b class="res">Power score</b></p>
<dl class="power__rows">
<div><dt>Heavy machine gun</dt><dd><span class="up">▲ PvE and bosses</span> thanks to high DPS · <span class="down">▼ PvP</span>: slow to aim down sights, reduced mobility</dd></div>
<div><dt>SMG with a small magazine</dt><dd><span class="up">▲ PvP</span>: high mobility and good TTK give an edge in PvP · <span class="down">▼ PvE</span>: the small magazine makes fights against many enemies harder</dd></div>
</dl>
</div>

These are tendencies, not hard rules: the machine gun is still viable in PvP.

After the math, every weapon goes through three checks: a PvE sandbox, the open world and internal PvP tests. If needed, I tune it afterwards.

Enemy parameters are mine too: I calculated damage, health, resistances and movement speed for 50+ enemy types, from regular mobs to bosses.

### Balance tables

I also maintain a large document with all the balance tables: many sheets for weapons, crafting, armor and resources, cross-linked throughout to keep manual work to a minimum and track every dependency and change. It is a key part of the team’s work: almost every game and level designer relies on it to some degree.

For this portfolio I put together a sample sheet that balances one weapon category with formulas I like to use: TTK by distance and hit probability from the ratio of spread area to target size. It shows the approach, not live game data.

{% include sample-link.html key="balance_sheet" label="Open the weapon balance sample" cls="btn" %}

**Result.** The target loop is in place: players progress steadily and keep upgrading their gear. When feedback pointed to a shortage or surplus of a resource, we fixed it quickly by adding new sources or new sinks, for example by rebalancing recipes. Opinions on weapons vary: some players call one gun the strongest, others another. For a shooter that is a good sign: there is no obvious best gun, and the balance works.

## Tooling: loot parser {#loot-parser}

**Problem.** Loot in PIONER is placed through thousands of spawners scattered across the open world, each with its own spawn rules, respawn timers and loot tables. To answer a simple balance question like *how much of what does a player find in this area?*, a designer had to open spawners one by one in the editor. At this project’s scale, that is practically impossible.

**Solution.** I wrote a **C++ tool that walks a level, reads every spawner and resolves its loot logic**, then exports one flat CSV. For each spawner it records:

- zone, spawner class and world coordinates;
- spawn and respawn rules and timers;
- every loot table it can roll, with weights and the **expected number of items**.

<div class="data-sample" markdown="0">
<p class="data-sample__title">Output format · names and values are anonymized</p>
<div class="data-sample__scroll"><table>
<thead><tr><th>Zone</th><th>Spawner</th><th>Respawn</th><th>Timer, s</th><th>Loot table</th><th>Weight</th><th>Expected items</th></tr></thead>
<tbody>
<tr><td>Zone_A</td><td>ItemSpawner_T2_07</td><td>After pickup</td><td>300</td><td>Misc_T2</td><td>5</td><td>6.7</td></tr>
<tr><td></td><td></td><td></td><td></td><td>Junk_Rare</td><td>1</td><td>1.3</td></tr>
<tr><td>Zone_B</td><td>Chest_Uncommon_03</td><td>Timer</td><td>600</td><td>Chest_Common_Weapon</td><td>15</td><td>0.15</td></tr>
<tr><td></td><td></td><td></td><td></td><td>Chest_Uncommon_Armor</td><td>25</td><td>0.25</td></tr>
</tbody></table></div>
</div>

**Result.** The loot of the game’s largest map became a spreadsheet: **about 3,000 spawners, 300+ zones and 160+ loot tables** in a single export. Loot can now be filtered, summed and compared by zone, tier or item category, and checked again after every change.

The first version took me a couple of evenings in my own time. Other designers in my department now use the export too, and level designers rely on it when they move loot around and clean up broken spawn points. It surfaced plenty of placement errors that would otherwise have to be found by hand.

Beyond raw numbers, the export makes it easy to build clear infographics, such as loot heatmaps. The map below shows loot concentrated around points of interest, with the most in the PvPvE zone. A map like this also exposes mistakes: areas with too little or too much loot.

{% include figure.html src="/assets/img/pioner/loot-heatmap-en.webp" alt="Heatmap of expected loot across the largest map of PIONER, built from the parser’s export" caption="Built from the parser’s export for the largest map: expected loot per map cell. Bright clusters are points of interest and the high-value PvPvE zone. Coordinates and values are left out." %}

## Hip-fire spread and an honest crosshair

**Problem.** The crosshair grew and shrank as the character moved, but hip-fire spread didn’t depend on movement at all: the player always fired with the same spread. The crosshair was a visual gimmick that told the player nothing.

**Solution.** I spotted this myself and took on the rework. Spread now depends on stance, movement speed and sustained fire, and it is tuned per weapon: all as is standard in arcade shooters. The crosshair reads the current spread and shows the actual area a bullet can land in.

**Result.** Hip-fire became a real decision: players see how accurate they are right now, and weapon classes handle differently. The change slotted into the game without issues.

## Readable grenade effects

**Problem.** The game has many grenade types, but their effects got in the way of reading combat. A technical issue let enemy silhouettes show through smoke. Thermite, incendiary and toxic grenades had blurry damage-zone edges that disappeared in tall grass, so players couldn’t tell where not to step.

**Solution.** I proposed fixing the effects to my lead and got the go-ahead. I set the requirements: lingering damage zones need clearly visible edges; effects must be bright enough not to get lost, without cluttering the screen. A junior designer turned them into a spec for the artists, and I oversaw how the finished art was accepted and integrated.

**Result.** Smoke hides again, and hazard zones read at a glance, even in grass. For me it’s an example of a task I ran through a junior designer: find the problem, get sign-off, delegate it and check the result.

## Content and technical work

- Create and tune weapons, armor, consumables and enemies using Data Tables and Primary Data Assets.
- Prototype new mechanics in Blueprints and iterate on them from update to update.
- Commission new content and the mechanics behind it from artists and programmers: write the specs and sign off the results.
- Before changing anything, dig into the project’s Behavior Trees and C++ systems to see how mechanics connect. Fix gameplay bugs in Blueprints.
- Reworked the perk system from scratch without breaking the systems around it.

## Team and mentoring

- Lead two junior designers: set their tasks, review their design documents, help them see their work through and share hands-on Unreal Engine experience.
- Together with a junior designer, reworked the clunky UX of the friends, chat and clan screens.
