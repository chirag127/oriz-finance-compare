"""publish.py - Publish markdown files to Medium via API.

MEDIUM_TOKEN must be set as env var (never hardcoded).
"""

import argparse
import os

import requests

TOKEN = os.environ.get("MEDIUM_TOKEN")
if not TOKEN:
    raise RuntimeError("Set MEDIUM_TOKEN env var.")

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; rv:91.0) Gecko/20100101 Firefox/91.0",
}


def get_author_id():
    r = requests.get("https://api.medium.com/v1/me", headers=HEADERS)
    r.raise_for_status()
    return r.json()["data"]["id"]


def read_file(filepath):
    with open(filepath) as f:
        content = f.read()
    ext = filepath.rsplit(".", 1)[-1] if "." in filepath else ""
    if ext == "md":
        ext = "markdown"
    return {"content": content, "contentFormat": ext}


def post_article(args):
    author_id = get_author_id()
    data = {"title": args["title"], **read_file(args["filepath"])}
    if args["tags"]:
        data["tags"] = [t.strip() for t in args["tags"].split(",")]
    data["publishStatus"] = args.get("pub") or "draft"
    r = requests.post(
        f"https://api.medium.com/v1/users/{author_id}/posts",
        headers=HEADERS,
        json=data,
    )
    print(r.status_code, r.json())
    if r.status_code in (200, 201):
        return r.json()["data"]["url"]
    return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filepath")
    parser.add_argument("-t", "--title", required=True)
    parser.add_argument("-a", "--tags", required=False)
    parser.add_argument("-p", "--pub", choices=["public", "unlisted", "draft"])
    args = parser.parse_args()
    print(post_article(vars(args)))
