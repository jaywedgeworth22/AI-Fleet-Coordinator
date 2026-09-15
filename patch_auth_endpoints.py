import sys

with open("scripts/mac-collab/mac-collab-server.py", "r") as f:
    content = f.read()

old_update = """    def _handle_finding_update(self, finding_id: str):
        if not authorized(self):
            return self._deny_auth()
        data, err = self._read_json_body()
        if err:
            return self._send(400, {"error": err})
        fields = {}
        if "status" in data:
            if data["status"] not in STATUSES:
                return self._send(400, {"error": "invalid_status", "allowed": STATUSES})
            fields["status"] = data["status"]
        if "addressed_by" in data:
            fields["addressed_by"] = data["addressed_by"]
        if "reported_by" in data:
            fields["reported_by"] = data["reported_by"]"""

new_update = """    def _handle_finding_update(self, finding_id: str):
        ident = authorized(self)
        if not ident:
            return self._deny_auth()
        data, err = self._read_json_body()
        if err:
            return self._send(400, {"error": err})
        fields = {}
        if "status" in data:
            if data["status"] not in STATUSES:
                return self._send(400, {"error": "invalid_status", "allowed": STATUSES})
            fields["status"] = data["status"]
        if "addressed_by" in data:
            if ident != "OWNER" and data["addressed_by"] and data["addressed_by"] != ident:
                return self._send(403, {"error": "forbidden", "message": f"Token is scoped to '{ident}'"})
            fields["addressed_by"] = data["addressed_by"]
        if "reported_by" in data:
            if ident != "OWNER" and data["reported_by"] and data["reported_by"] != ident:
                return self._send(403, {"error": "forbidden", "message": f"Token is scoped to '{ident}'"})
            fields["reported_by"] = data["reported_by"]"""

old_comment = """    def _handle_comment_create(self, finding_id: str):
        if not authorized(self):
            return self._deny_auth()
        data, err = self._read_json_body()
        if err:
            return self._send(400, {"error": err})
        author = str(data.get("author", "")).strip()
        text = str(data.get("text", "")).strip()"""

new_comment = """    def _handle_comment_create(self, finding_id: str):
        ident = authorized(self)
        if not ident:
            return self._deny_auth()
        data, err = self._read_json_body()
        if err:
            return self._send(400, {"error": err})
        author = str(data.get("author", "")).strip()
        if ident != "OWNER" and author and author != ident:
            return self._send(403, {"error": "forbidden", "message": f"Token is scoped to '{ident}'"})
        text = str(data.get("text", "")).strip()"""

content = content.replace(old_update, new_update)
content = content.replace(old_comment, new_comment)

with open("scripts/mac-collab/mac-collab-server.py", "w") as f:
    f.write(content)
