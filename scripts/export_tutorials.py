#!/usr/bin/env python3

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
TUTORIALS_DIR = REPO_ROOT / "tutorials"
HTML_DIR = TUTORIALS_DIR / "html"
PDF_DIR = TUTORIALS_DIR / "pdf"
DEFAULT_CHROME_PATHS = (
    Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"),
    Path("/Applications/Chromium.app/Contents/MacOS/Chromium"),
)


def find_chrome() -> str | None:
    for candidate in DEFAULT_CHROME_PATHS:
        if candidate.exists():
            return str(candidate)

    for binary in ("google-chrome", "chromium", "chrome"):
        resolved = shutil.which(binary)
        if resolved:
            return resolved

    return None


def run_command(command: list[str]) -> None:
    subprocess.run(command, check=True, cwd=REPO_ROOT)


def export_html(notebook: Path, output_dir: Path) -> Path:
    run_command(
        [
            "jupyter",
            "nbconvert",
            "--to",
            "html",
            str(notebook),
            "--output-dir",
            str(output_dir),
        ]
    )
    return output_dir / notebook.with_suffix(".html").name


def export_pdf(html_file: Path, output_file: Path, chrome_binary: str) -> None:
    run_command(
        [
            chrome_binary,
            "--headless=new",
            "--disable-gpu",
            "--no-first-run",
            "--allow-file-access-from-files",
            f"--print-to-pdf={output_file}",
            html_file.resolve().as_uri(),
        ]
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Export tutorial notebooks to HTML and PDF."
    )
    parser.add_argument(
        "--format",
        choices=("all", "html", "pdf"),
        default="all",
        help="Which artifacts to export.",
    )
    parser.add_argument(
        "notebooks",
        nargs="*",
        help="Optional notebook paths relative to the repository root.",
    )
    return parser.parse_args()


def resolve_notebooks(args: argparse.Namespace) -> list[Path]:
    if args.notebooks:
        notebooks = [(REPO_ROOT / notebook).resolve() for notebook in args.notebooks]
    else:
        notebooks = sorted(TUTORIALS_DIR.glob("*-Tutorial_*.ipynb"))

    missing = [notebook for notebook in notebooks if not notebook.exists()]
    if missing:
        names = ", ".join(str(path.relative_to(REPO_ROOT)) for path in missing)
        raise FileNotFoundError(f"Notebook(s) not found: {names}")

    return notebooks


def main() -> int:
    args = parse_args()

    try:
        notebooks = resolve_notebooks(args)
    except FileNotFoundError as error:
        print(error, file=sys.stderr)
        return 1

    if not notebooks:
        print("No tutorial notebooks found.", file=sys.stderr)
        return 1

    HTML_DIR.mkdir(parents=True, exist_ok=True)
    PDF_DIR.mkdir(parents=True, exist_ok=True)

    chrome_binary = find_chrome() if args.format in {"all", "pdf"} else None
    if args.format in {"all", "pdf"} and not chrome_binary:
        print(
            "Google Chrome or Chromium is required for PDF export but was not found.",
            file=sys.stderr,
        )
        return 1

    for notebook in notebooks:
        relative_name = notebook.relative_to(REPO_ROOT)
        print(f"Exporting {relative_name}...")

        html_file = HTML_DIR / notebook.with_suffix(".html").name
        if args.format in {"all", "html"} or not html_file.exists():
            html_file = export_html(notebook, HTML_DIR)

        if args.format in {"all", "pdf"}:
            export_pdf(
                html_file=html_file,
                output_file=PDF_DIR / notebook.with_suffix(".pdf").name,
                chrome_binary=chrome_binary,
            )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
