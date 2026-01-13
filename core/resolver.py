"""DNS resolver helpers for discovery pipeline."""
from __future__ import annotations

from typing import Iterable, List

from core.schemas import DiscoveryRecord


def resolve_assets(records: Iterable[DiscoveryRecord]) -> List[DiscoveryRecord]:
    """Placeholder resolver that returns records unchanged.

    Extend with DNS resolution for A/AAAA/CNAME records.
    """
    return list(records)
