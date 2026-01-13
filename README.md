# External Exposure Monitor (EEM)

External Exposure Monitor (EEM) is a modular pipeline that discovers, maps, and assesses an organization's external attack surface. It focuses on exposure visibility and shadow IT control rather than vulnerability scanning.

## Core workflow

```
Domain → Subdomain → IP → Ports → Services → Ownership → Risk → Report
```

## Repository layout

```
/core
    discovery.py
    resolver.py
    scanner.py
    fingerprint.py
    ownership.py
    risk.py
    report.py
/api
    FastAPI backend
/agents
    external_scanner
/web
    simple dashboard
/storage
    PostgreSQL or SQLite abstractions
```

## API endpoints

- `POST /scan` – run a scan for one or more domains
- `GET /assets` – list discovered assets
- `GET /risks` – list scored risks
- `GET /report` – generate JSON/HTML/PDF reports

## Security requirements

- No data leaves the system
- No destructive scanning
- Respect `robots.txt` for HTTP crawling
- Apply rate limiting for network operations

## MVP scope

- Support 1 domain
- Up to 1000 subdomains
- Up to 100 IPs
- Full scan in under 30 minutes
