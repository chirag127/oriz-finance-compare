"""
scrape_banks.py - EdgeGPT-based bank data scraper.

Cookies loaded from env var or gitignored bing_cookies.json.
Never hardcode cookies in source.

Usage:
    # Option 1: JSON file (gitignored)
    cp bing_cookies.example.json bing_cookies.json
    # fill in your Bing cookies, then:
    python scripts/scrape_banks.py

    # Option 2: env var
    BING_COOKIES='[{"name":"_U","value":"...","domain":".bing.com",...}]' python scripts/scrape_banks.py
"""

import asyncio
import json
import os
from pathlib import Path

from EdgeGPT.EdgeGPT import Chatbot, ConversationStyle


def load_cookies() -> list:
    env_val = os.environ.get("BING_COOKIES")
    if env_val:
        return json.loads(env_val)
    cookies_file = Path(__file__).parent.parent / "bing_cookies.json"
    if cookies_file.exists():
        return json.loads(cookies_file.read_text())
    raise RuntimeError(
        "No Bing cookies. Set BING_COOKIES env var or create bing_cookies.json. "
        "See bing_cookies.example.json. Never commit real cookies."
    )


BANKS = [
    "RBL Basic Savings Account",
    "IDFC First Bank Pratham Savings Account",
    "IndusInd Bank Indus Online Savings Account",
    "YES Bank Smart Salary Advantage",
    "Utkarsh Basic Savings Bank Deposit Account (BSBDA)",
    "AU Digital Savings Account",
    "Kotak Mahindra Bank 811 Digital Bank Account",
    "HDFC Bank BSBDA",
    "Standard Chartered Bank Aasaan",
    "State Bank of India BSBDA",
    "Jupiter Money Bank Account",
    "Fi money Bank Account",
]

PROMPT_TEMPLATE = """Answer these questions in a markdown table for {bank}:
1. Interest rates - savings account up to 1 lakh and FD for 1 year.
2. ATM charges for cash withdrawal, balance inquiry, and debit card charges.
3. Number of branches, ATMs, and employees.
4. Chequebook charges and passbook charges.
5. SMS alert charges.
6. Net banking, mobile banking, and UPI charges."""

OUTPUT_FILE = Path(__file__).parent.parent / "data" / "banks" / "notes.md"


async def scrape():
    cookies = load_cookies()
    with open(OUTPUT_FILE, "a") as f:
        for bank in BANKS:
            bot = await Chatbot.create(cookies=cookies)
            response = await bot.ask(
                prompt=PROMPT_TEMPLATE.format(bank=bank),
                conversation_style=ConversationStyle.creative,
            )
            reply = response["item"]["messages"][1]["text"]
            print(f"--- {bank} ---\n{reply}")
            f.write(f"\n## {bank}\n\n{reply}\n")
            await bot.close()


if __name__ == "__main__":
    asyncio.run(scrape())
