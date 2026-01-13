"""Storage layer for EEM."""
from __future__ import annotations

from pathlib import Path

from core.schemas import ScanReport


class InMemoryStore:
    def __init__(self, output_dir: Path | None = None) -> None:
        self.output_dir = output_dir or Path("./reports")
        self.report = ScanReport(assets=[], services=[], ownership=[], risks=[])

    def save(self, report: ScanReport) -> None:
        self.report = report
