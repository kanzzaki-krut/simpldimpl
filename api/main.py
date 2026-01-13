"""FastAPI backend for External Exposure Monitor."""
from __future__ import annotations

from datetime import datetime
from typing import Dict, List

from fastapi import FastAPI

from core.discovery import discover_assets
from core.ownership import infer_ownership
from core.report import write_html, write_json, write_pdf
from core.resolver import resolve_assets
from core.risk import score_risks
from core.scanner import scan_services
from core.schemas import ScanReport, ScanRequest
from storage.db import InMemoryStore


app = FastAPI(title="External Exposure Monitor")
store = InMemoryStore()


@app.post("/scan", response_model=ScanReport)
def scan(request: ScanRequest) -> ScanReport:
    assets = resolve_assets(discover_assets(request.domains))
    services = scan_services(assets)
    ownership = infer_ownership(services)
    risks = score_risks(services, ownership)
    report = ScanReport(
        assets=assets,
        services=services,
        ownership=ownership,
        risks=risks,
    )
    store.save(report)
    return report


@app.get("/assets")
def get_assets() -> Dict[str, List[dict]]:
    return {"assets": [item.model_dump() for item in store.report.assets]}


@app.get("/risks")
def get_risks() -> Dict[str, List[dict]]:
    return {"risks": [item.model_dump() for item in store.report.risks]}


@app.get("/report")
def get_report() -> Dict[str, str]:
    timestamp = datetime.utcnow().strftime("%Y%m%d%H%M%S")
    output_dir = store.output_dir
    output_dir.mkdir(parents=True, exist_ok=True)
    json_path = output_dir / f"report-{timestamp}.json"
    html_path = output_dir / f"report-{timestamp}.html"
    pdf_path = output_dir / f"report-{timestamp}.pdf"
    write_json(store.report, json_path)
    write_html(store.report, html_path)
    write_pdf(store.report, pdf_path, html_path=html_path)
    return {
        "json": str(json_path),
        "html": str(html_path),
        "pdf": str(pdf_path),
    }
