from __future__ import annotations

import argparse
import json
from pathlib import Path

from formal_docx_polish.polish import polish_file
from formal_docx_polish.validate import validate_file


KINDS = ["generic", "request", "plan", "report", "regulation", "meeting"]


def _default_output(path: Path) -> Path:
    return path.with_name(f"{path.stem}（版式精修）{path.suffix}")


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="formal-docx-polish",
        description="Chinese SOE/public-formal DOCX polish and validation toolkit.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    validate_parser = subparsers.add_parser("validate", help="Validate an existing DOCX")
    validate_parser.add_argument("input", help="Source .docx file")
    validate_parser.add_argument("--kind", default="generic", choices=KINDS)
    validate_parser.add_argument("--strict", action="store_true")

    polish_parser = subparsers.add_parser("polish", help="Polish an existing DOCX")
    polish_parser.add_argument("input", help="Source .docx file")
    polish_parser.add_argument("output", nargs="?", help="Target .docx file")
    polish_parser.add_argument("--kind", default="generic", choices=KINDS)
    return parser


def main() -> int:
    parser = _build_parser()
    args = parser.parse_args()

    if args.command == "validate":
        payload = validate_file(args.input, document_kind=args.kind)
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 2 if args.strict and not payload["ok"] else 0

    output_path = args.output or str(_default_output(Path(args.input)))
    payload = polish_file(args.input, output_path, document_kind=args.kind)
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
