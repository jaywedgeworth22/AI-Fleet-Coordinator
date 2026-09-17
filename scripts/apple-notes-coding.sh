#!/usr/bin/env bash
# Create (or update) an Apple Note in the iCloud "Coding" folder and try to pin it.
# Owner preference 2026-08-05: coding notes always go to Coding + pin to top.
# Owner 2026-08-09: title + timestamp shape (ALL apps, ALL agents):
#
#   Title:  "[APP, Agent] short topic"   e.g. "[UM, Grok] TestFlight first ship"
#           Multi-app: "[ST, CT, Grok] …"  Acronyms: UM ST CT CTS FLEET
#   Row 2:  "Sun, Aug 9, 3:52pm"         local create/update stamp (auto-injected)
#
# Usage:
#   apple-notes-coding.sh "Title" "Plain body text"
#   apple-notes-coding.sh "Title" --html /path/to/body.html
#   Prefer --html for owner-readable notes.  MD path emits <div><br></div>
#   spacers for blank lines, headings, and consecutive list items
#   (owner 2026-08-21: space sections apart; Notes collapses adjacent blocks).
#   apple-notes-coding.sh --update "Title" "Plain body text"   # refreshes timestamp
#   apple-notes-coding.sh --update "Title" --html /path/to/body.html
#   echo "body" | apple-notes-coding.sh "Title"
#   apple-notes-coding.sh --pin-only "Exact Note Title"
#   apple-notes-coding.sh --unpin-only "Exact Note Title"
#   APPLE_NOTES_PIN=0 apple-notes-coding.sh "Title" ...        # skip pinning
#   APPLE_NOTES_ACTIVATE=1 apple-notes-coding.sh "Title" ... # bring Notes to front
#
# Focus policy (owner 2026-08-10): create/update MUST NOT steal focus by default.
# Notes receives AppleScript body edits without activate/show.
#
# Pinning (owner + Claude 2026-08-10): fully headless by DEFAULT via the
# "Pin Coding Note" macOS Shortcut (Receive Text from Share Sheet → Find Note
# where Name contains Shortcut Input + Folder is Coding, limit 1 → Add Note to
# pinned notes). No window, no focus steal, no Accessibility. Unpin twin:
# "Unpin Coding Note" (same, with Remove). First run of each shortcut shows a
# one-time "Allow ... to share with Notes?" dialog — choose Always Allow.
# If the shortcut is missing, pin falls back to the legacy GUI menu-click path,
# which needs Accessibility and steals focus, and only runs with
# --pin / --pin-only / APPLE_NOTES_PIN=1.
# Canonical policy: /Users/jay/apps/AGENT-SYNC.md § Apple Notes.

set -euo pipefail

MODE=create
WANT_PIN=0
WANT_ACTIVATE=0
WANT_NOTIFY=0
NEEDS_OWNER=0
SUMMARY_TEXT=""
PR_NUMBERS="${PR_NUMBERS:-${APPLE_NOTES_PR:-}}"

# Env overrides (agents may set these explicitly).
[[ "${APPLE_NOTES_PIN:-0}" == "1" || "${APPLE_NOTES_PIN:-}" == "true" ]] && WANT_PIN=1
[[ "${APPLE_NOTES_ACTIVATE:-0}" == "1" || "${APPLE_NOTES_ACTIVATE:-}" == "true" ]] && WANT_ACTIVATE=1
[[ "${APPLE_NOTES_NOTIFY:-0}" == "1" || "${APPLE_NOTES_NOTIFY:-}" == "true" ]] && WANT_NOTIFY=1
[[ "${APPLE_NOTES_NEEDS_OWNER:-0}" == "1" || "${APPLE_NOTES_NEEDS_OWNER:-}" == "true" ]] && NEEDS_OWNER=1

TITLE=""
while [[ $# -gt 0 ]]; do
  case "${1:-}" in
    --pin-only)
      MODE=pin
      WANT_PIN=1
      shift || true
      TITLE="${1:-}"
      shift || true
      break
      ;;
    --unpin-only)
      MODE=unpin
      shift || true
      TITLE="${1:-}"
      shift || true
      break
      ;;
    --update)
      MODE=update
      shift || true
      TITLE="${1:-}"
      shift || true
      break
      ;;
    --pin)
      WANT_PIN=1
      shift || true
      ;;
    --activate|--front)
      WANT_ACTIVATE=1
      shift || true
      ;;
    --notify|--pushover)
      WANT_NOTIFY=1
      shift || true
      ;;
    --needs-owner|--action-required)
      NEEDS_OWNER=1
      shift || true
      ;;
    --summary)
      shift || true
      SUMMARY_TEXT="${1:-}"
      shift || true
      ;;
    --pr)
      shift || true
      PR_NUMBERS="${1:-}"
      shift || true
      ;;
    --)
      shift || true
      break
      ;;
    -*)
      echo "unknown flag: $1" >&2
      echo "usage: $0 [--update|--pin-only|--unpin-only|--pin|--activate|--notify|--needs-owner|--summary text|--pr \"18\"] \"Title\" [body | --html path]" >&2
      exit 2
      ;;
    *)
      TITLE="${1:-}"
      shift || true
      break
      ;;
  esac
done

if [[ -z "$TITLE" ]]; then
  echo "usage: $0 [--update|--pin-only|--unpin-only|--pin|--activate|--notify|--needs-owner|--summary text|--pr \"18\"] \"Title\" [body | --html path]" >&2
  exit 2
fi

if [[ "$MODE" == "pin" || "$MODE" == "unpin" ]]; then
  NOTE_ID=$(osascript -e "tell application \"Notes\" to get id of note \"$TITLE\" of folder \"Coding\" of account \"iCloud\"" 2>/dev/null || true)
  [[ -n "$NOTE_ID" ]] || { echo "$MODE-only: note not found in Coding: $TITLE" >&2; exit 3; }
  SKIP_BODY=1
else
  SKIP_BODY=0
fi

# Run a headless pin/unpin Shortcut with the note title as a text-file input.
# Returns 0 on success. First-ever run of each shortcut shows a one-time
# "Allow ... to share with Notes?" dialog — choose Always Allow.
_run_note_shortcut() {  # $1 = shortcut name
  shortcuts list 2>/dev/null | grep -qxF "$1" || return 2
  local tmp
  tmp="$(mktemp).txt"
  printf '%s' "$TITLE" > "$tmp"
  if shortcuts run "$1" -i "$tmp" >/dev/null 2>&1; then
    rm -f "$tmp"
    return 0
  fi
  rm -f "$tmp"
  return 1
}

if [[ "$MODE" == "unpin" ]]; then
  if _run_note_shortcut "Unpin Coding Note"; then
    echo "unpinned: yes (headless via 'Unpin Coding Note' shortcut)"
    exit 0
  elif [[ $? -eq 2 ]]; then
    echo "unpinned: no — 'Unpin Coding Note' shortcut not found. Create it: duplicate 'Pin Coding Note', rename, switch the last action's Add to Remove." >&2
    exit 4
  else
    echo "unpinned: no — 'Unpin Coding Note' shortcut run failed" >&2
    exit 4
  fi
fi

# Markdown → HTML for Notes.app (no external deps). Notes does not render MD.
# Supports: #/##/### headings, **bold**, *italic*, `code`, [text](url),
# -/* bullets, 1. numbered lists, blank-line paragraphs, --- hr.
_md_to_html() {
  # Markdown on stdin → HTML on stdout.
  # IMPORTANT: do NOT use `python3 - <<'PY'` here. That feeds the program on
  # stdin, so `sys.stdin.read()` always sees an empty body (notes with only a
  # title + timestamp). Write the converter to a temp file so stdin stays free
  # for the markdown pipe (owner: empty Grok/agent Notes bodies, 2026-08-10).
  local _md_py
  _md_py=$(mktemp /tmp/apple-notes-md.XXXXXX.py)
  cat >"${_md_py}" <<'PY'
import html, re, sys

# Owner 2026-08-21: Notes.app collapses adjacent blocks.  Blank markdown
# lines used to be dropped, so sections and bullets sat on top of each
# other.  Emit <div><br></div> spacers (same token as --html notes).
SPACER = "<div><br></div>"

def inline(s: str) -> str:
    s = html.escape(s)
    # Notes.app is an HTML renderer — two ASCII spaces collapse.
    # Owner 2026-08-21: sentence gap in HTML is &nbsp; + space.
    s = re.sub(r"([.!?]) {2,}", r"\1&nbsp; ", s)
    # links [text](url) — after escape brackets still match
    s = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        lambda m: f'<a href="{html.escape(m.group(2), quote=True)}">{m.group(1)}</a>',
        s,
    )
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", s)
    s = re.sub(r"(?<!_)_([^_]+)_(?!_)", r"<i>\1</i>", s)
    return s

text = sys.stdin.read()
# normalize newlines
text = text.replace("\r\n", "\n").replace("\r", "\n")
lines = text.split("\n")
out = []
i = 0
in_ul = False
in_ol = False

def last_is_spacer():
    return bool(out) and out[-1] == SPACER

def add_spacer():
    if out and not last_is_spacer():
        out.append(SPACER)

def peek_stripped(j):
    while j < len(lines):
        s = lines[j].strip()
        if s:
            return s
        j += 1
    return ""

def close_lists():
    global in_ul, in_ol
    closed = False
    if in_ul:
        out.append("</ul>")
        in_ul = False
        closed = True
    if in_ol:
        out.append("</ol>")
        in_ol = False
        closed = True
    if closed:
        add_spacer()

while i < len(lines):
    line = lines[i]
    stripped = line.strip()

    # blank → section/bullet air (deduped)
    if stripped == "":
        close_lists()
        add_spacer()
        i += 1
        continue

    # fenced code block
    if stripped.startswith("```"):
        close_lists()
        i += 1
        code_lines = []
        while i < len(lines) and not lines[i].strip().startswith("```"):
            code_lines.append(lines[i])
            i += 1
        if i < len(lines):
            i += 1  # closing fence
        out.append("<pre><code>" + html.escape("\n".join(code_lines)) + "</code></pre>")
        add_spacer()
        continue

    # hr
    if re.fullmatch(r"(-{3,}|\*{3,}|_{3,})", stripped):
        close_lists()
        add_spacer()
        out.append("<hr>")
        add_spacer()
        i += 1
        continue

    # headings
    m = re.match(r"^(#{1,6})\s+(.*)$", stripped)
    if m:
        close_lists()
        add_spacer()
        level = min(len(m.group(1)), 4)  # Notes-friendly h1–h4
        out.append(f"<h{level}>{inline(m.group(2))}</h{level}>")
        add_spacer()
        i += 1
        continue

    # unordered list
    m = re.match(r"^[-*+]\s+(.*)$", stripped)
    if m:
        if in_ol:
            out.append("</ol>")
            in_ol = False
            add_spacer()
        if not in_ul:
            out.append("<ul>")
            in_ul = True
        out.append(f"<li>{inline(m.group(1))}</li>")
        i += 1
        nxt = peek_stripped(i)
        if nxt and re.match(r"^[-*+]\s+", nxt):
            add_spacer()
        continue

    # ordered list
    m = re.match(r"^\d+[.)]\s+(.*)$", stripped)
    if m:
        if in_ul:
            out.append("</ul>")
            in_ul = False
            add_spacer()
        if not in_ol:
            out.append("<ol>")
            in_ol = True
        out.append(f"<li>{inline(m.group(1))}</li>")
        i += 1
        nxt = peek_stripped(i)
        if nxt and re.match(r"^\d+[.)]\s+", nxt):
            add_spacer()
        continue

    # paragraph (merge consecutive non-blank non-special lines)
    close_lists()
    para = [stripped]
    i += 1
    while i < len(lines):
        s2 = lines[i].strip()
        if s2 == "" or s2.startswith("#") or s2.startswith("```") or re.match(r"^[-*+]\s+", s2) or re.match(r"^\d+[.)]\s+", s2) or re.fullmatch(r"(-{3,}|\*{3,}|_{3,})", s2):
            break
        para.append(s2)
        i += 1
    out.append("<p>" + inline(" ".join(para)) + "</p>")

close_lists()
print("<div>" + "".join(out) + "</div>")
PY
  /usr/bin/python3 "${_md_py}"
  local _rc=$?
  rm -f "${_md_py}"
  return ${_rc}
}

# Notes.app collapses ASCII double spaces.  Turn leftover `.  ` / `!  ` / `?  `
# into `&nbsp; ` so sentence gaps survive.  Skip <pre> / <code>.
_html_sentence_gaps() {
  /usr/bin/python3 -c '
import re, sys
s = sys.stdin.read()
parts = re.split(r"(<pre[\s\S]*?</pre>|<code[\s\S]*?</code>)", s, flags=re.I)
out = []
for i, part in enumerate(parts):
    if i % 2 == 1:
        out.append(part)
        continue
    out.append(re.sub(r"([.!?]) {2,}", r"\1&nbsp; ", part))
sys.stdout.write("".join(out))
'
}

BODY_HTML=""
if [[ "$SKIP_BODY" == "0" ]]; then
if [[ "${1:-}" == "--html" ]]; then
  HTML_PATH="${2:-}"
  [[ -n "$HTML_PATH" && -f "$HTML_PATH" ]] || { echo "missing --html file" >&2; exit 2; }
  BODY_HTML=$(cat "$HTML_PATH")
elif [[ -n "${1:-}" ]]; then
  BODY_TEXT="$1"
  BODY_HTML=$(printf '%s' "$BODY_TEXT" | _md_to_html)
elif [[ ! -t 0 ]]; then
  # Wait up to 0.5s for data to avoid hanging forever if called in an environment
  # with an open pipe but no data (e.g. task runners, cron).
  BODY_TEXT=$(/usr/bin/python3 -c 'import sys, select; r, _, _ = select.select([sys.stdin], [], [], 0.5); sys.stdout.write(sys.stdin.read()) if r else None' 2>/dev/null)
  BODY_HTML=$(printf '%s' "$BODY_TEXT" | _md_to_html)
else
  BODY_HTML="<div></div>"
fi
BODY_HTML=$(printf '%s' "$BODY_HTML" | _html_sentence_gaps)

# Title shape check + ensure second-row timestamp (owner 2026-08-09).
# Title: "[APP, Agent] topic" — multi-app OK. Body first line: "Sun, Aug 9, 3:52pm".
# Do NOT put a second markdown # Title in the body — that doubles the title in Notes.
if ! printf '%s' "$TITLE" | grep -Eq '^\[[^]]+\][[:space:]]+'; then
  echo "warning: title should start with [APP, Agent] e.g. \"[UM, Grok] topic\" (got: $TITLE)" >&2
fi
if printf '%s' "$TITLE" | grep -Eiq 'session'; then
  echo "warning: do not put 'session' in Apple Note titles" >&2
fi

_send_pushover_notification() {
  local user_key token secrets_file
  secrets_file="${HOME}/.secrets/global-api-keys"
  if [[ -f "$secrets_file" ]]; then
    user_key=$(grep "^PUSHOVER_USER_KEY=" "$secrets_file" 2>/dev/null | cut -d'=' -f2- | tr -d '"' | tr -d "'" || true)
    token=$(grep "^PUSHOVER_USAGE_API_TOKEN=" "$secrets_file" 2>/dev/null | cut -d'=' -f2- | tr -d '"' | tr -d "'" || true)
    [[ -z "$token" ]] && token=$(grep "^PUSHOVER_ST_API_TOKEN=" "$secrets_file" 2>/dev/null | cut -d'=' -f2- | tr -d '"' | tr -d "'" || true)
    [[ -z "$token" ]] && token=$(grep "^PUSHOVER_CT_API_TOKEN=" "$secrets_file" 2>/dev/null | cut -d'=' -f2- | tr -d '"' | tr -d "'" || true)
  fi

  local msg="${SUMMARY_TEXT:-Apple Note updated in Coding folder}"
  if [[ "$NEEDS_OWNER" == "1" ]]; then
    msg="⚠️ [NEEDS OWNER REVIEW] ${msg}"
  fi

  if [[ -n "${user_key:-}" && -n "${token:-}" ]]; then
    curl -s \
      --form-string "token=${token}" \
      --form-string "user=${user_key}" \
      --form-string "title=${TITLE}" \
      --form-string "message=${msg}" \
      --form-string "sound=pushover" \
      https://api.pushover.net/1/messages.json >/dev/null 2>&1 || true
    echo "notification: sent via Pushover push alert to owner"
  elif command -v osascript >/dev/null 2>&1; then
    osascript -e "display notification \"$msg\" with title \"$TITLE\"" 2>/dev/null || true
    echo "notification: sent via macOS notification"
  fi
}

BODY_HTML=$(printf '%s' "$BODY_HTML" | NEEDS_OWNER="$NEEDS_OWNER" SUMMARY_TEXT="$SUMMARY_TEXT" PR_NUMBERS="$PR_NUMBERS" /usr/bin/python3 -c "
import sys, re, html, os
from datetime import datetime
body = sys.stdin.read()
needs_owner = os.environ.get('NEEDS_OWNER') == '1'
summary_text = os.environ.get('SUMMARY_TEXT', '').strip()
pr_numbers = os.environ.get('PR_NUMBERS', '').strip()
now = datetime.now()
# Sun, Aug 9, 3:52pm — no leading zero on day/hour (portable; avoid %-I)
_h = now.hour % 12 or 12
stamp = (
    now.strftime('%a, %b ')
    + str(now.day)
    + ', '
    + str(_h)
    + ':'
    + now.strftime('%M')
    + now.strftime('%p').lower()
)

def strip_outer_div(s):
    s = s.strip()
    if s.startswith('<div>') and s.endswith('</div>'):
        return s[5:-6]
    return s

inner = strip_outer_div(body).lstrip()
m = re.match(
    r'^(?:<p>)?\s*'
    r'(?:Mon|Tue|Wed|Thu|Fri|Sat|Sun), '
    r'(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) '
    r'\d{1,2}, \d{1,2}:\d{2}[ap]m'
    r'(?:\s*[·|—|-]\s*(?:PR\s*#?\s*[\d\s,#]+)+)?'
    r'\s*(?:</p>)?\s*',
    inner,
    re.I,
)

pr_suffix = ''
if pr_numbers:
    parts = [p.strip() for p in re.split(r'[,|&]', pr_numbers) if p.strip()]
    formatted_prs = []
    for p in parts:
        clean_p = re.sub(r'^(?:PR\s*#?|#)', '', p, flags=re.I).strip()
        if clean_p:
            formatted_prs.append('PR #' + clean_p)
    if formatted_prs:
        pr_suffix = ' · ' + ', '.join(formatted_prs)

if m:
    matched_text = m.group(0)
    inner = inner[m.end():]
    if not pr_suffix:
        # Preserve existing PR divider if found in existing timestamp line
        pr_match = re.search(r'[·|—|-]\s*(PR\s*#?\s*[\d\s,#]+)', matched_text, re.I)
        if pr_match:
            pr_suffix = ' · ' + pr_match.group(1).strip()

stamp += pr_suffix
stamp_p = '<p>' + html.escape(stamp) + '</p><div><br></div>'

extra_blocks = ''
if needs_owner:
    extra_blocks += '<div style=\"background-color: #FFF3CD; border-left: 5px solid #FFC107; color: #856404; padding: 10px 14px; margin-bottom: 12px; border-radius: 4px; font-family: -apple-system, sans-serif;\"><b>⚠️ NEEDS OWNER REVIEW / ACTION</b></div>'
if summary_text:
    extra_blocks += '<div style=\"background-color: #F8F9FA; border-left: 4px solid #0D6EFD; color: #212529; padding: 10px 14px; border-radius: 4px; margin-bottom: 12px; font-family: -apple-system, sans-serif;\"><b>📌 Mobile Quick View:</b> ' + html.escape(summary_text) + '</div>'

sys.stdout.write('<div>' + stamp_p + extra_blocks + inner + '</div>')
")

FULL_HTML=$(/usr/bin/python3 -c '
import html, sys
title = sys.argv[1]
body = sys.argv[2]
print("<h1>" + html.escape(title) + "</h1>" + body)
' "$TITLE" "$BODY_HTML")

TMP=$(mktemp /tmp/apple-note.XXXXXX)
printf '%s' "$FULL_HTML" >"$TMP"
# AppleScript's `system attribute` decodes environment variables as MacRoman, not
# UTF-8 (owner 2026-09-17: a title like "⭐️ Background Jobs Master List" came back
# as "‚≠êÔ∏è Background Jobs Master List", so `note noteTitle of codingFolder` never
# matched the existing note and --update silently created a new one every run — 96
# duplicates piled up this way). Route the title through a UTF-8 temp file and
# `read ... as «class utf8»`, same pattern already used for the HTML body below.
TITLE_FILE=$(mktemp /tmp/apple-note-title.XXXXXX)
printf '%s' "$TITLE" >"$TITLE_FILE"
trap 'rm -f "$TMP" "$TITLE_FILE"' EXIT

if [[ "$MODE" == "update" ]]; then
  NOTE_ID=$(TITLE_FILE="$TITLE_FILE" TMP="$TMP" WANT_ACTIVATE="$WANT_ACTIVATE" osascript <<'EOF'
set titlePath to POSIX file (system attribute "TITLE_FILE")
set noteTitle to read titlePath as «class utf8»
set htmlPath to POSIX file (system attribute "TMP")
set htmlBody to read htmlPath as «class utf8»
tell application "Notes"
  set codingFolder to missing value
  try
    set codingFolder to folder "Coding" of account "iCloud"
  end try
  if codingFolder is missing value then
    tell account "iCloud"
      set codingFolder to make new folder with properties {name:"Coding"}
    end tell
  end if
  set targetNote to missing value
  try
    set targetNote to note noteTitle of codingFolder
  end try
  if targetNote is missing value then
    -- create if missing
    set targetNote to make new note at codingFolder with properties {body:htmlBody}
  else
    set body of targetNote to htmlBody
  end if
  -- Do NOT show/activate by default (steals owner focus). Optional via env.
  if (system attribute "WANT_ACTIVATE") is "1" then
    show targetNote
    activate
  end if
  return id of targetNote
end tell
EOF
)
  echo "updated note id=$NOTE_ID in folder Coding title=$TITLE"
else
  NOTE_ID=$(WANT_ACTIVATE="$WANT_ACTIVATE" osascript <<EOF
set htmlPath to POSIX file "$TMP"
set htmlBody to read htmlPath as «class utf8»

tell application "Notes"
  set codingFolder to missing value
  try
    set codingFolder to folder "Coding" of account "iCloud"
  end try
  if codingFolder is missing value then
    tell account "iCloud"
      set codingFolder to make new folder with properties {name:"Coding"}
    end tell
  end if

  set newNote to make new note at codingFolder with properties {body:htmlBody}
  if (system attribute "WANT_ACTIVATE") is "1" then
    show newNote
    activate
  end if
  return id of newNote
end tell
EOF
)
  echo "created note id=$NOTE_ID in folder Coding"
fi
fi

if [[ "$WANT_NOTIFY" == "1" || "$NEEDS_OWNER" == "1" ]]; then
  _send_pushover_notification
fi

# Preferred pin path (2026-08-10): the "Pin Coding Note" Shortcut runs fully
# headless — no window, no focus steal, no Accessibility needed — so it is ON
# BY DEFAULT (owner preference: pin coding notes when able). The shortcut is:
#   Receive Text from Share Sheet → Find Note (Name contains Shortcut Input,
#   Folder is Coding, limit 1) → Add Note to pinned notes.
# Set APPLE_NOTES_PIN=0 to skip pinning entirely.
if [[ "${APPLE_NOTES_PIN:-}" != "0" ]]; then
  # Settle delay: a just-created/updated note may not be visible to the
  # Shortcut's Find yet (index race) — a miss pops a note picker on the
  # owner's screen. Two seconds reliably clears it (observed 2026-08-10).
  [[ "$MODE" == "create" || "$MODE" == "update" ]] && sleep 2
  if _run_note_shortcut "Pin Coding Note"; then
    echo "pinned: yes (headless via 'Pin Coding Note' shortcut)"
    exit 0
  elif [[ $? -eq 1 ]]; then
    echo "pinned: shortcut run failed; falling back to GUI path if requested" >&2
  fi
fi

# Legacy fallback: GUI pin (needs Accessibility for System Events).
# Requires show+activate + menu click — steals focus. Skipped unless
# --pin / --pin-only / APPLE_NOTES_PIN=1.
if [[ "$WANT_PIN" != "1" ]]; then
  echo "pinned: skipped ('Pin Coding Note' shortcut unavailable; pass --pin for GUI pin, which steals focus)"
  exit 0
fi

# Deterministic selection: re-`show` the exact note by id, then menu-click, with retries —
# the old version pinned whatever happened to be selected, which failed (or could pin the
# wrong note) whenever creation focus was lost (2026-08-08 fix).
PIN_RESULT=$(NOTE_ID="$NOTE_ID" osascript <<'EOF' 2>&1 || true
set noteId to system attribute "NOTE_ID"
set pinned to false
repeat with attempt from 1 to 3
  tell application "Notes"
    try
      show note id noteId
    end try
    activate
  end tell
  delay (0.5 * attempt + 0.4)
  tell application "System Events"
    tell process "Notes"
      repeat with menuName in {"File", "Note", "Edit"}
        try
          if exists menu item "Unpin Note" of menu menuName of menu bar 1 then
            set pinned to true
            exit repeat
          end if
        end try
        try
          set mi to menu item "Pin Note" of menu menuName of menu bar 1
          if enabled of mi then
            click mi
            set pinned to true
            exit repeat
          end if
        end try
      end repeat
    end tell
  end tell
  if pinned then exit repeat
end repeat
if pinned then
  return "pinned"
else
  return "pin-menu-not-found"
end if
EOF
)

if [[ "$PIN_RESULT" == "pinned" ]]; then
  echo "pinned: yes"
elif echo "$PIN_RESULT" | grep -qi 'assistive access\|not allowed'; then
  echo "pinned: no (grant Accessibility to Terminal/iTerm/osascript, or right-click note → Pin Note)"
else
  echo "pinned: no ($PIN_RESULT) — right-click note in list → Pin Note"
fi
