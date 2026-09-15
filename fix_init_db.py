with open("scripts/mac-collab/mac-collab-server.py", "r") as f:
    content = f.read()

dup = """        if "claimed_at" not in existing_cols:
            conn.execute("ALTER TABLE findings ADD COLUMN claimed_at TEXT")
        if "claimed_at" not in existing_cols:
            conn.execute("ALTER TABLE findings ADD COLUMN claimed_at TEXT")"""
clean = """        if "claimed_at" not in existing_cols:
            conn.execute("ALTER TABLE findings ADD COLUMN claimed_at TEXT")"""

content = content.replace(dup, clean)

with open("scripts/mac-collab/mac-collab-server.py", "w") as f:
    f.write(content)
