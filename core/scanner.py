"""Port and service scanning pipeline stages."""
from __future__ import annotations

from typing import Iterable, List

from core.schemas import DiscoveryRecord, ServiceRecord


SCAN_STAGES = ("masscan", "nmap", "httpx", "nuclei")


def scan_services(assets: Iterable[DiscoveryRecord]) -> List[ServiceRecord]:
    """Stub scanner that returns empty results.

    Implement masscan -> nmap -> httpx -> nuclei sequencing here.
    """
    _ = list(assets)
    return []
