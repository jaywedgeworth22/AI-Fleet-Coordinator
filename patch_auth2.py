import sys

with open("scripts/mac-collab/mac-collab-server.py", "r") as f:
    content = f.read()

old_authorized = """def authorized(handler: BaseHTTPRequestHandler) -> bool:
    if not TOKEN:
        return False
    auth = handler.headers.get("Authorization", "")
    if auth.lower().startswith("bearer "):
        return token_matches(auth[7:].strip(), TOKEN)
    if auth.lower().startswith("basic ") and basic_authorized(handler):
        # Same browser session that unlocked /board also gets API access —
        # the browser re-sends its cached Basic credentials automatically.
        return True
    return False


def basic_authorized(handler: BaseHTTPRequestHandler) -> bool:
    \"\"\"Gate the /board page itself (not just its data fetches). Username is
    ignored; password is checked against the same MAC_COLLAB_TOKEN. Native
    browser login dialog via 401 + WWW-Authenticate.\"\"\"
    if not TOKEN:
        return False
    auth = handler.headers.get("Authorization", "")
    if not auth.lower().startswith("basic "):
        return False
    try:
        decoded = base64.b64decode(auth[6:].strip()).decode("utf-8", "replace")
    except Exception:
        return False
    parts = decoded.split(":", 1)
    if len(parts) != 2:
        return False
    return token_matches(parts[1], TOKEN)"""

new_authorized = """def authorized(handler: BaseHTTPRequestHandler):
    '''Returns the identity (str) if authorized, else None.'''
    if not TOKENS:
        return None
    auth = handler.headers.get("Authorization", "")
    if auth.lower().startswith("bearer "):
        token_val = auth[7:].strip()
        for t, ident in TOKENS.items():
            if token_matches(token_val, t):
                return ident or "OWNER"
    if auth.lower().startswith("basic "):
        ident = basic_authorized(handler)
        if ident:
            return ident
    return None


def basic_authorized(handler: BaseHTTPRequestHandler):
    \"\"\"Gate the /board page itself (not just its data fetches). Username is
    ignored; password is checked against any MAC_COLLAB_TOKEN. Native
    browser login dialog via 401 + WWW-Authenticate.\"\"\"
    if not TOKENS:
        return None
    auth = handler.headers.get("Authorization", "")
    if not auth.lower().startswith("basic "):
        return None
    try:
        decoded = base64.b64decode(auth[6:].strip()).decode("utf-8", "replace")
    except Exception:
        return None
    parts = decoded.split(":", 1)
    if len(parts) != 2:
        return None
    password = parts[1]
    for t, ident in TOKENS.items():
        if token_matches(password, t):
            return ident or "OWNER"
    return None"""

content = content.replace(old_authorized, new_authorized)

with open("scripts/mac-collab/mac-collab-server.py", "w") as f:
    f.write(content)
