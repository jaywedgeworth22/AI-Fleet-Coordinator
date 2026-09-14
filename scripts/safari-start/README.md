# Safari Start Page

Jay's Safari new-tab and new-window page.  One self-contained HTML file: no network calls, light theme by default, dark when macOS is dark.  It is installed as a local `file://` page, so it opens instantly and works offline.

## What It Shows

- Clock, date, and greeting in the Mac's own time zone.  Away from US Central it also names the zone's city and long name with its UTC offset and shows Central time underneath.  UTC is always there.
- A search box.  Enter searches Google.  The prefixes `gh`, `b`, `w`, and `yt` go to GitHub, THE BOARD, Wikipedia, and YouTube.  Anything that looks like a URL opens directly, and `/` focuses the box.
- Three link cards: Fleet, Apps, and Infra & Tools.  Fleet apps show their own icons; third-party services show their brand marks.

## Install

```bash
scripts/safari-start/install.sh
```

Copies `index.html` to `~/Sites/safari-start/` and sets Safari's `HomePage`, `NewTabBehavior`, and `NewWindowBehavior`.  Open a new tab to see it.  `install.sh --revert` restores Safari's built-in Start Page.

## Edit

Links are the `SECTIONS` array in the inline script, one object per link.  Badge artwork is the `ICONS` table above it: fleet app icons come from `agent-logos/app-*.png` shrunk to 96px, brand marks from Simple Icons, and Octicons from Primer, all inlined as data URIs so the page stays a single file.  Re-run `install.sh` after editing.

## iPhone

iOS Safari has no homepage or new-tab setting.  Below 560px the same page switches to a phone layout with larger touch rows and safe-area padding.  Host it somewhere the phone can reach and use Add to Home Screen.
