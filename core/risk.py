"""Risk scoring logic for exposed services."""
from __future__ import annotations

from typing import Iterable, List, Tuple

from core.schemas import OwnershipRecord, RiskRecord, ServiceRecord


RISK_RULES: Tuple[Tuple[str, int], ...] = (
    ("admin_interface", 30),
    ("no_auth", 40),
    ("outdated_tls", 10),
    ("cloud_storage", 30),
    ("unknown_owner", 30),
    ("shadow_it", 20),
)


def _score_to_rating(score: int) -> str:
    if score >= 80:
        return "CRITICAL"
    if score >= 50:
        return "HIGH"
    if score >= 20:
        return "MEDIUM"
    return "LOW"


def score_risks(
    services: Iterable[ServiceRecord],
    ownership: Iterable[OwnershipRecord],
) -> List[RiskRecord]:
    """Compute risk scores based on rules and ownership signals."""
    ownership_map = {item.asset_id: item for item in ownership}
    results: List[RiskRecord] = []
    for service in services:
        score = 0
        reasons = []
        asset_id = f"{service.ip}:{service.port}"
        if service.detected_app and any(
            key in service.detected_app.lower()
            for key in ("admin", "grafana", "jira")
        ):
            score += 30
            reasons.append("Admin interface exposed")
        if service.auth_type in (None, "none"):
            score += 40
            reasons.append("No authentication detected")
        if service.tls and service.tls.get("version") in {"TLS1.0", "TLS1.1"}:
            score += 10
            reasons.append("Outdated TLS")
        if service.detected_app and "storage" in service.detected_app.lower():
            score += 30
            reasons.append("Cloud storage exposed")
        owner = ownership_map.get(asset_id)
        if owner and owner.probable_team == "Unknown":
            score += 30
            reasons.append("Unknown owner")
        if owner and owner.confidence_score < 0.4:
            score += 20
            reasons.append("Shadow IT")
        results.append(
            RiskRecord(
                asset_id=asset_id,
                score=score,
                rating=_score_to_rating(score),
                reasons=reasons or ["No elevated risk flags"],
            )
        )
    return results
