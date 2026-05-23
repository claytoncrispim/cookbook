# Python Virtual Environment Setup Steps

Date: 2026-05-23
Project: `/home/clayton/dev-projects/cookbook`

## 1) Check if Python is installed

Run:

```bash
/usr/bin/python --version
python3 --version
```

Observed output:

```text
Python 3.12.3
Python 3.12.3
```

## 2) Configure Python environment for the workspace

Action taken (via VS Code Python environment tooling):

- Configured the workspace Python environment.
- Active interpreter resolved to:

```text
/home/clayton/dev-projects/cookbook/.venv/bin/python
```

## 3) Install virtual environment package

Installed package:

```text
virtualenv
```

Equivalent command form:

```bash
/home/clayton/dev-projects/cookbook/.venv/bin/python -m pip install virtualenv
```

## 4) Verify the virtual environment directory exists

Run:

```bash
ls -d .venv
```

Observed output:

```text
.venv
```

## 5) Activate the virtual environment (bash)

Run:

```bash
source .venv/bin/activate
```

## 6) Deactivate when finished

Run:

```bash
deactivate
```

## Quick Start (Teammates)

Run these in project root:

```bash
python3 --version
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install virtualenv
```

## Automation Added

The following helper files were added to streamline setup and verification:

- `requirements.txt` with:

```text
virtualenv
```

- `Makefile` targets:

```bash
make setup
make verify
```

- `verify_env.py` script, which checks:
	- active Python executable
	- Python version
	- `.venv` directory presence
	- virtual environment activation status
	- `virtualenv` import and version

Latest verification output:

```text
Python executable: /home/clayton/dev-projects/cookbook/.venv/bin/python
Python version: 3.12.3
Venv directory exists: True
Running inside virtual environment: True
virtualenv import: OK
virtualenv version: 21.3.3
```
