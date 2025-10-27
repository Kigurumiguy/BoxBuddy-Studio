# 📦 BoxBuddy-Studio
> 
*Your creative sanctuary for building amazing cardboard box creations!*

Welcome to **BoxBuddy-Studio** – a cozy corner of the internet dedicated to the wonderful world of cardboard crafting! Whether you're building castles, rockets, robots, or anything your imagination dreams up, this is your go-to resource for offline-friendly guides, printable templates, and a supportive community of makers.

## 🌟 What is BoxBuddy-Studio?
BoxBuddy-Studio is all about celebrating creativity without screens! We believe that the best adventures start with a simple cardboard box and a bit of imagination. This project provides:
- **Offline-first design** – All guides can be downloaded and used without an internet connection
- **Printable templates** – Ready-to-print patterns, cutting guides, and instruction sheets
- **Step-by-step tutorials** – Clear, friendly instructions for makers of all ages and skill levels
- **Community support** – A welcoming space to share your creations and get inspired
- **No special tools needed** – Most projects require only basic supplies: boxes, scissors, tape, and markers!

## ✨ Features
- Core project guides with materials, steps, and printable patterns
- Offline browsing and local storage of your builds
- Friendly maker tone and encouragement throughout the app
- NEW: Weekly Workshop mode (see below)

### 🗞️ Weekly Workshop – Ongoing Creative Drop
Bring a little magazine magic to your making. Each week, BoxBuddy automatically creates a fresh bundle of 3–5 projects — one Playful, one Useful, one Hybrid, plus a couple of random extras — designed to be meaningful, practical, and fun to keep.

How it works:
- Generates a new set every 7 days, or instantly when you click “Weekly Workshop → New Week”
- Stores each bundle locally in a dated folder: `./Weekly/YYYY-MM-DD/`
- Saves data as JSON, with optional printable PDFs for templates and a weekly summary
- Works fully offline using a local creativity algorithm (prompt templates + randomness)
- Lightweight scheduling via Python `datetime` checks, no external services required

What each project includes:
- Title and short description
- Category: Playful, Useful, or Hybrid
- Estimated build time and skill level
- Required materials (only everyday items)
- Step-by-step instructions
- Decoration and durability tips
- “Why You’ll Keep It” — a quick note on long-term value
- Optional printable template (PDF) with cut/fold lines

Visual style and tone:
- Layout mimics a mini magazine spread: a playful cover, individual project pages, and a printable summary sheet
- Cozy, encouraging voice of a creative coach:
  - “Hey Andrew, it’s Workshop Week — how about a cardboard terrarium lamp?”
  - “This week’s Hybrid build: The Storage Dragon — a box that guards your snacks.”
  - “Grab that coffee — we’ve got three new projects waiting in the workshop.”

UI Integration:
- Adds a “Weekly Workshop” button to the main screen
- Clicking it runs the generator, creating this week’s bundle if needed
- Includes a “See Last Week’s Builds” link to browse previous folders
- On trigger, BoxBuddy greets you with: “Welcome to this week’s BoxBuddy Workshop, Andrew! Let’s make something new to keep forever.”

Developer notes:
- Module: `weekly_workshop.py`
- Entry point: `run_weekly_workshop(force_new: bool = False, seed: int | None = None)`
- Data format: `./Weekly/YYYY-MM-DD/bundle.json` with an array of projects; optional PDFs may be added alongside
- Safe to call repeatedly — it will reuse the current week’s bundle unless `force_new=True`

## 🎨 Project Categories
### 🏰 Castles & Forts
Build epic fortresses, cozy hideaways, and medieval castles. Perfect for imaginative play!

### 🚀 Vehicles & Transportation
Cars, rockets, boats, trains – if it moves (or looks like it should!), we've got a guide for it.

### 🤖 Robots & Characters
Create friendly robots, dinosaurs, animals, and other characters to populate your cardboard world.

### 🎭 Playsets & Scenes
Markets, theaters, puppet stages, and more – build entire worlds from cardboard.

### 🎲 Games & Activities
From marble runs to board games, discover interactive cardboard projects.

## 📚 Getting Started
1. **Browse the guides** – Check out our collection of projects in the `/guides` folder
2. **Download templates** – Grab printable PDFs from the `/templates` directory
3. **Gather supplies** – Cardboard boxes, scissors, tape, glue, markers/paint
4. **Start creating** – Follow along at your own pace, and make each project your own!
5. **Share your work** – Post photos in Discussions to inspire others

## 🛠️ Supply Suggestions
Most projects use common household items:
- Cardboard boxes (various sizes)
- Scissors or box cutter (adults only for sharp tools!)
- Tape (masking, duct, or packing tape)
- Non-toxic glue or glue sticks
- Markers, crayons, or paint
- Ruler and pencil for measuring
- Optional: String, fabric scraps, bottle caps, and other found materials

## 💡 Philosophy
At BoxBuddy-Studio, we believe:
- **Everyone is creative** – You don't need special artistic skills to make something amazing
