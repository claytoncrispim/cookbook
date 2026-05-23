# Cookbook

A production-minded Django project inspired by the Smartnotes app from LinkedIn Learning's Django Essential Training.

Portfolio positioning: a privacy-aware CRUD product that demonstrates practical backend engineering, product thinking, and clean project communication.

## Project Proposition

Cookbook is a notes-style web application where users can create personal content, control visibility, and selectively share public entries.

Value delivered:

- solves a real product need: private note-taking with optional public sharing
- demonstrates full-stack web fundamentals in Django
- highlights secure-by-default decisions around ownership and visibility
- presents code and docs in a format suitable for technical review by recruiters and hiring teams

## Product Scope (Smartnotes Context)

This implementation follows the Smartnotes learning project pattern and includes the same core behavior:

- account lifecycle flows: sign up, log in, log out, and farewell flow
- user-owned notes via ForeignKey relationships
- privacy control for each note with an is_public flag
- shareable links for public notes
- popular notes that respect privacy boundaries
- Bootstrap-based UI customization

## Tech Stack

- Python 3.12
- Django 6
- SQLite
- Bootstrap (CDN)

## Feature Highlights

- Authentication and session flows aligned with modern Django behavior
- Access control enforcing user ownership on note operations
- Public endpoints that expose only explicitly public notes
- Mix of class-based views for CRUD and function-based views for focused state transitions
- POST-only logout compatibility for Django 5+ and 6+

## Quick Start

From the project root:

```bash
python3 --version
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open the app at http://127.0.0.1:8000/

## Safe Retrofit for Existing GitHub Repos

If the repository already exists and has been pushed, you can still initialize Django safely without rewriting history:

```bash
source .venv/bin/activate
python -m pip install django
django-admin startproject cookbook .
python manage.py check
git add .
git commit -m "Initialize Django project structure"
git push
```

Why this is safe:

- the command writes Django files into the current repository
- history remains linear (no force push required)
- previous commits stay intact

## Project Commands

```bash
make setup
make verify
python manage.py check
python manage.py migrate
python manage.py runserver
```

## Roadmap

Completed foundation:

- authentication and user-specific note ownership
- public/private visibility model
- share-link behavior for public notes
- repository bootstrap automation and environment verification

Next feature milestones:

- rich note metadata: tags, categories, and favorites
- improved discovery: search, filters, and sort options
- author experience: draft mode and archive/restore actions
- quality improvements: test coverage for permission and visibility rules
- product polish: improved UI consistency and accessibility checks

## Repository Layout

- manage.py: Django management entry point
- cookbook/: Django project package (settings, urls, wsgi, asgi)
- requirements.txt: pinned Python dependencies
- verify_env.py: local environment verification script
- PYTHON_VENV_SETUP_STEPS.md: setup log and command history
- .gitignore: common Python and Django ignores

## Deployment

Deployment platform is intentionally undecided at this stage.

Planned deployment readiness work:

- move secrets and environment config to environment variables
- production-safe settings split (dev vs production)
- static file strategy and security hardening checklist
- CI checks for migrations, tests, and linting before release

## Engineering Notes

- Local SQLite database is ignored by git by default.
- For production deployment, set DEBUG=False and use environment-based secrets.

## What I Learned

- How to design ownership-first data models where each note is tied to a specific authenticated user.
- How to enforce privacy boundaries so public endpoints never expose private user data.
- How to balance class-based views for maintainable CRUD flows with function-based views for focused state changes.
- How to bootstrap and document a project so another engineer can run it quickly with predictable results.

## Contribution and Testing

For reviewers and collaborators:

- Keep changes small and feature-focused; open one pull request per feature or bug fix.
- Add or update tests when behavior changes, especially around access control and visibility rules.
- Run local quality checks before pushing:

```bash
python manage.py check
python manage.py test
make verify
```

Suggested branch naming:

- `feature/<short-description>`
- `fix/<short-description>`
- `docs/<short-description>`

## Implementation Updates

- 2026-05-23: Initialized Django project in-place within existing repository, added environment automation, and polished README for portfolio presentation.
