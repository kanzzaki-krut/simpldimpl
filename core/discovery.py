"""Asset discovery module for external exposure monitoring."""
from __future__ import annotations

from typing import Iterable, List

from core.schemas import DiscoveryRecord


DISCOVERY_SOURCES = ("amass", "subfinder", "crt.sh", "dnsx", "asn")


def discover_assets(domains: Iterable[str]) -> List[DiscoveryRecord]:
    """Stub discovery that builds normalized records per domain.

    Integrations with amass, subfinder, crt.sh, dnsx, and ASN lookups
    should be added here.
    """
    records: List[DiscoveryRecord] = []
    for domain in domains:
        records.append(
            DiscoveryRecord(
                domain=domain,
                subdomain=f"www.{domain}",
                ip=None,
                cname=None,
                provider_hint=None,
            )
        )
    return records
