"""
Unity Game Developer Portfolio — "game landing page" built in Streamlit.

Structure:
  data.py   -> all editable content (name, projects, skills, etc.)
  style.py  -> CSS design system (colors, type, components)
  app.py    -> this file: page config, nav, and section rendering

Run locally:
    pip install -r requirements.txt
    streamlit run app.py

Deploy free on Streamlit Community Cloud:
    1. Push this folder to a public GitHub repo.
    2. Go to https://share.streamlit.io -> New app -> pick the repo -> app.py
    3. Done. Redeploys automatically on every push.
"""

import base64
import os

import streamlit as st
from streamlit_option_menu import option_menu

import data as d
from style import inject

# ------------------------------------------------------------------
# Page config + global CSS
# ------------------------------------------------------------------
st.set_page_config(
    page_title=f"{d.PROFILE['name']} — {d.PROFILE['role']}",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded",
)
inject(st)


# ------------------------------------------------------------------
# Helpers
# ------------------------------------------------------------------
def b64_image(path):
    """Return base64-encoded image data, or None if the file doesn't exist."""
    if path and os.path.isfile(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None


b64_file = b64_image  # same helper, used for both images and the resume PDF


def initials(name):
    parts = [p for p in name.replace("[", "").replace("]", "").split() if p]
    return "".join(p[0].upper() for p in parts[:2]) or "?"


def stat_bar(label, value, suffix="/ 100"):
    st.markdown(
        f"""
        <div class="stat-row">
            <div class="stat-top"><span>{label}</span><span>{value} {suffix}</span></div>
            <div class="stat-track"><div class="stat-fill" style="width:{value}%;"></div></div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def section_head(title, subtitle=None, eyebrow=None):
    eyebrow_html = f'<span class="eyebrow">{eyebrow}</span><br>' if eyebrow else ""
    sub_html = f'<div class="sec-sub">{subtitle}</div>' if subtitle else ""
    st.markdown(
        f'<div class="sec-head">{eyebrow_html}<h2>{title}</h2>{sub_html}</div>',
        unsafe_allow_html=True,
    )


def link_button_row(links):
    """Render external links as HTML anchor-buttons (no server round-trip needed)."""
    buttons = ""
    for label, url in links.items():
        if not url:
            continue
        buttons += (
            f'<a href="{url}" target="_blank" style="text-decoration:none;">'
            f'<span style="display:inline-block;margin:4px 8px 0 0;padding:6px 14px;'
            f'border-radius:8px;background:linear-gradient(90deg,#8B5CF6,#6D3FE0);'
            f'color:white;font-family:Rajdhani,sans-serif;font-weight:700;font-size:0.85rem;">'
            f'{label}</span></a>'
        )
    if buttons:
        st.markdown(buttons, unsafe_allow_html=True)


# ------------------------------------------------------------------
# Sidebar — "Main Menu"
# ------------------------------------------------------------------
with st.sidebar:
    avatar_b64 = b64_image(d.PROFILE["avatar"])
    avatar_html = (
        f'<img src="data:image/png;base64,{avatar_b64}">'
        if avatar_b64
        else f'''<div style="width:72px;height:72px;border-radius:50%;margin:0 auto 8px auto;
                display:flex;align-items:center;justify-content:center;
                background:linear-gradient(135deg,#8B5CF6,#2DD4BF);
                font-family:Rajdhani,sans-serif;font-weight:700;font-size:1.4rem;color:#0A0D14;
                border:2px solid #8B5CF6;">{initials(d.PROFILE["name"])}</div>'''
    )

    st.markdown(
        f"""
        <div class="player-card">
            {avatar_html}
            <div class="player-name">{d.PROFILE['name']}</div>
            <div>{d.PROFILE['role']}</div>
            <div class="player-lvl">LVL {d.PROFILE['level']}</div>
            <div class="player-status">{d.PROFILE['status']}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    NAV_OPTIONS = [
        "Home", "About Me", "Projects", "Experience",
        "Skills", "Testimonials", "Certifications", "Resume", "Contact",
    ]
    # lets the "View Projects" button on Home jump the menu to another page
    forced_index = st.session_state.pop("force_nav_index", None)

    selected = option_menu(
        menu_title=None,
        options=NAV_OPTIONS,
        icons=[
            "house-door", "person-badge", "controller", "briefcase",
            "bar-chart-steps", "star", "award", "file-earmark-text", "envelope",
        ],
        default_index=0,
        manual_select=forced_index,
        key="main_menu",
        styles={
            "container": {"padding": "0", "background-color": "transparent"},
            "icon": {"color": "#8892B0", "font-size": "15px"},
            "nav-link": {
                "font-family": "Rajdhani, sans-serif",
                "font-weight": "600",
                "font-size": "15px",
                "color": "#E8EAF6",
                "border-radius": "8px",
                "margin": "3px 0",
                "padding": "9px 12px",
            },
            "nav-link-selected": {
                "background-color": "rgba(139,92,246,0.18)",
                "color": "#FFFFFF",
                "border-left": "3px solid #8B5CF6",
            },
        },
    )

    st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)
    social_line = "  ·  ".join(
        f'<a href="{url}" target="_blank">{name}</a>'
        for name, url in d.PROFILE["socials"].items()
        if url
    )
    st.markdown(
        f'<div style="font-size:0.78rem; text-align:center;">{social_line}</div>',
        unsafe_allow_html=True,
    )


# ------------------------------------------------------------------
# HOME
# ------------------------------------------------------------------
def render_home():
    st.markdown('<div class="hero-wrap">', unsafe_allow_html=True)
    st.markdown('<span class="eyebrow">◆ PRESS START</span>', unsafe_allow_html=True)
    st.markdown(f'<div class="hero-title">{d.PROFILE["name"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="hero-role">&gt; {d.PROFILE["role"]} — {d.PROFILE["location"]}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="hero-tagline">{d.PROFILE["tagline"]}</div>', unsafe_allow_html=True)

    c1, c2, c3 = st.columns([1, 1, 4])
    with c1:
        if st.button("🎮 View Projects", use_container_width=True):
            st.session_state["force_nav_index"] = 2  # index of "Projects" in NAV_OPTIONS
            st.rerun()
    with c2:
        resume_data = b64_image(d.PROFILE["resume_pdf"])
        if resume_data:
            st.download_button(
                "📄 Resume",
                data=base64.b64decode(resume_data),
                file_name="resume.pdf",
                mime="application/pdf",
                use_container_width=True,
            )
        else:
            st.button("📄 Resume", use_container_width=True, disabled=True,
                       help="Add assets/resume.pdf to enable this")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<div style='height:10px;'></div>", unsafe_allow_html=True)
    cols = st.columns(len(d.PROFILE["hero_stats"]))
    for col, stat in zip(cols, d.PROFILE["hero_stats"]):
        with col:
            st.markdown(
                f'<div class="hud-stat"><div class="num">{stat["value"]}</div>'
                f'<div class="lbl">{stat["label"]}</div></div>',
                unsafe_allow_html=True,
            )

    st.markdown("<div style='height:34px;'></div>", unsafe_allow_html=True)
    section_head("Featured Builds", eyebrow="◆ LEVEL SELECT")
    feat_cols = st.columns(min(3, len(d.PROJECTS)))
    for col, proj in zip(feat_cols, d.PROJECTS[:3]):
        with col:
            render_project_card(proj, compact=True)


# ------------------------------------------------------------------
# ABOUT ME
# ------------------------------------------------------------------
def render_about():
    section_head("About Me", eyebrow="◆ CHARACTER SHEET")
    col1, col2 = st.columns([1, 1.6], gap="large")

    with col1:
        portrait_b64 = b64_image(d.ABOUT["portrait"])
        if portrait_b64:
            st.markdown(
                f'<div class="panel"><img src="data:image/png;base64,{portrait_b64}" '
                f'style="width:100%;border-radius:8px;"></div>',
                unsafe_allow_html=True,
            )
        else:
            st.markdown(
                '<div class="panel" style="text-align:center;padding:60px 20px;'
                'color:#8892B0;font-family:JetBrains Mono, monospace;font-size:0.8rem;">'
                'Add assets/about_portrait.png</div>',
                unsafe_allow_html=True,
            )
        st.markdown('<div class="panel">', unsafe_allow_html=True)
        st.markdown('<span class="eyebrow">Fun Facts</span>', unsafe_allow_html=True)
        for fact in d.ABOUT["fun_facts"]:
            st.markdown(f"- {fact}")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="panel">', unsafe_allow_html=True)
        for para in d.ABOUT["bio_paragraphs"]:
            st.markdown(f"<p style='color:#C7CBE0;'>{para}</p>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="panel">', unsafe_allow_html=True)
        st.markdown('<span class="eyebrow">Core Attributes</span>', unsafe_allow_html=True)
        for trait in d.ABOUT["traits"]:
            stat_bar(trait["label"], trait["value"])
        st.markdown('</div>', unsafe_allow_html=True)


# ------------------------------------------------------------------
# PROJECTS
# ------------------------------------------------------------------
def render_project_card(proj, compact=False):
    cover_b64 = b64_image(proj["cover"])
    cover_html = (
        f'<img src="data:image/png;base64,{cover_b64}">'
        if cover_b64 else proj["genre"]
    )
    st.markdown(f'<div class="proj-cover">{cover_html}</div>', unsafe_allow_html=True)
    st.markdown(
        f"""
        <div class="proj-card-body">
            <div class="proj-genre">{proj['genre']} · {proj['engine']} · {proj['year']}</div>
            <div class="proj-title">{proj['title']}</div>
            <div class="proj-blurb">{proj['blurb']}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    link_button_row(proj["links"])
    if not compact:
        with st.expander("▶ Full Case Study"):
            st.markdown(f"**Role:** {proj['role']}  \n**Platform:** {proj['platform']}")
            st.markdown(proj["description"])
            tags_html = "".join(f'<span class="tag-chip">{t}</span>' for t in proj["tags"])
            st.markdown(tags_html, unsafe_allow_html=True)
    st.markdown("<div style='height:22px;'></div>", unsafe_allow_html=True)


def render_projects():
    section_head("Game Library", "Every title below shipped, jammed, or launched publicly.", eyebrow="◆ LIBRARY")
    cols = st.columns(3)
    for i, proj in enumerate(d.PROJECTS):
        with cols[i % 3]:
            render_project_card(proj, compact=False)


# ------------------------------------------------------------------
# EXPERIENCE
# ------------------------------------------------------------------
def render_experience():
    section_head("Experience", "The quest log — studios, teams, and shipped work.", eyebrow="◆ QUEST LOG")
    for job in d.EXPERIENCE:
        st.markdown('<div class="panel quest-card">', unsafe_allow_html=True)
        st.markdown(f'<span class="quest-tag">{job["reward_tag"]}</span>', unsafe_allow_html=True)
        st.markdown(
            f"<h4 style='margin:0;'>{job['role']} · <span style='color:#8B5CF6;'>{job['company']}</span></h4>",
            unsafe_allow_html=True,
        )
        st.markdown(
            f'<div style="color:#8892B0;font-family:JetBrains Mono, monospace;font-size:0.8rem;">'
            f'{job["period"]} · {job["location"]}</div>',
            unsafe_allow_html=True,
        )
        st.markdown(f"<p style='color:#C7CBE0;margin-top:8px;'>{job['summary']}</p>", unsafe_allow_html=True)
        for ach in job["achievements"]:
            st.markdown(f"- {ach}")
        st.markdown('</div>', unsafe_allow_html=True)


# ------------------------------------------------------------------
# SKILLS
# ------------------------------------------------------------------
def render_skills():
    section_head("Skills", "Stat sheet — tools, languages, and the specialties I lean on.", eyebrow="◆ STAT SHEET")
    cats = list(d.SKILLS.items())
    cols = st.columns(2)
    for i, (cat, skills) in enumerate(cats):
        with cols[i % 2]:
            st.markdown('<div class="panel">', unsafe_allow_html=True)
            st.markdown(f'<span class="eyebrow">{cat}</span>', unsafe_allow_html=True)
            for s in skills:
                stat_bar(s["name"], s["level"])
            st.markdown('</div>', unsafe_allow_html=True)


# ------------------------------------------------------------------
# TESTIMONIALS
# ------------------------------------------------------------------
def render_testimonials():
    section_head("Player Reviews", "What teammates and leads say after shipping together.", eyebrow="◆ REVIEWS")
    cols = st.columns(3)
    for i, t in enumerate(d.TESTIMONIALS):
        with cols[i % 3]:
            stars = "★" * t["rating"] + "☆" * (5 - t["rating"])
            st.markdown(
                f"""
                <div class="panel">
                    <div class="review-stars">{stars}</div>
                    <div class="review-quote">“{t['quote']}”</div>
                    <div class="review-name">{t['name']}</div>
                    <div class="review-title">{t['title']}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )


# ------------------------------------------------------------------
# CERTIFICATIONS
# ------------------------------------------------------------------
def render_certifications():
    section_head("Achievements Unlocked", "Certifications and courses, ranked by how much they made me sweat.", eyebrow="◆ TROPHIES")
    cols = st.columns(3)
    for i, c in enumerate(d.CERTIFICATIONS):
        with cols[i % 3]:
            title_html = (
                f'<a href="{c["link"]}" target="_blank" style="color:inherit;text-decoration:none;">{c["title"]}</a>'
                if c.get("link") else c["title"]
            )
            st.markdown(
                f"""
                <div class="panel ach-card">
                    <div class="ach-icon">{c['icon']}</div>
                    <div class="proj-title" style="font-size:1.05rem;">{title_html}</div>
                    <div class="review-title">{c['issuer']} · {c['date']}</div>
                    <span class="ach-rarity rarity-{c['rarity']}">{c['rarity']}</span>
                </div>
                """,
                unsafe_allow_html=True,
            )


# ------------------------------------------------------------------
# RESUME
# ------------------------------------------------------------------
def render_resume():
    section_head("Game Manual", "The full printable rundown — one PDF, everything above.", eyebrow="◆ MANUAL")
    resume_b64 = b64_image(d.PROFILE["resume_pdf"])
    st.markdown('<div class="panel">', unsafe_allow_html=True)
    if resume_b64:
        st.download_button(
            "📄 Download Resume (PDF)",
            data=base64.b64decode(resume_b64),
            file_name=f"{d.PROFILE['name'].replace(' ', '_')}_Resume.pdf",
            mime="application/pdf",
        )
        st.markdown("<div style='height:16px;'></div>", unsafe_allow_html=True)
        pdf_html = (
            f'<iframe src="data:application/pdf;base64,{resume_b64}" '
            f'width="100%" height="700" style="border:1px solid #262E4A;border-radius:10px;"></iframe>'
        )
        st.markdown(pdf_html, unsafe_allow_html=True)
    else:
        st.info("Add your PDF at `assets/resume.pdf` to enable download + preview here.")
    st.markdown('</div>', unsafe_allow_html=True)


# ------------------------------------------------------------------
# CONTACT
# ------------------------------------------------------------------
def render_contact():
    section_head(d.CONTACT["headline"], d.CONTACT["subtext"], eyebrow="◆ MULTIPLAYER")
    col1, col2 = st.columns([1.3, 1], gap="large")

    with col1:
        st.markdown('<div class="panel">', unsafe_allow_html=True)
        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input("Your name")
            email = st.text_input("Your email")
            message = st.text_area("Message", height=140)
            sent = st.form_submit_button("🚀 Send Transmission")

        if sent:
            if not (name and email and message):
                st.warning("Fill in every field before sending.")
            elif d.CONTACT["formspree_endpoint"]:
                try:
                    import requests
                    r = requests.post(
                        d.CONTACT["formspree_endpoint"],
                        data={"name": name, "email": email, "message": message},
                        headers={"Accept": "application/json"},
                        timeout=10,
                    )
                    if r.ok:
                        st.success("Message sent — thanks! I'll reply soon.")
                    else:
                        st.error("Something went wrong sending that. Try email instead.")
                except Exception:
                    st.error("Something went wrong sending that. Try email instead.")
            else:
                st.info(
                    f"Form isn't wired to send yet — add a Formspree endpoint in "
                    f"`data.py` (`CONTACT['formspree_endpoint']`), or email me directly "
                    f"at {d.CONTACT['email']}."
                )
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="panel">', unsafe_allow_html=True)
        st.markdown('<span class="eyebrow">Direct Connect</span>', unsafe_allow_html=True)
        st.markdown(f"📧 [{d.CONTACT['email']}](mailto:{d.CONTACT['email']})")
        for name, url in d.PROFILE["socials"].items():
            if url:
                st.markdown(f"🔗 [{name}]({url})")
        st.markdown('</div>', unsafe_allow_html=True)


# ------------------------------------------------------------------
# Router
# ------------------------------------------------------------------
page = selected

PAGES = {
    "Home": render_home,
    "About Me": render_about,
    "Projects": render_projects,
    "Experience": render_experience,
    "Skills": render_skills,
    "Testimonials": render_testimonials,
    "Certifications": render_certifications,
    "Resume": render_resume,
    "Contact": render_contact,
}

PAGES.get(page, render_home)()
