"""Shared test setup.

`publish.py` raises at import time if MEDIUM_TOKEN is unset (module-level
guard), so we set a dummy token before any test imports it. Tests that
exercise HTTP mock the transport with `responses`; no real network is hit.
"""

import os

os.environ.setdefault("MEDIUM_TOKEN", "test-token")
