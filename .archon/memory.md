# Archon Project Memory
> Last full scan: 2026-03-03
> Repository: vediyappanm/ultrathink-doc

## Project Overview
Ultrathink-doc is a documentation/shop site for Ultrathink, deployed on Netlify. It uses a static HTML frontend (`index.html`) with Python backend scripts handling authentication (`auth.py`) and shop logic (`shop.py`). The project has a minimal file structure with Netlify handling deployment.

## Architecture
- `index.html` — primary entry point / frontend
- `src/auth.py` — authentication logic
- `src/shop.py` — shop/commerce logic
- `netlify.toml` — Netlify deployment configuration
- `ultrathink_doc (1).html.html` — likely a stale/duplicate HTML artifact, not actively used

## Tech Stack
- Python (version not specified) — backend scripts
- HTML — frontend/documentation pages
- Netlify — deployment and hosting

## Team Conventions
- Use parameterized queries, not string concatenation for SQL in `src/*.py`
- Use environment variables for secrets, never hardcode credentials in `src/*.py`
- Validate and sanitize all user input before processing in `src/*.py`
- Use specific except clauses, not bare `except:` in `src/*.py`

## Known Weak Areas
- SQL injection risk — `src/*.py` — seen 5+ times (PRs #10, #14)
- Hardcoded secrets/passwords — `src/*.py` — seen 5+ times (PRs #10, #14)
- Bare except clauses — `src/*.py` — seen 4+ times (PRs #10, #14)
- Missing input validation — `src/*.py` — seen 4+ times (PRs #10, #14)
- Stale/duplicate file artifact — `ultrathink_doc (1).html.html` — seen 1 time

## Architecture Decisions
- Static HTML + Python scripts — lightweight documentation site architecture — reviewers: verify no sensitive logic is exposed in HTML files
- Netlify deployment — static hosting with possible serverless functions — reviewers: confirm `netlify.toml` redirects and build settings are appropriate for each environment
- Separate `auth.py` and `shop.py` — concerns are split by domain — reviewers: ensure auth checks are enforced before any shop operations

## Files to Always Check
- `src/auth.py` — check for hardcoded credentials, bare except clauses, parameterized queries, and input validation
- `src/shop.py` — check for SQL injection risks, missing input validation, and proper auth enforcement before operations
- `netlify.toml` — verify environment-specific settings and no secrets committed
- `ultrathink_doc (1).html.html` — verify this stale duplicate is intentional and contains no sensitive data; consider removing

## Manual Overrides
_This section is edited by the team. Preserve any existing content._