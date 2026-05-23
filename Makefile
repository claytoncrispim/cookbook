.PHONY: setup verify

setup:
	python3 -m venv .venv
	. .venv/bin/activate && python -m pip install --upgrade pip
	. .venv/bin/activate && python -m pip install -r requirements.txt

verify:
	. .venv/bin/activate && python verify_env.py
