#!/usr/bin/env python3
from __future__ import annotations

import os
import pathlib
import sys


def main() -> int:
    project_root = pathlib.Path(__file__).resolve().parent
    venv_dir = project_root / ".venv"

    print("Python executable:", sys.executable)
    print("Python version:", sys.version.split()[0])
    print("Venv directory exists:", venv_dir.exists())

    in_venv = sys.prefix != getattr(sys, "base_prefix", sys.prefix)
    print("Running inside virtual environment:", in_venv)

    try:
        import virtualenv  # type: ignore
    except Exception as exc:  # pragma: no cover
        print("virtualenv import: FAILED")
        print("Reason:", exc)
        return 1

    print("virtualenv import: OK")
    print("virtualenv version:", virtualenv.__version__)

    expected_fragment = os.path.join(str(project_root), ".venv")
    if expected_fragment not in sys.executable:
        print("Warning: interpreter does not appear to come from this project's .venv")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
