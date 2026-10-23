---
layout: case
ref: the-braves
lang: en
section: experience
order: 2
title: The Braves
eyebrow: "101XP · Unity · 2023 — 2024"
summary: "Live-service action game in the spirit of Vampire Survivors. I built a content pipeline tool, wrote specs for and supported many mechanics — hero skills, weapon mechanics, gamepad controls — and balanced live content and events."
cover: "https://cdn.cloudflare.steamstatic.com/steam/apps/2479830/header.jpg"
cover_label: "Unity"
accent: teal
tags: [Tools, Mechanics, Gamepad, Live-ops]
role: "Technical Game Designer"
company: 101XP
period: "Mar 2023 — Nov 2024"
engine: "Unity"
platform: "PC (Steam)"
genre: "Survivors-like action, live-service"
status: "Released"
links:
  - { label: "Steam page", url: "https://store.steampowered.com/app/2479830/The_Braves/" }
highlights:
  - { value: "×10", label: "faster content integration with my tool" }
  - { value: "20+", label: "specs written for artists and programmers" }
stack: [Unity, "C#", ScriptableObjects, Google Sheets, Jira, Confluence, Git]
permalink: /experience/the-braves/
---

## Overview

**The Braves** is a live-service action game heavily inspired by *Vampire Survivors*, built around hero collection, progression systems and a steady flow of new content.

I joined the project after Craft of Survival and stayed until I left 101XP. The team had about 30 people, five of them game designers: tasks came from the project owner, and we split them among ourselves. As a technical game designer I worked both on the game itself and on the way content got into it. Since the game was continuously updated, most features were shaped through iteration — internal feedback, playtests and production priorities — rather than designed once and left alone.

## Content pipeline tool

**Problem.** Every piece of new content was designed in Google Sheets and then had to be transferred into the project’s admin panel by hand. With regular updates this was slow, repetitive and error-prone.

**Solution.** The admin panel had no usable API — it only ran in a browser. So I wrote a script for a screen automation tool (Clickerman, in BASIC) that moves the data from Google Sheets into the admin panel by itself. A typical job: 5 armor sets × 4 pieces × 5 rarities — 100 near-identical entries.

**Result.** The script keeps a steady pace and never tires, while manual entry slows down after a few items. Content integration became **10× faster**, and designers spent their time on design and balance instead of data entry.

## Mechanics

I wrote design specs for and supported a large number of mechanics — most of them small, but together they make up a big part of the game:

- **Hero skills** — individual abilities designed from concept through implementation and balance.
- **Weapon mechanics** — new weapon behaviours added as part of content updates.
- **Gamepad controls** — the UI was built for a mouse, so controller support had to fit into existing screens full of tabs and sub-menus. I followed familiar conventions: bumpers switch main tabs, triggers switch nested ones, holding the upgrade button upgrades to max. The spec had a single layout table for Sony, Xbox and Nintendo built on abstract actions (“Action 1” = Square / X), and the rest of the document referred only to actions — so a layout could change in one place without rewriting the spec.
- **Boss variations** — for example, an elite version of a boss that fires a wave and advances inside a ring of spinning discs. Mine first spawns a ring wide enough to trap the player, then adds tighter and tighter rings that herd the player toward the boss — and only then fires the wave, which the player has to dodge.
- **Achievement showcase** — designed the achievement showcase, frames and avatars from scratch — groundwork for future social features. The first iteration followed Steam (click a slot, then pick from a list) and didn’t convince the project owner. In the second, the list is open from the start and each click adds an achievement to the showcase in order. That version was approved.

## Content and live operations

- Set up new content in the game for regular updates.
- For seasonal events — Halloween and New Year — new heroes and skins were added to the gacha. I calculated the drop rates and set them up in the game.
- Tuned enemy difficulty, rewards and the gacha economy across live updates, making sure new content didn’t disrupt the player’s progression.

## Challenges

Adding features to a game that is already live means respecting what players have: new mechanics had to fit existing systems, stay compatible with future content and not break progression. Much of the work was careful, incremental improvement rather than replacing what already worked.
