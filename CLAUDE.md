# Notes for Claude working on this site

## CV must always match the site
Standing rule from the site owner: every change to the site updates BOTH CVs (EN and RU)
in the same commit, without being asked. Never push a site change with a stale CV
or a red `build_cv.py --check`.

Both CVs (`assets/files/Timur_Khazirov_CV.pdf`, `assets/files/Timur_Khazirov_CV_RU.pdf`)
are generated — never edit the PDFs by hand.

- Job titles and dates: `_data/career.yml` (shared with the site timeline)
- Contacts: `_data/profile.yml` (shared with the site header/footer)
- All other CV text (both languages): `_cv/cv.yml`

After ANY change to site content (pages, `_data/*`), before committing:
1. Check whether the change affects a fact that is also in the CV (dates, roles,
   projects, numbers, tools, languages, contacts). If it does, update `_cv/cv.yml`
   in BOTH languages so the CV says the same thing as the site.
2. Run `python3 tools/build_cv.py` — it rebuilds the PDFs when any source changed.
3. Run `python3 tools/build_cv.py --check` — must exit 0 (no stale PDFs, no fact mismatches).
   Add new cross-checked facts to `FACTS` in `tools/build_cv.py` when a key number appears.

The GitHub Action `.github/workflows/cv-check.yml` runs the same check on every push.

The CV download buttons (sidebar and About page) use `profile.cv[lang]`, so the
English site serves the English CV and `/ru/` serves the Russian one.

If Playwright's Chromium is not installed but another Chromium binary is, run the build
with that binary by patching `BrowserType.launch` to pass `executable_path` (do not
change `build_cv.py` for a local environment).

## Languages
Every page exists in EN (root) and RU (`ru/`), linked by the same `ref`.
Any content change must be made in both languages. Russian copy should read
naturally (no calques or bureaucratic phrasing).
