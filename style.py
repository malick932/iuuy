"""
Design tokens + CSS for the portfolio.

Palette
-------
bg            #0A0D14   near-black navy — the "void" behind the HUD
bg-panel      #12172A   panel fill
bg-panel-2    #171D33   slightly lighter panel (hover/alt rows)
border        #262E4A   hairline panel borders
accent-violet #8B5CF6   primary accent — epic-item purple
accent-mint   #2DD4BF   secondary accent — XP / online-status teal
accent-gold   #F5B400   achievement gold
text          #E8EAF6   primary text
text-muted    #8892B0   secondary text

Type
----
display : Rajdhani       (headings — geometric, HUD-like)
pixel   : Press Start 2P (used sparingly — badges, eyebrows, nav)
body    : Inter          (paragraph text)
mono    : JetBrains Mono (stats, numbers, tags)
"""

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@500;600;700&family=Press+Start+2P&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500;600&display=swap');

:root {
    --bg: #0A0D14;
    --bg-panel: #12172A;
    --bg-panel-2: #171D33;
    --border: #262E4A;
    --violet: #8B5CF6;
    --mint: #2DD4BF;
    --gold: #F5B400;
    --text: #E8EAF6;
    --text-muted: #8892B0;
}

/* ---------- base canvas ---------- */
.stApp {
    background:
        radial-gradient(ellipse 80% 50% at 50% -10%, rgba(139,92,246,0.14), transparent),
        repeating-linear-gradient(180deg, rgba(255,255,255,0.012) 0px, rgba(255,255,255,0.012) 1px, transparent 1px, transparent 3px),
        var(--bg);
    color: var(--text);
    font-family: 'Inter', sans-serif;
}
#MainMenu, footer, header {visibility: hidden;}
.block-container {padding-top: 2rem; padding-bottom: 4rem; max-width: 1080px;}

h1, h2, h3, h4 {
    font-family: 'Rajdhani', sans-serif !important;
    font-weight: 700 !important;
    color: var(--text) !important;
    letter-spacing: 0.01em;
}

::selection { background: var(--violet); color: white; }

/* ---------- eyebrow / pixel labels ---------- */
.eyebrow {
    font-family: 'Press Start 2P', monospace;
    font-size: 0.6rem;
    color: var(--mint);
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 0.6rem;
    display: inline-block;
}

/* ---------- sidebar / main menu ---------- */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0D111C 0%, #0A0D14 100%);
    border-right: 1px solid var(--border);
}
.player-card {
    border: 1px solid var(--border);
    background: var(--bg-panel);
    border-radius: 10px;
    padding: 14px;
    margin-bottom: 18px;
    text-align: center;
}
.player-card img {
    width: 72px; height: 72px; border-radius: 50%;
    object-fit: cover;
    border: 2px solid var(--violet);
    box-shadow: 0 0 16px rgba(139,92,246,0.5);
    margin-bottom: 8px;
}
.player-name { font-family: 'Rajdhani', sans-serif; font-weight: 700; font-size: 1.05rem; }
.player-lvl {
    display: inline-block; margin-top: 4px;
    font-family: 'JetBrains Mono', monospace; font-size: 0.68rem;
    color: var(--bg); background: var(--gold);
    padding: 2px 8px; border-radius: 20px; font-weight: 600;
}
.player-status {
    margin-top: 8px; font-size: 0.72rem; color: var(--mint);
    font-family: 'JetBrains Mono', monospace;
}
.player-status::before { content: "● "; }

/* option-menu overrides injected via kwargs in app.py, this covers fallback radio */
div[role="radiogroup"] label {
    font-family: 'Rajdhani', sans-serif !important;
    font-size: 1rem !important;
}

/* ---------- generic panel / card ---------- */
.panel {
    background: var(--bg-panel);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 22px 24px;
    margin-bottom: 16px;
    transition: border-color 0.2s ease, transform 0.2s ease;
}
.panel:hover { border-color: rgba(139,92,246,0.5); }

/* ---------- hero ---------- */
.hero-wrap { padding: 2.2rem 0 1rem 0; }
.hero-title {
    font-family: 'Rajdhani', sans-serif;
    font-weight: 700;
    font-size: 3.4rem;
    line-height: 1.05;
    background: linear-gradient(90deg, #FFFFFF 0%, #C9C4FF 60%, var(--violet) 100%);
    -webkit-background-clip: text;
    background-clip: text;
    color: transparent;
    margin: 0 0 0.4rem 0;
}
.hero-role {
    font-family: 'JetBrains Mono', monospace;
    color: var(--mint);
    font-size: 1.05rem;
    margin-bottom: 0.8rem;
}
.hero-tagline { color: var(--text-muted); font-size: 1.05rem; max-width: 560px; margin-bottom: 1.6rem; }

.hud-stat {
    border: 1px solid var(--border);
    background: var(--bg-panel);
    border-radius: 10px;
    padding: 12px 16px;
    text-align: center;
}
.hud-stat .num {
    font-family: 'JetBrains Mono', monospace;
    font-size: 1.5rem; font-weight: 600; color: var(--violet);
}
.hud-stat .lbl { font-size: 0.72rem; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.04em; }

/* ---------- buttons ---------- */
.stButton > button, .stDownloadButton > button, .stLinkButton > a {
    font-family: 'Rajdhani', sans-serif !important;
    font-weight: 700 !important;
    letter-spacing: 0.03em;
    background: linear-gradient(90deg, var(--violet), #6D3FE0) !important;
    color: white !important;
    border: none !important;
    border-radius: 8px !important;
    padding: 0.55rem 1.3rem !important;
    box-shadow: 0 0 0 rgba(139,92,246,0);
    transition: box-shadow 0.2s ease, transform 0.15s ease;
}
.stButton > button:hover, .stDownloadButton > button:hover, .stLinkButton > a:hover {
    box-shadow: 0 0 22px rgba(139,92,246,0.55);
    transform: translateY(-1px);
    color: white !important;
}
.stButton > button:focus-visible {
    outline: 2px solid var(--mint) !important; outline-offset: 2px;
}

/* secondary/ghost variant via kwarg type="secondary" */
button[kind="secondary"] {
    background: transparent !important;
    border: 1px solid var(--border) !important;
    color: var(--text) !important;
}
button[kind="secondary"]:hover { border-color: var(--mint) !important; box-shadow: 0 0 14px rgba(45,212,191,0.35) !important; }

/* ---------- stat bars (skills / traits) ---------- */
.stat-row { margin-bottom: 14px; }
.stat-row .stat-top {
    display: flex; justify-content: space-between;
    font-family: 'JetBrains Mono', monospace; font-size: 0.78rem;
    color: var(--text-muted); margin-bottom: 4px;
}
.stat-track {
    width: 100%; height: 8px; background: #1B2138;
    border-radius: 6px; overflow: hidden; border: 1px solid var(--border);
}
.stat-fill {
    height: 100%; border-radius: 6px;
    background: linear-gradient(90deg, var(--mint), var(--violet));
}

/* ---------- project cards (game library) ---------- */
.proj-cover {
    width: 100%; aspect-ratio: 16/9; border-radius: 10px 10px 0 0;
    background: linear-gradient(135deg, #1B2138, #0F1424);
    display: flex; align-items: center; justify-content: center;
    color: var(--text-muted); font-family: 'JetBrains Mono', monospace; font-size: 0.75rem;
    border: 1px solid var(--border); border-bottom: none;
    overflow: hidden;
}
.proj-cover img { width: 100%; height: 100%; object-fit: cover; }
.proj-card-body {
    border: 1px solid var(--border); border-top: none;
    border-radius: 0 0 10px 10px; padding: 16px 18px;
    background: var(--bg-panel);
}
.proj-genre {
    font-family: 'JetBrains Mono', monospace; font-size: 0.68rem;
    color: var(--gold); text-transform: uppercase; letter-spacing: 0.05em;
}
.proj-title { font-family: 'Rajdhani', sans-serif; font-weight: 700; font-size: 1.3rem; margin: 2px 0 6px 0; }
.proj-blurb { color: var(--text-muted); font-size: 0.9rem; }
.tag-chip {
    display: inline-block; font-family: 'JetBrains Mono', monospace; font-size: 0.68rem;
    color: var(--mint); border: 1px solid rgba(45,212,191,0.35);
    background: rgba(45,212,191,0.07);
    padding: 3px 9px; border-radius: 20px; margin: 3px 6px 0 0;
}

/* ---------- quest log (experience) ---------- */
.quest-card { position: relative; padding-left: 20px; }
.quest-card::before {
    content: ""; position: absolute; left: 0; top: 6px; bottom: -8px;
    width: 2px; background: linear-gradient(180deg, var(--violet), transparent);
}
.quest-tag {
    font-family: 'JetBrains Mono', monospace; font-size: 0.65rem;
    color: var(--bg); background: var(--mint);
    padding: 2px 8px; border-radius: 20px; font-weight: 600;
    display: inline-block; margin-bottom: 6px;
}

/* ---------- reviews (testimonials) ---------- */
.review-stars { color: var(--gold); letter-spacing: 2px; font-size: 0.95rem; }
.review-quote { font-style: italic; color: var(--text); margin: 8px 0 10px 0; }
.review-name { font-family: 'Rajdhani', sans-serif; font-weight: 700; }
.review-title { color: var(--text-muted); font-size: 0.82rem; }

/* ---------- achievements (certifications) ---------- */
.ach-card { text-align: center; }
.ach-icon { font-size: 2.1rem; margin-bottom: 6px; }
.ach-rarity {
    font-family: 'JetBrains Mono', monospace; font-size: 0.62rem;
    text-transform: uppercase; letter-spacing: 0.05em;
    padding: 2px 8px; border-radius: 20px; display: inline-block; margin-top: 6px;
}
.rarity-Common { color: #9AA4C4; border: 1px solid #9AA4C4; }
.rarity-Rare { color: var(--mint); border: 1px solid var(--mint); }
.rarity-Epic { color: var(--violet); border: 1px solid var(--violet); }
.rarity-Legendary { color: var(--gold); border: 1px solid var(--gold); }

/* ---------- section heading pattern ---------- */
.sec-head { margin-bottom: 1.4rem; }
.sec-head h2 { font-size: 2rem; margin: 0; }
.sec-sub { color: var(--text-muted); margin-top: 4px; }

/* ---------- misc ---------- */
hr { border-color: var(--border) !important; }
a { color: var(--mint); }
</style>
"""


def inject(st):
    st.markdown(CSS, unsafe_allow_html=True)
