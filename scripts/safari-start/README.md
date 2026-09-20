# Safari Start Page

Jay's Safari new-tab and new-window page.  One self-contained HTML file that follows the System theme by default (Light or Dark can be forced in Settings).  It is installed as a local `file://` page, so it opens instantly and works offline.  The only network call is search autocomplete: as you type, the box shows suggestions from this page's own links plus live web suggestions from `start.jays.services/suggest` (a Google Suggest proxy) — and it degrades silently to just the on-page matches when offline.  The same file is hosted at `https://jays.services/start/` for iPhone.

## What It Shows

- Clock, date, and greeting in the Mac's own time zone.  Away from US Central it also names the zone's city and long name with its UTC offset and shows Central time underneath.  UTC is always there.
- A search box that works like a browser URL bar.  Typing opens a suggestions dropdown: matching Start-Page links (every fleet app and repo) first, then live web autocomplete.  Arrow keys move through it, Enter opens the highlighted row, Tab fills the box, Escape closes it.  Enter with nothing highlighted searches Google.  The prefixes `gh`, `b`, `w`, and `yt` go to GitHub, THE BOARD, Wikipedia, and YouTube.  Anything that looks like a URL opens directly, and `/` focuses the box.
- Three link cards: Fleet, Apps, and Infra & Tools.  Fleet apps show their own icons; third-party services show their brand marks.  The Fleet card includes every repo in `fleet-apps.json` (including Harness and congress-trading-shared).
- A Settings button (gear).  Theme, hide or show any link, add a custom link.  Choices stay in `localStorage` on that device.

## Install (Mac)

```bash
scripts/safari-start/install.sh
```

Copies `public/index.html` to `~/Sites/safari-start/` and sets Safari's `HomePage`, `NewTabBehavior`, and `NewWindowBehavior` on both the global domain and the sandboxed container plist.  Safari is quit so the keys stick.  `install.sh --revert` restores Safari's built-in Start Page.

If a new tab still shows Apple's Start Page, the container plist was not written or Safari was left running.  Re-run the installer.

## Hosted

The same page is public at https://start.jays.services, served from `public/` as Cloudflare Worker static assets (`wrangler.jsonc`, account Usage.Jays.Services, zone `jays.services`).  The Worker (`worker.js`) also answers `GET /suggest?q=…`, proxying Google Suggest and adding permissive CORS so the search box's web autocomplete works from the deployed site, the `file://` install, and the `jays.services/start/` copy alike.  The page carries a `noindex` tag and a `robots.txt` that disallows crawling.  Deploy after editing:

```bash
cd scripts/safari-start && wrangler deploy
```

`wrangler` needs a login that can reach the Usage.Jays.Services account (`wrangler login`, or the Cloudflare keys from the handoff file as environment variables).

## iPhone

iOS Safari has no homepage or new-tab setting, so on the phone the page is a home-screen app.  Open https://start.jays.services in Safari, tap Share, then Add to Home Screen.  It opens full screen, and links open in an in-app browser sheet with a Done button that returns to the launcher.  Below 560px the page uses a phone layout with larger touch rows and safe-area padding.
