# Paul's Appalachian Trail Journal

A minimalist, terminal-friendly blog for documenting my Appalachian Trail journey.

## Quick Start

```bash
cd /home/paul/repos/journal
python3 scripts/server.py
# Access via: http://localhost:8080
```

Or with Python's built-in server:
```bash
python3 -m http.server 8000
# Access via: http://localhost:8000
```

## Viewing in Lynx

```bash
lynx http://localhost:8080
```

Or in a regular browser: `http://localhost:8080`

## Directory Structure

```
journal/
├── index.html              # Main landing page (includes current location)
├── about-me.html           # About page
├── base.html               # Base template
├── posts/                  # Blog posts (post-001.html, etc.)
├── assets/                 # Static assets
│   ├── css/               # Stylesheets
│   └── images/            # Images (ASCII art, etc.)
├── scripts/                # Server scripts
│   └── server.py          # HTTP server
├── docs/                   # Documentation
│   └── agent/             # Agent/planning docs
├── README.md               # This file
└── AGENTS.md               # Agent instructions
```

## Adding a New Post

1. Navigate to `posts/`
2. Create a new file: `post-NNN.html`
   (Replace NNN with the next sequential number)
3. Copy `post-001.html` as a template
4. Update the post content
5. Add a link in `index.html`:
   ```html
   <article class="blog-post">
       <h3>
           <span class="post-date">[2024-09-20]</span> 
           <span class="post-mile">Trail Name (AT XXX mi)</span>
       </h3>
       <p>Trail summary...</p>
       <p><a href="post-NNN.html">Read more →</a></p>
   </article>
   ```

## Features

- **Progress Bar**: Shows current mileage vs. total goal (2,160 mi)
- **Current Location**: Display where you are on the trail
- **Blog Posts**: Chronological trail updates
- **Terminal-First**: Works perfectly in Lynx and other text browsers
- **Static**: No database or backend required
- **Minimalist**: Pure HTML/CSS, no JavaScript

## Trail Progress

- **Total Distance**: 2,160 miles
- **Current Progress**: 0 miles (0%)
- **Current Location**: Not yet started
- **Start Date**: TBD

## Notes

- The site is designed to be minimalist and work in the simplest browsers
- No JavaScript is required - works in Lynx, links, and other text-only browsers
- Static site - no database or backend required
