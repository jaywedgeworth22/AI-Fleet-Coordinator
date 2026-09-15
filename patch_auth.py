import sys

with open("scripts/mac-collab/mac-collab-server.py", "r") as f:
    content = f.read()

old_load_token = """def load_token() -> str:
    env = os.environ.get("MAC_COLLAB_TOKEN", "").strip()
    if env:
        return env
    if SECRETS.is_file():
        for line in SECRETS.read_text().splitlines():
            s = line.strip()
            if s.startswith("export "):
                s = s[7:]
            if s.startswith("MAC_COLLAB_TOKEN="):
                return s.split("=", 1)[1].strip().strip('"').strip("'")
    return ""


TOKEN = load_token()"""

new_load_token = """def load_tokens() -> dict[str, str]:
    '''Returns a mapping of {token: identity}. 
    MAC_COLLAB_TOKEN maps to None (legacy admin/root), 
    MAC_COLLAB_TOKEN_X maps to "X" (e.g. "AG", "CODEX").'''
    tokens = {}
    # 1. From env vars directly (less common for the full list)
    for k, v in os.environ.items():
        if k.startswith("MAC_COLLAB_TOKEN") and v.strip():
            identity = k[len("MAC_COLLAB_TOKEN_"):] if k != "MAC_COLLAB_TOKEN" else None
            tokens[v.strip()] = identity
            
    # 2. From secrets file
    if SECRETS.is_file():
        for line in SECRETS.read_text().splitlines():
            s = line.strip()
            if s.startswith("export "):
                s = s[7:]
            if s.startswith("MAC_COLLAB_TOKEN"):
                parts = s.split("=", 1)
                if len(parts) == 2:
                    k = parts[0].strip()
                    v = parts[1].strip().strip('"').strip("'")
                    if v:
                        identity = k[len("MAC_COLLAB_TOKEN_"):] if k != "MAC_COLLAB_TOKEN" else None
                        tokens[v] = identity
    return tokens

TOKENS = load_tokens()
TOKEN = next((t for t, ident in TOKENS.items() if ident is None), None) # Fallback for legacy basic auth checks
"""

content = content.replace(old_load_token, new_load_token)

with open("scripts/mac-collab/mac-collab-server.py", "w") as f:
    f.write(content)
