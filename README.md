# 🎮 Unity Developer Portfolio — Streamlit Edition

A game-landing-page-styled portfolio, built with Streamlit. Sidebar
"Main Menu" navigation, HUD hero, a "game library" for projects, a
"quest log" for experience, a "stat sheet" for skills, "player
reviews" for testimonials, and "achievements unlocked" for certs.

Runs entirely on free hosting (Streamlit Community Cloud), no backend
required.

---

## 1. Run it locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

It opens at `http://localhost:8501`. Everything works with the
placeholder content out of the box — no missing images will break it,
they just show a styled fallback until you add real ones.

---

## 2. Personalize your content

**You should only ever need to edit `data.py`.** Every string on the
site — your name, bio, projects, jobs, skills, testimonials,
certifications, and contact info — lives in that one file, laid out
as plain Python dicts and lists. Open it and replace anything inside
`[ ]` brackets.

- To add/remove a project, testimonial, job, or cert: copy an existing
  entry in the relevant list in `data.py` and edit it, or delete one
  you don't need.
- Skill categories (`SKILLS` dict) and skill levels (0–100) are yours
  to redefine — add or remove categories freely.

`app.py` (layout) and `style.py` (CSS/colors/fonts) don't need to be
touched unless you want to change the design itself.

## 3. Add your assets

Drop these files into the `assets/` folder using these exact names
(all optional — the site degrades gracefully without them):

| File | Used for |
|---|---|
| `assets/avatar.png` | Sidebar profile photo (square image works best) |
| `assets/about_portrait.png` | Portrait on the About Me page |
| `assets/resume.pdf` | Download button + inline preview on Resume page |
| `assets/projects/project1.png` (etc.) | Cover art for each project card — match the path in `data.py` |

## 4. Change the color/theme (optional)

Open `style.py` — the palette is defined once at the top as CSS
variables (`--violet`, `--mint`, `--gold`, `--bg`, etc.) inside the
`CSS` string. Change those hex values and the whole site re-themes.
Fonts are loaded from Google Fonts in the same `@import` line.

## 5. Wire up the contact form (optional)

By default the contact form validates input but doesn't send email
(no backend). To make it actually deliver messages for free:

1. Create a free form endpoint at [formspree.io](https://formspree.io).
2. Paste your endpoint URL into `CONTACT["formspree_endpoint"]` in
   `data.py`.

Without this, the form still works as a "get in touch" panel with a
direct mailto link and social links.

---

## 6. Deploy for free — Streamlit Community Cloud

1. Push this whole folder to a **public** GitHub repo (private repos
   need a paid plan to deploy for free — public is free either way).
2. Go to **[share.streamlit.io](https://share.streamlit.io)**, sign
   in with GitHub, click **New app**.
3. Pick your repo/branch, set the main file to `app.py`, click
   **Deploy**.
4. You get a free `yourapp.streamlit.app` URL. Every push to your
   repo redeploys automatically.

That's it — no server, no Docker, no cost.

---

## Project structure

```
unity_portfolio/
├── app.py                  # layout + navigation + section rendering
├── data.py                 # ← ALL your content goes here
├── style.py                # CSS design system (colors, type, components)
├── requirements.txt
├── .streamlit/config.toml  # base dark theme for native widgets
└── assets/
    ├── avatar.png           (you add)
    ├── about_portrait.png   (you add)
    ├── resume.pdf           (you add)
    ├── projects/            (you add cover images)
    └── certs/               (unused by default — reserved if you want cert badge images later)
```

## Design notes

- Sidebar "Main Menu" behaves like a game pause menu — your name,
  level tag, and status sit in a player card, with animated-glow nav
  items below it.
- Fonts: **Rajdhani** for headings (HUD/geometric feel), **Press
  Start 2P** used sparingly for small pixel-style eyebrow labels only
  (never for paragraph text — it's unreadable at length), **Inter**
  for body copy, **JetBrains Mono** for stats and numbers.
- Everything reflows for mobile since it's built on Streamlit's
  responsive column grid.
