"""Tests for scripts/publish.py — Medium publishing.

HTTP is mocked with `responses`; no real network calls. `read_file` is a
pure parser (file ext -> Medium contentFormat) tested against real temp files.
"""

import json

import pytest
import responses

import publish

ME_URL = "https://api.medium.com/v1/me"
POSTS_URL_TMPL = "https://api.medium.com/v1/users/{author}/posts"


# ---------------------------------------------------------------------------
# read_file: ext -> contentFormat mapping (the parser)
# ---------------------------------------------------------------------------


def test_read_file_md_maps_to_markdown(tmp_path):
    f = tmp_path / "post.md"
    f.write_text("# Hello", encoding="utf-8")
    out = publish.read_file(str(f))
    assert out == {"content": "# Hello", "contentFormat": "markdown"}


def test_read_file_html_keeps_ext(tmp_path):
    f = tmp_path / "post.html"
    f.write_text("<h1>Hi</h1>", encoding="utf-8")
    out = publish.read_file(str(f))
    assert out["contentFormat"] == "html"
    assert out["content"] == "<h1>Hi</h1>"


def test_read_file_no_extension_gives_empty_format(tmp_path):
    f = tmp_path / "README"
    f.write_text("plain", encoding="utf-8")
    out = publish.read_file(str(f))
    assert out["contentFormat"] == ""


def test_read_file_dotted_name_uses_last_segment(tmp_path):
    # rsplit(".", 1) means "my.post.md" -> "md" -> "markdown"
    f = tmp_path / "my.post.md"
    f.write_text("x", encoding="utf-8")
    assert publish.read_file(str(f))["contentFormat"] == "markdown"


# ---------------------------------------------------------------------------
# get_author_id: HTTP mocked
# ---------------------------------------------------------------------------


@responses.activate
def test_get_author_id_returns_id():
    responses.add(responses.GET, ME_URL, json={"data": {"id": "author-123"}}, status=200)
    assert publish.get_author_id() == "author-123"
    # bearer header is sent
    assert responses.calls[0].request.headers["Authorization"].startswith("Bearer ")


@responses.activate
def test_get_author_id_raises_on_http_error():
    responses.add(responses.GET, ME_URL, json={"errors": []}, status=401)
    with pytest.raises(Exception):
        publish.get_author_id()


# ---------------------------------------------------------------------------
# post_article: HTTP mocked, tag + publishStatus logic
# ---------------------------------------------------------------------------


def _mock_me(author="a1"):
    responses.add(responses.GET, ME_URL, json={"data": {"id": author}}, status=200)


@responses.activate
def test_post_article_returns_url_on_success(tmp_path):
    _mock_me("a1")
    posts_url = POSTS_URL_TMPL.format(author="a1")
    responses.add(
        responses.POST,
        posts_url,
        json={"data": {"url": "https://medium.com/@x/post-1"}},
        status=201,
    )
    f = tmp_path / "a.md"
    f.write_text("body", encoding="utf-8")

    url = publish.post_article(
        {"title": "T", "filepath": str(f), "tags": "a, b ,c", "pub": "public"}
    )
    assert url == "https://medium.com/@x/post-1"

    sent = json.loads(responses.calls[1].request.body)
    assert sent["title"] == "T"
    assert sent["contentFormat"] == "markdown"
    # tags split + stripped
    assert sent["tags"] == ["a", "b", "c"]
    assert sent["publishStatus"] == "public"


@responses.activate
def test_post_article_defaults_to_draft_when_pub_missing(tmp_path):
    _mock_me("a2")
    responses.add(
        responses.POST,
        POSTS_URL_TMPL.format(author="a2"),
        json={"data": {"url": "u"}},
        status=200,
    )
    f = tmp_path / "b.md"
    f.write_text("body", encoding="utf-8")

    # no tags, no pub -> publishStatus draft, no tags key
    publish.post_article({"title": "T", "filepath": str(f), "tags": None})
    sent = json.loads(responses.calls[1].request.body)
    assert sent["publishStatus"] == "draft"
    assert "tags" not in sent


@responses.activate
def test_post_article_returns_none_on_failure(tmp_path):
    _mock_me("a3")
    responses.add(
        responses.POST,
        POSTS_URL_TMPL.format(author="a3"),
        json={"errors": [{"message": "bad"}]},
        status=400,
    )
    f = tmp_path / "c.md"
    f.write_text("body", encoding="utf-8")

    assert publish.post_article({"title": "T", "filepath": str(f), "tags": None}) is None
