# Notes for Claude working on this site

## CV must always match the site
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

## Languages
Every page exists in EN (root) and RU (`ru/`), linked by the same `ref`.
Any content change must be made in both languages. Russian copy should read
naturally (no calques or bureaucratic phrasing).
