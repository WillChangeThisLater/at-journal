# Appalachian Trail Journal

Static site for my [hopefully minimalist blog](https://willchangethislater.github.io/at-journal/) which will document my trials and tribulations on the A.T.

## Quick Start

```bash
python3 -m http.server 8000
```

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
4. **IMPORTANT**: Update these values in the new post (they'll be copied from the template):
   - **Location**: Change from "Titusville, NJ" to your current location (e.g., "Damascus, VA")
   - **Progress**: Change from "0/2160 mi (0%)" to your current progress (e.g., "470/2160 mi (21.76%)")
   - **Mile marker**: Update the meta data to reflect your actual mile (e.g., "470 mi")
5. Update the post content
6. Add a link in `index.html`:
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
