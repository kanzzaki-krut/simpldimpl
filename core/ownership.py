"""Ownership attribution engine."""
from __future__ import annotations

from typing import Iterable, List

from core.fingerprint import KNOWN_SAAS_FINGERPRINTS
from core.schemas import OwnershipRecord, ServiceRecord


DEFAULT_TEAM = "Unknown"


def infer_ownership(services: Iterable[ServiceRecord]) -> List[OwnershipRecord]:
    """Assign a probable team based on detected applications and patterns."""
    results: List[OwnershipRecord] = []
    for service in services:
        detected = (service.detected_app or "").lower()
        probable_team = DEFAULT_TEAM
        evidence = []
        confidence = 0.2
        for fingerprint, team in KNOWN_SAAS_FINGERPRINTS.items():
            if fingerprint in detected:
                probable_team = team
                evidence.append(f"Matched fingerprint: {fingerprint}")
                confidence = 0.8
                break
        results.append(
            OwnershipRecord(
                asset_id=f"{service.ip}:{service.port}",
                probable_team=probable_team,
                confidence_score=confidence,
                evidence=evidence or ["No strong ownership signal"],
            )
        )
    return results
