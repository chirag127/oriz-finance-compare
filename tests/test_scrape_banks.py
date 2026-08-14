"""Tests for scripts/scrape_banks.py — cookie loading + prompt template.

The module does `from EdgeGPT.EdgeGPT import Chatbot, ConversationStyle` at
top level. EdgeGPT is an abandoned package that fails to import on modern
Python (needs the removed `pkg_resources`), so we stub it in `sys.modules`
before importing the module. This runs the REAL `scrape_banks` source
(`load_cookies`, `PROMPT_TEMPLATE`, `BANKS`) — the parts under test have no
actual EdgeGPT dependency. No network / EdgeGPT calls are made.
"""

import json
import sys
import types

import pytest


def _import_scrape_banks():
    stub = types.ModuleType("EdgeGPT.EdgeGPT")
    stub.Chatbot = object
    stub.ConversationStyle = types.SimpleNamespace(creative="creative")
    pkg = types.ModuleType("EdgeGPT")
    pkg.EdgeGPT = stub
    sys.modules.setdefault("EdgeGPT", pkg)
    sys.modules.setdefault("EdgeGPT.EdgeGPT", stub)
    import scrape_banks  # noqa: E402

    return scrape_banks


scrape_banks = _import_scrape_banks()


# ---------------------------------------------------------------------------
# load_cookies: env var takes precedence, then file, then error
# ---------------------------------------------------------------------------


def test_load_cookies_from_env(monkeypatch):
    cookies = [{"name": "_U", "value": "abc"}]
    monkeypatch.setenv("BING_COOKIES", json.dumps(cookies))
    assert scrape_banks.load_cookies() == cookies


def test_load_cookies_from_file(monkeypatch, tmp_path):
    monkeypatch.delenv("BING_COOKIES", raising=False)
    cookies = [{"name": "SRCHD", "value": "xyz"}]
    cookies_file = tmp_path / "bing_cookies.json"
    cookies_file.write_text(json.dumps(cookies), encoding="utf-8")
    # load_cookies reads <repo>/bing_cookies.json == parent.parent of the module
    fake_module = tmp_path / "scripts" / "scrape_banks.py"
    monkeypatch.setattr(scrape_banks, "__file__", str(fake_module))
    assert scrape_banks.load_cookies() == cookies


def test_load_cookies_env_precedence_over_file(monkeypatch, tmp_path):
    env_cookies = [{"name": "env"}]
    monkeypatch.setenv("BING_COOKIES", json.dumps(env_cookies))
    fake_module = tmp_path / "scripts" / "scrape_banks.py"
    (tmp_path / "bing_cookies.json").write_text('[{"name":"file"}]', encoding="utf-8")
    monkeypatch.setattr(scrape_banks, "__file__", str(fake_module))
    assert scrape_banks.load_cookies() == env_cookies


def test_load_cookies_missing_raises(monkeypatch, tmp_path):
    monkeypatch.delenv("BING_COOKIES", raising=False)
    fake_module = tmp_path / "scripts" / "scrape_banks.py"  # no cookies file exists
    monkeypatch.setattr(scrape_banks, "__file__", str(fake_module))
    with pytest.raises(RuntimeError, match="No Bing cookies"):
        scrape_banks.load_cookies()


# ---------------------------------------------------------------------------
# Prompt template + bank list are the scrape "contract"
# ---------------------------------------------------------------------------


def test_prompt_template_formats_bank_name():
    out = scrape_banks.PROMPT_TEMPLATE.format(bank="Acme Bank")
    assert "Acme Bank" in out
    assert "{bank}" not in out
    assert "Interest rates" in out


def test_banks_list_nonempty_and_unique():
    assert len(scrape_banks.BANKS) >= 1
    assert len(set(scrape_banks.BANKS)) == len(scrape_banks.BANKS)
    assert all(isinstance(b, str) and b.strip() for b in scrape_banks.BANKS)
