#!/usr/bin/env python3
"""Build both CV PDFs (EN + RU) from one source, in sync with the site.

Sources:
  _cv/cv.yml          CV text (both languages)
  _data/career.yml    job titles and dates   (shared with the site timeline)
  _data/profile.yml   contacts               (shared with the site header/footer)

Usage:
  python3 tools/build_cv.py           rebuild PDFs if any source changed
  python3 tools/build_cv.py --force   rebuild unconditionally
  python3 tools/build_cv.py --check   exit 1 if the PDFs are out of date or facts disagree

Needs: pyyaml, playwright (+ Chromium). Fonts: Liberation Serif / Times New Roman.
"""
import hashlib, html, os, re, sys, tempfile
import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = ["_cv/cv.yml", "_data/career.yml", "_data/profile.yml", "tools/build_cv.py"]
OUT = {"en": "assets/files/Timur_Khazirov_CV.pdf", "ru": "assets/files/Timur_Khazirov_CV_RU.pdf"}
STAMP = "_cv/.build-hash"
NAME = {"en": "TIMUR KHAZIROV", "ru": "ТИМУР ХАЗИРОВ"}
SITE = "https://khazirovtimur.github.io"

# Facts that must read the same on the site and in both CVs.
FACTS = [
    {"en": "C1", "ru": "C1", "site": ["about/index.md", "ru/about/index.md"]},
    {"en": "10×", "ru": "10 раз", "site": ["experience/the-braves.md", "ru/experience/the-braves.md"]},
    {"en": "20+", "ru": "20+", "site": ["experience/the-braves.md", "ru/experience/the-braves.md"]},
    {"en": "50+", "ru": "50+", "site": ["_data/home.yml"]},
    {"en": "Senior Technical / Balance Game Designer", "ru": "Senior-геймдизайнер: техдизайн и баланс", "site": ["_data/i18n.yml", "_data/ui.yml"]},
    {"en": "3,000", "ru": "3 000", "site": ["experience/pioner.md", "ru/experience/pioner.md"]},
]


def load(p):
    with open(os.path.join(ROOT, p), encoding="utf-8") as f:
        return yaml.safe_load(f)


def sources_hash():
    h = hashlib.sha256()
    for p in SRC:
        with open(os.path.join(ROOT, p), "rb") as f:
            h.update(f.read())
    return h.hexdigest()


def e(s):
    return html.escape(str(s))


def render(lang, cv, career, prof):
    t = lambda d: d[lang]
    H = cv["headings"]
    li = "".join
    contacts = [f"Email: {e(prof['email'])}"]
    if prof.get("linkedin"):
        contacts.append(f'LinkedIn: <a href="{e(prof["linkedin"])}">Timur Khazirov</a>')
    if prof.get("telegram"):
        contacts.append(f"Telegram: @{e(prof['telegram'])}")
    site_url = SITE + ("/ru/" if lang == "ru" else "/")
    contacts.append(f'{e(t(H["portfolio"]))}: <a href="{site_url}">khazirovtimur.github.io</a>')

    jobs = []
    for job in career:
        ref = job["projects"][0] if job.get("projects") else "qa"
        data = cv["jobs"][ref]
        role = re.sub(r"\s·\s.*$", "", t(job["role"]))  # drop " · Project" suffix
        project = ""
        if data.get("project"):
            project = f'<div class="job-project">{e(t(H["project"]))}: {e(t(data["project"]))}</div>'
        bullets = li(f"<li>{e(b)}</li>" for b in t(data["bullets"]))
        jobs.append(f'''<div class="job">
  <div class="job-head"><span class="job-title">{e(role)} — {e(job["company"])}</span><span class="job-dates">{e(t(job["period"]))}</span></div>
  {project}<ul>{bullets}</ul></div>''')

    skills = li(f"<dt>{e(t(s['name']))}</dt><dd>{e(t(s['text']))}</dd>" for s in cv["skills"])
    dot = ' <span class="dots">•</span> '
    projects = li(f"<p><b>{e(t(p['name']))}</b> — {e(t(p['text']))}</p>" for p in cv["personal_projects"])

    return f'''<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><title>{e(NAME[lang])} — CV</title>
<style>
@page {{ size: A4; margin: 15mm 16mm 14mm 16mm; }}
* {{ box-sizing: border-box; }}
body {{ margin: 0; font-family: "Liberation Serif", "Times New Roman", serif; font-size: 10.6pt; line-height: 1.36; color: #1a1a1a; }}
h1 {{ margin: 0; font-size: 22pt; letter-spacing: .03em; color: #0f1f3d; }}
.role {{ margin: 2px 0 6px; font-size: 13pt; font-weight: bold; color: #2f5496; }}
.contacts {{ font-size: 9.6pt; color: #555; }} .contacts a {{ color: #2f5496; }}
.note {{ font-size: 9.6pt; font-style: italic; color: #666; margin-top: 2px; }}
h2 {{ margin: 14px 0 6px; padding-bottom: 3px; border-bottom: 1.2px solid #2f5496; font-size: 11.5pt; letter-spacing: .08em; text-transform: uppercase; color: #2f5496; break-after: avoid-page; }}
p {{ margin: 0 0 5px; }}
.skills {{ display: grid; grid-template-columns: 136px 1fr; gap: 1px 12px; margin: 0; }}
.skills dt {{ font-weight: bold; color: #0f1f3d; }} .skills dd {{ margin: 0; }}
.job {{ margin-top: 9px; }}
.job-head, .job-project {{ break-after: avoid-page; }}
.job-head {{ display: flex; justify-content: space-between; align-items: baseline; gap: 12px; }}
.job-title {{ font-weight: bold; font-size: 11.2pt; color: #0f1f3d; }}
.job-dates {{ font-style: italic; color: #666; font-size: 9.8pt; white-space: nowrap; }}
.job-project {{ font-style: italic; color: #2f5496; font-size: 9.8pt; margin: 1px 0 3px; }}
ul {{ margin: 2px 0 0; padding-left: 15px; }} li {{ margin: 2px 0; break-inside: avoid-page; }}
.dots {{ color: #2f5496; padding: 0 2px; }}
</style></head><body>
<h1>{e(NAME[lang])}</h1>
<div class="role">{e(t(cv["title"]))}</div>
<div class="contacts">{" &nbsp;|&nbsp; ".join(contacts)}</div>
<div class="note">{e(t(cv["note"]))}</div>
<h2>{e(t(H["profile"]))}</h2>{li(f"<p>{e(p)}</p>" for p in t(cv["profile"]))}
<h2>{e(t(H["competencies"]))}</h2><p>{dot.join(e(c) for c in t(cv["competencies"]))}</p>
<h2>{e(t(H["skills"]))}</h2><dl class="skills">{skills}</dl>
<h2>{e(t(H["experience"]))}</h2>{li(jobs)}
<h2>{e(t(H["projects"]))}</h2>{projects}
<h2>{e(t(H["education"]))}</h2><ul>{li(f"<li>{e(x)}</li>" for x in t(cv["education"]))}</ul>
<h2>{e(t(H["additional"]))}</h2><p>{dot.join(e(x) for x in t(cv["additional"]))}</p>
<h2>{e(t(H["languages"]))}</h2><p>{e(t(cv["languages"]))}</p>
</body></html>'''


def check_facts(cv_texts):
    problems = []
    for f in FACTS:
        for lang in ("en", "ru"):
            if f[lang] not in cv_texts[lang]:
                problems.append(f"CV {lang}: missing '{f[lang]}'")
        for p in f["site"]:
            lang = "ru" if p.startswith("ru/") else "en"
            with open(os.path.join(ROOT, p), encoding="utf-8") as fh:
                if f[lang] not in fh.read():
                    problems.append(f"site {p}: missing '{f[lang]}'")
    return problems


def main():
    args = set(sys.argv[1:])
    cv, career, prof = load("_cv/cv.yml"), load("_data/career.yml"), load("_data/profile.yml")
    pages = {lang: render(lang, cv, career, prof) for lang in ("en", "ru")}
    problems = check_facts({k: html.unescape(v) for k, v in pages.items()})
    for ref in [(j["projects"][0] if j.get("projects") else "qa") for j in career]:
        if ref not in cv["jobs"]:
            problems.append(f"_cv/cv.yml: no bullets for career entry '{ref}'")
    h = sources_hash()
    stamp_path = os.path.join(ROOT, STAMP)
    old = open(stamp_path).read().strip() if os.path.exists(stamp_path) else ""
    stale = old != h or not all(os.path.exists(os.path.join(ROOT, p)) for p in OUT.values())

    if "--check" in args:
        for p in problems:
            print("FACT:", p)
        if stale:
            print("STALE: CV PDFs are older than their sources — run tools/build_cv.py")
        sys.exit(1 if (stale or problems) else 0)

    if problems:
        print("\n".join("FACT: " + p for p in problems))
        sys.exit(1)
    if not stale and "--force" not in args:
        print("CVs are up to date")
        return

    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw, tempfile.TemporaryDirectory() as tmp:
        browser = pw.chromium.launch()
        for lang, doc in pages.items():
            src = os.path.join(tmp, f"cv_{lang}.html")
            with open(src, "w", encoding="utf-8") as f:
                f.write(doc)
            page = browser.new_page()
            page.goto("file://" + src)
            page.pdf(path=os.path.join(ROOT, OUT[lang]), format="A4", print_background=True, prefer_css_page_size=True)
            print("built", OUT[lang])
        browser.close()
    with open(stamp_path, "w") as f:
        f.write(h + "\n")


if __name__ == "__main__":
    main()
