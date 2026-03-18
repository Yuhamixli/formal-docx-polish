from __future__ import annotations

import json
from importlib.resources import files
from typing import Any


def _deep_merge(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    merged = dict(base)
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key] = _deep_merge(merged[key], value)
        else:
            merged[key] = value
    return merged


def load_profile(document_kind: str = "generic") -> dict[str, Any]:
    profile_path = files("formal_docx_polish.profiles").joinpath("soe-formal-docx-v1.json")
    data = json.loads(profile_path.read_text(encoding="utf-8"))
    base = data["base"]
    kind_cfg = data.get("kinds", {}).get(document_kind, {})
    return _deep_merge(base, kind_cfg)
