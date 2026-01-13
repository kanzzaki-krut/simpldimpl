"""Reporting utilities for JSON, HTML, and PDF outputs."""
from __future__ import annotations

import json
from pathlib import Path
from typing import Optional

from core.schemas import ScanReport


HTML_TEMPLATE = """<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <title>External Exposure Monitor Report</title>
  <style>
    body { font-family: Arial, sans-serif; margin: 2rem; }
    table { border-collapse: collapse; width: 100%; margin-bottom: 2rem; }
    th, td { border: 1px solid #ddd; padding: 0.5rem; text-align: left; }
    th { background: #f5f5f5; }
  </style>
</head>
<body>
  <h1>External Exposure Monitor</h1>
  <p>Asset inventory: {asset_count}</p>
  <p>Service inventory: {service_count}</p>
  <p>Risk summary: {risk_count}</p>
</body>
</html>
"""


def write_json(report: ScanReport, path: Path) -> None:
    path.write_text(report.model_dump_json(indent=2))


def write_html(report: ScanReport, path: Path) -> None:
    html = HTML_TEMPLATE.format(
        asset_count=len(report.assets),
        service_count=len(report.services),
        risk_count=len(report.risks),
    )
    path.write_text(html)


def write_pdf(report: ScanReport, path: Path, html_path: Optional[Path] = None) -> None:
    """Write a placeholder PDF indicator (real renderer integration needed)."""
    data = {
        "notice": "PDF rendering not yet implemented",
        "html_source": str(html_path) if html_path else None,
        "summary": {
            "assets": len(report.assets),
            "services": len(report.services),
            "risks": len(report.risks),
        },
    }
    path.write_text(json.dumps(data, indent=2))
