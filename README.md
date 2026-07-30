# Finance Compare

[![Stars](https://img.shields.io/github/stars/chirag127/finance-compare?style=flat-square)](https://github.com/chirag127/finance-compare/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](LICENSE)

**Live site: https://finance-compare.oriz.in**

India financial product comparison and analysis hub. Zero-balance bank accounts and private bank data now; stocks and investment products coming next.

---

## What it compares

### Bank accounts (live)

| File | Contents |
|------|----------|
| `data/banks/zero-balance-accounts.md` | 12 zero-balance savings accounts — interest, ATM charges, digital banking fees |
| `data/banks/top-private-banks.md` | Top private banks — branches, ATMs, employees, financials |
| `data/banks/comparison.md` | Consolidated comparison table |
| `data/banks/private-banks.csv` | Raw CSV for private bank metrics |
| `data/banks/notes.md` | Scraped raw notes from EdgeGPT |

### Coming next

- `data/stocks/` — NSE/BSE stock comparison (P/E, dividend yield, 52-week range)
- `data/investments/` — Mutual funds, FD rates, NBFC products

---

## How data is generated

`scripts/scrape_banks.py` uses [EdgeGPT](https://github.com/acheong08/EdgeGPT) to query Bing for each bank's public rate/charge data and writes results to `data/banks/notes.md`.

Cookies are **never hardcoded** — provide via env var or a gitignored file:

```bash
# Option 1: env var
export BING_COOKIES='[{"name":"_U","value":"...","domain":".bing.com",...}]'
python scripts/scrape_banks.py

# Option 2: file (gitignored)
cp bing_cookies.example.json bing_cookies.json
# fill in your cookies
python scripts/scrape_banks.py
```

To publish a markdown file to Medium:

```bash
export MEDIUM_TOKEN=your_medium_integration_token
python scripts/publish.py data/banks/comparison.md -t "Top Zero Balance Accounts in India" -p public
```

---

## View the site locally

```bash
open docs/index.html
# or: python -m http.server 8080 --directory docs
```

---

## Data sources

Data sourced from publicly available bank websites, RBI publications, and BSE/NSE filings. Rates and charges change — verify directly with the bank. This project is for informational comparison only and does not constitute financial advice.

---

MIT License — Chirag Singhal
