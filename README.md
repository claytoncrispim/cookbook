# Cookbook

Minimal Python project bootstrap for a Python + Django-style workflow.

## Requirements

- Python 3.12+
- bash shell

## Quick Start

From the project root, run:

```bash
python3 --version
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## Verify Setup

Run:

```bash
make verify
```

Expected checks:

- project virtual environment exists
- Python is running from `.venv`
- `virtualenv` imports correctly

## Make Targets

```bash
make setup
make verify
```

## Project Files

- `requirements.txt`: Python dependencies
- `verify_env.py`: local environment verification script
- `PYTHON_VENV_SETUP_STEPS.md`: detailed setup log and command history
- `.gitignore`: common Python and Django ignores

## Deactivate Environment

```bash
deactivate
```
