---
layout: case
ref: the-braves
lang: en
section: experience
order: 2
title: The Braves
eyebrow: "101XP · Unity · 2023 — 2024"
summary: "Live-service arcade game in the spirit of Vampire Survivors. I set up content, wrote specs for and owned many mechanics: hero skills, weapons, gamepad controls. I balanced enemies and the event economy, and made content setup 10× faster with a tool I built."
cover: "https://cdn.cloudflare.steamstatic.com/steam/apps/2479830/header.jpg"
cover_label: "Unity"
accent: teal
tags: [Tools, Mechanics, Gamepad, Live-ops]
role: "Technical Game Designer"
company: 101XP
period: "Mar 2023 — Nov 2024"
engine: "Unity"
platform: "PC (Steam)"
genre: "Survivors-like arcade, live-service"
status: "Released"
links:
  - { label: "Steam page", url: "https://store.steampowered.com/app/2479830/The_Braves/" }
highlights:
  - { value: "×10", label: "faster content integration with my tool" }
  - { value: "25+", label: "specs written for artists and programmers" }
stack: [Unity, "C#", ScriptableObjects, Google Sheets, Jira, Confluence, Git]
permalink: /experience/the-braves/
---

## Overview

**The Braves** is a live-service arcade game heavily inspired by *Vampire Survivors*. The player collects heroes, upgrades them, their gear and the hub, and fights monsters and bosses across different locations.

I joined the project after Craft of Survival and stayed until I left 101XP. The team had about 30 people, five of them game designers: tasks came from the project owner, and we split them among ourselves. As a technical game designer I worked both on the game itself and on the way content got into it. The game was continuously updated, so there was a constant flow of new tasks and content.

## Content pipeline tool

**Problem.** Every piece of new content was calculated and balanced in Google Sheets and then had to be transferred into the project’s admin panel by hand. With regular updates this was slow, repetitive and error-prone.

**Solution.** The admin panel had no usable API and only ran in a browser. So I wrote a script for a screen automation tool (Clickerman, in BASIC) that moves the data from Google Sheets into the admin panel by itself. A typical job: 5 armor sets × 4 pieces × 5 rarities, which makes 100 near-identical entries.

**Result.** The script keeps a steady pace and never tires, while manual entry slows down after a few items. Content integration became **10× faster**, and designers spent their time on design and balance instead of data entry.

## Mechanics

I wrote design specs for and owned a large number of mechanics. Most of them are small, but together they make up a big part of the game:

- **Hero skills**: individual abilities designed from concept through implementation and balance.
- **Weapon mechanics**: new weapon behaviors added as part of content updates.
- **Gamepad controls**: the UI was built for a mouse, so controller support had to fit into existing screens full of tabs and sub-menus. I followed familiar conventions: bumpers switch main tabs, triggers switch nested ones, holding the upgrade button upgrades to max. The spec had a single layout table for Sony, Xbox and Nintendo built on abstract actions (“Action 1” = Square / X), and the rest of the document referred only to actions, so a layout could change in one place without rewriting the spec.
- **Boss variations**: for example, an elite version of a boss that fires a wave and advances inside a ring of spinning discs. Mine first spawns a ring wide enough to trap the player, then adds tighter and tighter rings that herd the player toward the boss. Only then does it fire the wave, which the player has to dodge.
- **Player profile**: designed its UX from scratch: the achievement showcase, frames and avatars, groundwork for future social features.

## Content and live operations

- Set up new content: heroes, gear, abilities, monsters and more.
- Seasonal events such as Halloween or New Year brought a seasonal gacha with limited heroes, skins and weapons. I calculated the drop rates and set them up in the game.
- Tuned enemy difficulty and level completion rewards.
