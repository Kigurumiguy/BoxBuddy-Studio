"""
BoxBuddy Weekly Workshop – Ongoing Creative Drop

Placeholder module for the Weekly Workshop feature.

Purpose:
- Generate a fresh bundle of 3–5 build ideas every week (Playful, Useful, Hybrid + extras)
- Store each week's set in a dated folder under ./Weekly/YYYY-MM-DD
- Work offline via a lightweight creativity algorithm (prompt templates + randomness)
- Produce JSON data and optional printable PDFs for templates/summary

Integration points (expected by the main app):
- Add a "Weekly Workshop" button in the UI that calls run_weekly_workshop()
- On new week or button press, generate a new set if not already created for this week
- Provide simple browsing of previous weeks (e.g., list directories under ./Weekly)

NOTE: This is a placeholder. Replace stubs with real UI hooks and PDF generation.
"""
from __future__ import annotations

import json
import random
from dataclasses import dataclass, asdict
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict, Any

WEEKLY_ROOT = Path("Weekly")  # relative to repo/app root: ./Weekly/

CATEGORIES = ["Playful", "Useful", "Hybrid"]
SKILL_LEVELS = ["Beginner", "Intermediate", "Advanced"]

# Prompt-style templates that the real generator can expand with local randomness.
TITLE_SEEDS = {
    "Playful": [
        "Cardboard Terrarium Lamp",
        "Mini Theater Stage",
        "Tiny City Streetscape",
        "Pocket Arcade Cabinet",
        "Papercraft Creature Buddy",
    ],
    "Useful": [
        "Desk Cable Caddy",
        "Phone Perch Stand",
        "Snack Stash Drawer",
        "Charging Station Cove",
        "Fold-flat Shelf Bin",
    ],
    "Hybrid": [
        "Storage Dragon (Guards Your Snacks)",
        "Habit Tracker Flip-Box",
        "Travel Sketch Folio",
        "Terrarium Night Nook",
        "Memo Mailbox",
    ],
}

MATERIAL_POOL = [
    "cardboard box(es)",
    "paper or cardstock",
    "tape (paper or masking)",
    "white glue or glue stick",
    "scissors or craft knife",
    "ruler",
    "pencil/pen",
    "markers/paints",
    "binder clips or clothespins",
    "recycled clear plastic (window)",
]

DECOR_TIPS = [
    "Add doodle borders and tiny stars.",
    "Ink the edges for a polished look.",
    "Use a single accent color for cohesion.",
    "Cut a peek-through window and back with clear plastic.",
    "Seal edges with paper tape for durability.",
]

DURABILITY_TIPS = [
    "Reinforce corners with folded card triangles.",
    "Laminate stress points with an extra layer of card.",
    "Use small dots of glue, then clamp with clips until dry.",
    "Score fold lines lightly for cleaner bends.",
    "Add a cross-brace where weight is carried.",
]

WHY_KEEP_IT_PHRASES = [
    "It becomes part of your daily flow.",
    "It holds memories and little treasures.",
    "It saves you time every morning.",
    "It displays your personality proudly.",
    "It’s sturdy enough to last and evolve with you.",
]

@dataclass
class Project:
    title: str
    description: str
    category: str  # Playful | Useful | Hybrid
    est_build_time_min: int
    skill_level: str
    materials: List[str]
    steps: List[str]
    decor_tips: List[str]
    durability_tips: List[str]
    why_youll_keep_it: str
    printable_template_pdf: str | None = None  # path to generated PDF (optional)


def _rand_est_time() -> int:
    return random.choice([25, 30, 40, 45, 60, 75, 90])


def _rand_materials(n: int = 6) -> List[str]:
    return random.sample(MATERIAL_POOL, k=min(n, len(MATERIAL_POOL)))


def _gen_description(title: str, category: str) -> str:
    vibe = {
        "Playful": "whimsy and delight",
        "Useful": "tidy efficiency",
        "Hybrid": "clever fun with purpose",
    }[category]
    return f"A {category.lower()} build that brings {vibe} to your space: {title}."


def _gen_steps(category: str) -> List[str]:
    base = [
        "Sketch the outline and take simple measurements.",
        "Cut main panels and score fold lines.",
        "Glue or tape structural seams; let dry.",
        "Test fit moving parts; adjust as needed.",
        "Add decoration and protective reinforcements.",
    ]
    if category == "Useful":
        base.insert(3, "Add supports or dividers for function.")
    if category == "Playful":
        base.insert(3, "Create a playful feature (window, character, or scene).")
    if category == "Hybrid":
        base.insert(3, "Blend a playful accent with a practical compartment.")
    return base


def _rand_title(category: str) -> str:
    return random.choice(TITLE_SEEDS[category])


def _rand_why_keep_it() -> str:
    return random.choice(WHY_KEEP_IT_PHRASES)


def _rand_decor_tips() -> List[str]:
    return random.sample(DECOR_TIPS, k=2)


def _rand_durability_tips() -> List[str]:
    return random.sample(DURABILITY_TIPS, k=2)


def generate_week_bundle(seed: int | None = None) -> List[Project]:
    """Generate 3–5 projects: at least one of each category.

    Works fully offline; randomness can be seeded for repeatability in tests.
    """
    if seed is not None:
        random.seed(seed)

    projects: List[Project] = []

    # Ensure at least one of each
    for cat in CATEGORIES:
        title = _rand_title(cat)
        projects.append(
            Project(
                title=title,
                description=_gen_description(title, cat),
                category=cat,
                est_build_time_min=_rand_est_time(),
                skill_level=random.choice(SKILL_LEVELS),
                materials=_rand_materials(),
                steps=_gen_steps(cat),
                decor_tips=_rand_decor_tips(),
                durability_tips=_rand_durability_tips(),
                why_youll_keep_it=_rand_why_keep_it(),
                printable_template_pdf=None,  # Placeholder: generate later
            )
        )

    # Optionally add 0–2 extras of any category
    extras = random.randint(0, 2)
    for _ in range(extras):
        cat = random.choice(CATEGORIES)
        title = _rand_title(cat)
        projects.append(
            Project(
                title=title,
                description=_gen_description(title, cat),
                category=cat,
                est_build_time_min=_rand_est_time(),
                skill_level=random.choice(SKILL_LEVELS),
                materials=_rand_materials(),
                steps=_gen_steps(cat),
                decor_tips=_rand_decor_tips(),
                durability_tips=_rand_durability_tips(),
                why_youll_keep_it=_rand_why_keep_it(),
                printable_template_pdf=None,
            )
        )

    return projects


def week_folder(date: datetime | None = None) -> Path:
    """Compute the folder path for the given week date (YYYY-MM-DD)."""
    d = date or datetime.now()
    return WEEKLY_ROOT / d.strftime("%Y-%m-%d")


def save_week_bundle(projects: List[Project], date: datetime | None = None) -> Path:
    """Save the bundle to ./Weekly/YYYY-MM-DD as JSON and leave hooks for PDFs."""
    folder = week_folder(date)
    folder.mkdir(parents=True, exist_ok=True)

    data = [asdict(p) for p in projects]
    with open(folder / "bundle.json", "w", encoding="utf-8") as f:
        json.dump({
            "week": folder.name,
            "generated_at": datetime.now().isoformat(),
            "projects": data,
        }, f, ensure_ascii=False, indent=2)

    # Placeholder for optional PDFs:
    # - template PDFs per project (e.g., folder / f"{slug(title)}.pdf")
    # - weekly summary PDF (materials list for all builds)

    return folder


def new_week_needed(last_generated: datetime | None, now: datetime | None = None) -> bool:
    """Decide whether a new week should be generated.

    - If nothing has been generated yet, return True
    - If 7+ days have elapsed since last_generated, return True
    - Otherwise, False
    """
    if last_generated is None:
        return True
    now_dt = now or datetime.now()
    return (now_dt - last_generated) >= timedelta(days=7)


def run_weekly_workshop(force_new: bool = False, seed: int | None = None) -> Path:
    """Main entry point for the app.

    - If force_new is True, always generate a fresh bundle for the current date
    - Else, generate only if a bundle for this week doesn't exist yet
    - Returns the path to the week's folder
    """
    today_folder = week_folder()
    if not force_new and (today_folder / "bundle.json").exists():
        return today_folder

    projects = generate_week_bundle(seed=seed)
    saved = save_week_bundle(projects)
    return saved


# UI copy ideas for tone and personality (used by frontend layer):
WELCOME_LINE = (
    "Welcome to this week’s BoxBuddy Workshop, Andrew! Let’s make something new to keep forever."
)

MAGAZINE_VIBES = [
    "Hey Andrew, it’s Workshop Week — how about a cardboard terrarium lamp?",
    "This week’s Hybrid build: The Storage Dragon — a box that guards your snacks.",
    "New week, new builds, Andrew!",
    "Grab that coffee — we’ve got three new projects waiting in the workshop.",
    "Your cardboard deserves another adventure.",
]

# End of placeholder module.
