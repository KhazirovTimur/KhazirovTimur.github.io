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
period: "Mid 2023 — Nov 2024"
engine: "Unity"
platform: "PC (Steam)"
genre: "Survivors-like action, live-service"
status: "Released"
links:
  - { label: "Steam page", url: "https://store.steampowered.com/app/2479830/The_Braves/" }
highlights:
  - { value: "~5×", label: "faster content integration with my tool" }
stack: [Unity, "C#", ScriptableObjects, Google Sheets, Jira, Confluence, Git]
permalink: /experience/the-braves/
---

## Overview

**The Braves** is a live-service action game heavily inspired by *Vampire Survivors*, built around hero collection, progression systems and a steady flow of new content.

I joined the project after Craft of Survival and stayed on it until I left 101XP. As a technical game designer I worked both on the game itself and on the way content got into it. Since the game was continuously updated, most features were shaped through iteration — internal feedback, playtests and production priorities — rather than designed once and left alone.

## Content pipeline tool

**Problem.** Every piece of new content was designed in Google Sheets and then had to be transferred into the project’s admin panel by hand. With regular updates this was slow, repetitive and error-prone.

**Solution.** I built an internal tool that moves the data from Google Sheets into the admin panel automatically.

**Result.** Content integration became **roughly 5× faster**, and designers spent their time on design and balance instead of manual data entry.

## Mechanics

I wrote design specs for and supported a large number of mechanics — most of them small, but together they make up a big part of the game:

- **Hero skills** — individual abilities designed from concept through implementation and balance.
- **Weapon mechanics** — new weapon behaviours added as part of content updates.
- **Gamepad controls** — I owned controller support: how every gameplay action and every screen works with a gamepad, from input and navigation design to implementation with programmers and UI artists. A mobile version of the game was also planned.
- **Boss variations** — elite versions with additional attack patterns, tuned so they stay challenging across updates.
- **Gameplay UI** — player-facing UI flows, including a redesign of the achievement interface.

## Content and live operations

- Set up new content in the game for regular updates.
- Calculated part of the balance for an in-game event.
- Tuned enemy difficulty, rewards and the gacha economy across live updates, making sure new content didn’t disrupt the player’s progression.

## Challenges

Adding features to a game that is already live means respecting what players have: new mechanics had to fit existing systems, stay compatible with future content and not break progression. Much of the work was careful, incremental improvement rather than replacing what already worked.
