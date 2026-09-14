# Safari Start Page

Jay's Safari new-tab and new-window page.  One self-contained HTML file: no network calls, light theme by default, dark when chosen in Settings (or System).  It is installed as a local `file://` page, so it opens instantly and works offline.  The same file is hosted at `https://jays.services/start/` for iPhone.

## What It Shows

- Clock, date, and greeting in the Mac's own time zone.  Away from US Central it also names the zone's city and long name with its UTC offset and shows Central time underneath.  UTC is always there.
- A search box.  Enter searches Google.  The prefixes `gh`, `b`, `w`, and `yt` go to GitHub, THE BOARD, Wikipedia, and YouTube.  Anything that looks like a URL opens directly, and `/` focuses the box.
- Three link cards: Fleet, Apps, and Infra & Tools.  Fleet apps show their own icons; third-party services show their brand marks.
- A Settings button (gear).  Theme, hide or show any link, add a custom link.  Choices stay in `localStorage` on that device.

## Install (Mac)

```bash
scripts/safari-start/install.sh
```

Copies `index.html` to `~/Sites/safari-start/` and sets Safari's `HomePage`, `NewTabBehavior`, and `NewWindowBehavior` on both the global domain and the sandboxed container plist.  Safari is quit so the keys stick.  `install.sh --revert` restores Safari's built-in Start Page.

If a new tab still shows Apple's Start Page, the container plist was not written or Safari was left running.  Re-run the installer.

## iPhone

iOS Safari has no homepage setting.  After Personal-Site deploys `site/public/start/index.html`:

1. Open `https://jays.services/start/` in Safari.
2. Share → Add to Home Screen (Title: Start).
3. Optional: add that URL to Favorites so it appears on Safari's Start Page.

Below 560px the page uses a phone layout with larger touch rows and safe-area padding.

## Edit

Default links are the `SECTIONS` array in the inline script.  Badge artwork is the `ICONS` table above it.  Re-run `install.sh` after editing, and copy the file to Personal-Site `site/public/start/index.html` when the phone copy should update.
