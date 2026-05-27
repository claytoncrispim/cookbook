# Cookbook 🍲

**Privacy-aware Django recipe app** where users can create recipes, keep them private, publish selected ones, and share public recipe pages.

Built as a portfolio project inspired by the Smartnotes app from LinkedIn Learning's Django Essential Training, with the recipe domain used to demonstrate practical CRUD design, authentication, visibility rules, and product-minded documentation.

> This project is designed to show more than basic Django setup: it focuses on ownership, access control, public sharing rules, and a repo presentation style that is easy for recruiters and other engineers to review.

---

## Live Demo

https://cookbook-web-4w16.onrender.com/

---

## 📷 Screenshot

![A screenshot of the Cookbook application showing the recipe interface and Bootstrap-based layout.](./static/images/Screenshot%20from%202026-05-24%2018-12-24.png)

---

## ✨ Features

### 1. User accounts and session flows

- Sign up, log in, and log out with Django auth views adapted to project-specific templates.
- Redirect behavior configured explicitly so login and logout land on meaningful app pages.
- Ownership-sensitive pages only expose edit/delete controls to the recipe author.

### 2. Recipe CRUD workflow

- Create, read, update, and delete recipes through Django class-based views.
- Recipes store title, description, ingredients, instructions, timestamps, likes, and visibility state.
- Each recipe belongs to one authenticated user through a `ForeignKey` relationship.

### 3. Public and private visibility model

- Authors can keep recipes private or mark them public.
- Private recipes remain visible only to their owner.
- Public recipes can be discovered by other users and accessed through shareable links.

### 4. Share page with privacy-aware behavior

- Public recipes can be opened by the author, other logged-in users, and anonymous visitors.
- Private recipes show a warning to the owner explaining that the recipe must be public before sharing.
- Non-owners never learn that a missing recipe is private; they only see a generic "not found or removed" style message.

### 5. Popular recipes and lightweight discovery

- Popular page lists public recipes with at least one like.
- Main recipe list includes the current user's own recipes plus other users' public recipes.
- Like actions are protected so private recipes are not exposed through direct URL access.

### 6. Bootstrap-based UI

- Lightweight interface built with Django templates and Bootstrap 5.
- Navigation adapts to authentication state.
- Templates were renamed and normalized from the original notes-oriented learning project into the recipe domain.

---

## 🧱 Tech Stack

**Backend**

- Python 3.12
- Django 6
- SQLite
- python-dotenv

**Frontend / templating**

- Django templates
- Bootstrap 5 (CDN)

**Environment / tooling**

- `venv`
- `virtualenv`
- Makefile helpers

---

## 🗺️ Architecture

```text
root
├── cookbook/
│   ├── settings.py        # Django settings, env loading, auth redirects
│   ├── urls.py            # Project-level routing
│   ├── asgi.py
│   └── wsgi.py
├── home/
│   ├── urls.py            # Landing page and auth-related routes
│   ├── views.py           # Home, login, logout, register, farewell
│   └── templates/home/
├── recipes/
│   ├── models.py          # Recipe model and ownership relationship
│   ├── forms.py           # ModelForm for recipe creation and editing
│   ├── urls.py            # CRUD, share, like, visibility toggle routes
│   ├── views.py           # Class-based CRUD + share/privacy logic
│   ├── admin.py
│   ├── migrations/
│   └── templates/recipes/
├── static/
│   ├── images/
│   └── templates/base.html
├── manage.py
├── requirements.txt
├── Makefile
└── verify_env.py
```

**Key routes**

- `/` - landing page
- `/login/` - login page
- `/register/` - registration page
- `/smart/recipes/` - recipe list
- `/smart/recipes/popular/` - popular public recipes
- `/smart/recipes/<id>/` - recipe detail page
- `/smart/recipes/<id>/share/` - privacy-aware share page

---

## 🚀 Getting Started (local dev)

### 1. Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/cookbook.git
cd cookbook
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Create your environment file

Create a `.env` file in the project root:

```bash
SECRET_KEY=your_django_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

You can also copy values from `.env.example` and replace the placeholders.

### 5. Apply migrations

```bash
python manage.py migrate
```

### 6. Run the project

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

---

## 📦 Project Commands

```bash
make setup
make verify
python manage.py check
python manage.py migrate
python manage.py test
python manage.py runserver
```

---

## 🧪 Interesting implementation details

- **Environment-first configuration**
	- `SECRET_KEY`, `DEBUG`, and `ALLOWED_HOSTS` are loaded from `.env`.
	- Missing required values fail fast via `ImproperlyConfigured`.

- **Ownership-driven data model**
	- Every recipe belongs to a Django `User` through the `author` field.
	- Reverse access is available through `related_name='recipes'`.

- **Privacy-aware route behavior**
	- Detail and share pages allow public recipes to be seen by other users.
	- Private recipes remain accessible only to their author.
	- Direct action endpoints are guarded so hidden recipes are not exposed by guessed URLs.

- **Learning-project retrofit**
	- The app started from a Smartnotes-style tutorial structure.
	- Naming and templates were normalized from notes to recipes without changing the core product logic.

---

## 🔮 Roadmap / ideas

- Add search and filtering by ingredient, title, and author.
- Introduce recipe categories, tags, and favorites.
- Improve test coverage around permissions, sharing, and visibility transitions.
- Add pagination for recipe list and popular recipes.
- Improve accessibility and mobile polish across templates.
- Explore image upload support for recipes.

---

## 📦 Deployment notes

Deployment is intentionally not finalized yet, but the project is already structured to support a production pass.

- Move to production-safe settings with `DEBUG=False`.
- Use environment variables or a secret manager for deployed secrets.
- Add static file handling strategy for production.
- Introduce CI checks for migrations, tests, and health validation.

---

## 🙋 About the author

This project was designed and built by **Clayton Crispim** as a hands-on way to:

- Practice Django in a realistic CRUD product scenario.
- Work through authentication, permissions, and public/private access rules.
- Build a repository that reads like a portfolio artifact, not just a tutorial dump.

I’m actively building portfolio projects while targeting Junior / Entry-level software roles.

---

## 📄 License

This project is currently shared for portfolio and learning purposes.
If you would like to reuse part of it, please open an issue or reach out first.

---

## 🏗️ How I would extend this in a production setting

If this were a real product, I would:

- Add automated tests for the main visibility and sharing rules.
- Replace SQLite with PostgreSQL.
- Add pagination, search indexing, and caching for public recipe discovery.
- Add image uploads and richer recipe metadata.
- Introduce role-aware moderation or abuse reporting for public recipes.
- Add observability, structured logging, and deployment pipelines.

---

## 📝 Implementation updates

- 2026-05-23: Initialized the Django project in-place, added environment automation, and documented the setup for portfolio presentation.
- 2026-05-24: Added auth redirect configuration, normalized recipe ownership accessors, and refined share/list visibility behavior.
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
