# Blox Fruits clone — GitHub Pages

## Files
```
index.html        -> redirects to game.html
game.html         -> game page + private server lobby
profile.html      -> profile clone
database.json     -> JSON database
assets/           -> profile images
assets/bf/        -> game images, badges, music
server.py         -> optional local server (not needed on GitHub Pages)
```

## Publish
1. Create a new public repository on GitHub.
2. Upload every file above, keeping the folder structure (`assets/` and `assets/bf/`).
3. Repository **Settings -> Pages -> Build and deployment**
   - Source: **Deploy from a branch**
   - Branch: **main**, folder: **/(root)**
   - Save.
4. Wait ~1 minute. Your link is:
   ```
   https://YOUR_USERNAME.github.io/YOUR_REPO/
   ```

## How it works on GitHub Pages
- Paths are relative, so the site works at any repository subpath.
- `database.json` loads from the same folder.
- The Discord webhook is called directly from the browser. Discord returns CORS headers for `*.github.io`, so no backend is required.
- If the direct call fails, the page falls back to `notify` (used by the optional local `server.py`).

## Local run (optional)
```
python server.py
```
Then open `http://127.0.0.1:8900/`.
