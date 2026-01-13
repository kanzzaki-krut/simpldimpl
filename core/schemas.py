"""Normalized JSON schemas used across pipeline modules."""
from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import BaseModel, Field


class DiscoveryRecord(BaseModel):
    domain: str
    subdomain: Optional[str] = None
    ip: Optional[str] = None
    cname: Optional[str] = None
    provider_hint: Optional[str] = None


class ServiceRecord(BaseModel):
    ip: str
    port: int
    protocol: str
    service: Optional[str] = None
    version: Optional[str] = None
    tls: Optional[Dict[str, str]] = None
    headers: Optional[Dict[str, str]] = None
    auth_type: Optional[str] = None
    detected_app: Optional[str] = None


class OwnershipRecord(BaseModel):
    asset_id: str
    probable_team: str
    confidence_score: float = Field(ge=0.0, le=1.0)
    evidence: List[str]


class RiskRecord(BaseModel):
    asset_id: str
    score: int
    rating: str
    reasons: List[str]


class ScanRequest(BaseModel):
    domains: List[str]
    asns: Optional[List[str]] = None
    ip_ranges: Optional[List[str]] = None


class ScanReport(BaseModel):
    assets: List[DiscoveryRecord]
    services: List[ServiceRecord]
    ownership: List[OwnershipRecord]
    risks: List[RiskRecord]
