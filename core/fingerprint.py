"""Fingerprinting helpers for service identification."""
from __future__ import annotations

from typing import Dict


KNOWN_SAAS_FINGERPRINTS: Dict[str, str] = {
    "gitlab": "DevOps",
    "mattermost": "IT",
    "bitrix": "Marketing",
    "crm": "Sales",
    "minio": "Infrastructure",
    "vpn": "Network",
}
