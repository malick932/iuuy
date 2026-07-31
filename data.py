"""
====================================================================
 EDIT THIS FILE TO PERSONALIZE YOUR PORTFOLIO
====================================================================
Every piece of text on the site lives here. app.py only handles
layout and styling — you should never need to touch it just to
update your bio, projects, or contact info.

Replace anything inside [ ] brackets. Delete list items you don't
need, or copy/paste one to add more (projects, jobs, certs, etc).
====================================================================
"""

# --------------------------------------------------------------
# PLAYER PROFILE (top of sidebar + hero section)
# --------------------------------------------------------------
PROFILE = {
    "name": "Umer Malik",
    "role": "Unity Game Developer",
    "tagline": "I build high-quality 2D & 3D games for Android • iOS • PC • WebGL",
    "level":100,  # purely cosmetic — bump it whenever you feel like it
    "location": "[Rawalpindi, Pakistan]",
    "avatar": "avatara.png",  # square image, drop your headshot/avatar here
    "status": "Open to work",  # e.g. "Open to work" / "Currently at [Studio]" / "Freelance"
    "hero_stats": [
       {"label": "Years as Unity Developer","value": "3+"},
        {"label": "Projects Completed","value": "20+"},
        {"label": "Cross-Platform Games","value":"4+"},
        {"label": "Clients Served","value": "10+"},
    ],
    "socials": {
        "LinkedIn": "http://www.linkedin.com/in/umer-malik-mu99",
        "Bihance": "https://www.behance.net/umermalick",
        "Email": "malickumer1@gmail.com",
    },
    "resume_pdf": "assets/resume.pdf",  # drop your PDF resume here
}

# --------------------------------------------------------------
# ABOUT ME — origin story + traits
# --------------------------------------------------------------
ABOUT = {
    "portrait": "assets/about_portrait.png",
    "bio_paragraphs": [
        "[Two or three sentences on how you got into game dev — the "
        "spark. What game made you want to build games?]",
        "[A couple sentences on what you focus on now — gameplay "
        "programming, systems design, tools, whatever your specialty is.]",
        "[A sentence on what you're looking for next — the kind of "
        "team, studio, or project that gets you excited.]",
    ],
    "traits": [
        {"label": "Gameplay Programming", "value": 90},
        {"label": "Systems Design", "value": 80},
        {"label": "Team Collaboration", "value": 85},
        {"label": "Shipping Under Deadline", "value": 75},
    ],
    "fun_facts": [
        "[Favorite game of all time: ___]",
        "[Current engine version you swear by: Unity ___]",
        "[A quirky fact — coffee count, speedrun PB, game jam war story]",
    ],
}

# --------------------------------------------------------------
# PROJECTS — your "game library"
# --------------------------------------------------------------
PROJECTS = [
    {
        "title": "[Project Title One]",
        "cover": "assets/projects/project1.png",
        "genre": "Platformer",
        "engine": "Unity / C#",
        "year": "2025",
        "blurb": "[One punchy sentence — what's the hook / core loop?]",
        "description": (
            "[2-4 sentences on the project. What was your role? What "
            "was the biggest technical or design challenge, and how did "
            "you solve it? What are you proudest of?]"
        ),
        "role": "[Solo Dev / Gameplay Programmer / Lead Designer]",
        "platform": "[PC / Mobile / WebGL]",
        "tags": ["Gameplay Systems", "Procedural Generation", "AI/Behavior Trees"],
        "links": {
            "Play": "https://yourusername.itch.io/project-one",
            "Trailer": "https://youtube.com/watch?v=...",
            "Source": "https://github.com/yourusername/project-one",
        },
    },
    {
        "title": "[Project Title Two]",
        "cover": "assets/projects/project2.png",
        "genre": "Top-Down Shooter",
        "engine": "Unity / C#",
        "year": "2024",
        "blurb": "[One punchy sentence — what's the hook / core loop?]",
        "description": (
            "[2-4 sentences on the project — role, challenge, outcome.]"
        ),
        "role": "[Your role]",
        "platform": "[Platform]",
        "tags": ["Multiplayer (Netcode)", "VFX", "UI/UX"],
        "links": {
            "Play": "https://yourusername.itch.io/project-two",
            "Trailer": "",
            "Source": "https://github.com/yourusername/project-two",
        },
    },
    {
        "title": "[Project Title Three]",
        "cover": "assets/projects/project3.png",
        "genre": "Puzzle / VR",
        "engine": "Unity / C#",
        "year": "2023",
        "blurb": "[One punchy sentence — what's the hook / core loop?]",
        "description": (
            "[2-4 sentences on the project — role, challenge, outcome.]"
        ),
        "role": "[Your role]",
        "platform": "[Platform]",
        "tags": ["VR (XR Toolkit)", "Physics", "Level Design"],
        "links": {
            "Play": "",
            "Trailer": "",
            "Source": "https://github.com/yourusername/project-three",
        },
    },
]

# --------------------------------------------------------------
# EXPERIENCE — "quest log"
# --------------------------------------------------------------
EXPERIENCE = [
    {
        "role": "[Job Title]",
        "company": "[Studio / Company Name]",
        "period": "[Mon YYYY] — Present",
        "location": "[City / Remote]",
        "summary": "[One line describing the team/product.]",
        "achievements": [
            "[Quantified win — e.g. shipped feature X used by Y players]",
            "[Another concrete contribution]",
            "[Another concrete contribution]",
        ],
        "reward_tag": "Current Quest",
    },
    {
        "role": "[Previous Job Title]",
        "company": "[Previous Studio Name]",
        "period": "[Mon YYYY] — [Mon YYYY]",
        "location": "[City / Remote]",
        "summary": "[One line describing the team/product.]",
        "achievements": [
            "[Concrete contribution]",
            "[Concrete contribution]",
        ],
        "reward_tag": "Quest Complete",
    },
    {
        "role": "[Internship / Freelance Title]",
        "company": "[Company Name]",
        "period": "[Mon YYYY] — [Mon YYYY]",
        "location": "[City / Remote]",
        "summary": "[One line describing the team/product.]",
        "achievements": [
            "[Concrete contribution]",
        ],
        "reward_tag": "Quest Complete",
    },
]

# --------------------------------------------------------------
# SKILLS — stat sheet, grouped by category
# --------------------------------------------------------------
SKILLS = {
    "Engine & Core": [
        {"name": "Unity (Engine)", "level": 90},
        {"name": "C#", "level": 88},
        {"name": "Gameplay Systems", "level": 85},
        {"name": "Shader Graph / HLSL", "level": 60},
    ],
    "Tools & Pipeline": [
        {"name": "Git / Version Control", "level": 85},
        {"name": "Unity Addressables", "level": 70},
        {"name": "Jira / Trello", "level": 75},
        {"name": "Blender (basic asset prep)", "level": 50},
    ],
    "Specialties": [
        {"name": "Netcode / Multiplayer", "level": 65},
        {"name": "AI / Behavior Trees", "level": 70},
        {"name": "Mobile Optimization", "level": 72},
        {"name": "VR / XR Toolkit", "level": 55},
    ],
    "Soft Skills": [
        {"name": "Cross-discipline Communication", "level": 88},
        {"name": "Scrum / Agile Workflow", "level": 80},
        {"name": "Mentoring", "level": 65},
    ],
}

# --------------------------------------------------------------
# TESTIMONIALS — "player reviews"
# --------------------------------------------------------------
TESTIMONIALS = [
    {
        "quote": "[What did they say about working with you? Keep it real "
                  "and specific — one or two sentences.]",
        "name": "[Reviewer Name]",
        "title": "[Their role — e.g. Lead Producer @ Studio]",
        "rating": 5,
    },
    {
        "quote": "[Another short, specific quote about your impact.]",
        "name": "[Reviewer Name]",
        "title": "[Their role]",
        "rating": 5,
    },
    {
        "quote": "[Another short, specific quote about your impact.]",
        "name": "[Reviewer Name]",
        "title": "[Their role]",
        "rating": 4,
    },
]

# --------------------------------------------------------------
# CERTIFICATIONS — "achievements unlocked"
# --------------------------------------------------------------
CERTIFICATIONS = [
    {
        "title": "[Certified Unity Developer]",
        "issuer": "[Unity Technologies]",
        "date": "[2024]",
        "rarity": "Legendary",  # Common / Rare / Epic / Legendary — cosmetic only
        "icon": "🏆",
        "link": "",
    },
    {
        "title": "[C# Advanced Certification]",
        "issuer": "[Issuing Org]",
        "date": "[2023]",
        "rarity": "Epic",
        "icon": "⚔️",
        "link": "",
    },
    {
        "title": "[Game Design Fundamentals]",
        "issuer": "[Issuing Org / Course]",
        "date": "[2022]",
        "rarity": "Rare",
        "icon": "🛡️",
        "link": "",
    },
]

# --------------------------------------------------------------
# CONTACT
# --------------------------------------------------------------
CONTACT = {
    "headline": "Start a Session",
    "subtext": "Got a project, a role, or just want to talk shaders and "
               "spaghetti code architecture? Send a message.",
    "email": "you@example.com",
    # Optional: Formspree endpoint (formspree.io) makes the form actually
    # send email without a backend. Leave blank to just show a mailto link.
    "formspree_endpoint": "",
}
