# Appalachian Trail Update Site - Design Plan

## Overview
A minimalist, terminal-friendly blog for posting Appalachian Trail updates. No JavaScript, mostly HTML/CSS, designed for Lynx browser.

## Key Features
1. **Progress Bar** - Shows current mileage vs total goal (e.g., "AT 1234 mi / 2160 mi total")
2. **Current Location** - Hiker's current spot on the trail
3. **Blog Posts** - Chronological list of trail updates
4. **Terminal Aesthetic** - Simple ASCII styling, no fancy CSS

## Site Structure

```
journal/
├── index.html              # Main landing page (progress + latest posts + current location)
├── about-me.html           # About page
├── base.html               # Base template
├── posts/                  # Blog posts directory
├── assets/                 # Static assets
│   ├── css/                # Stylesheets
│   └── images/             # Images (ASCII art, etc.)
├── scripts/                # Server scripts
│   └── server.py           # HTTP server
├── docs/
│   └── agent/              # Agent-specific docs
│       ├── PLAN.md         # This file
│       └── PROMPT.md       # Original prompt
├── README.md
└── AGENTS.md
```

## Mockup 1: Main Index Page

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  Paul's Appalachian Trail Journal                                          │
│  =====================================================================      │
│  PROGRESS BAR:                                                              │
│  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  │
│  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  │
│  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  │
│  PROGRESS: 0/2160 mi (0%)                                                 │
│  ────────────────────────────────────────────────────────────────────────  │
│  CURRENT LOCATION: Not yet started                                        │
│  ────────────────────────────────────────────────────────────────────────  │
│  RECENT UPDATES:                                                           │
│  ────────────────────────────────────────────────────────────────────────  │
│  [2024-09-15] Katahdin Stream Campground (AT 144 mi)                      │
│          5 miles today. First real rain in weeks!                         │
│  ────────────────────────────────────────────────────────────────────────  │
│  [2024-09-14] Baxter State Park (AT 139 mi)                               │
│          7 miles. Moose sighting at mile 23!                              │
│  ────────────────────────────────────────────────────────────────────────  │
│  ────────────────────────────────────────────────────────────────────────  │
│  [BACK TO INDEX] [CURRENT LOCATION] [ABOUT ME]                            │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Mockup 2: Blog Post View

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  Paul's Appalachian Trail Journal                                          │
│  =====================================================================      │
│  PROGRESS: 0/2160 mi (0%)                                                 │
│  ────────────────────────────────────────────────────────────────────────  │
│  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  │
│  ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░  │
│  ────────────────────────────────────────────────────────────────────────  │
│  TODAY'S UPDATE: Katahdin Stream Campground                                │
│  Date: 2024-09-15 | Mile: 144 mi                                           │
│  ────────────────────────────────────────────────────────────────────────  │
│  Today was the first real rain in weeks.                                  │
│  ────────────────────────────────────────────────────────────────────────  │
│  [BACK TO INDEX]                                                           │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Implementation

- **Web files**: Stored at root level for easy editing/deployment
- **Assets**: CSS and images in `assets/` subdirectory
- **Server script**: `scripts/server.py`
- **Documentation**: `docs/agent/`
- **No Gopher**: Simplified to HTTP only

## Next Steps

1. ✅ Create directory structure
2. ✅ Build index.html with progress bar and recent posts
3. ✅ Create post template
4. ✅ Add location page
5. ✅ Implement HTTP server
6. ✅ Style with minimal CSS
7. ⬜ Add actual trail data as Paul starts his hike
8. ⬜ Test site with Lynx browser
9. ⬜ Deploy to a public server
