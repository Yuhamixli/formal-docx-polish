# formal-docx-polish 公文格式

Reusable Chinese SOE/public-formal DOCX polishing toolkit.

[![CI](https://github.com/Yuhamixli/formal-docx-polish/actions/workflows/ci.yml/badge.svg)](https://github.com/Yuhamixli/formal-docx-polish/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](./LICENSE)

This repo packages three things together:

1. a Python library for polishing and validating existing `.docx` files
2. a CLI for repeatable batch polishing / validation
3. a Cursor skill bundle for Word brushing workflows

It is designed for high-frequency scenarios such as:

- 国企正式材料刷稿
- 公文/请示/方案/制度/会议材料版式统一
- Word 文档页边距、行距、字号、字体、标题层级统一
- “先校验 -> 再精修 -> 再校验”的可重复流程

## Why this exists

There are many generic DOCX libraries, but very few tools that directly target
the repetitive “formal material brushing” workflow common in Chinese SOE/public
office writing:

- content is already mostly done
- structure is mostly right
- the document still looks inconsistent
- the review feedback is often about spacing, headings, margins, fonts, and tables

This toolkit focuses on that narrow, repeatable layer.

## Scope

This toolkit focuses on:

- page size and margins
- title / subtitle / version / date baseline
- body font, size, line spacing, and first-line indent
- heading hierarchy
- chapter/article structure for regulation-style docs
- table header/body styling
- page-number baseline
- practical validation output

This toolkit does **not** try to fully replace:

- 红头文模板
- 发文字号 / 签发人 / 印章区
- highly custom visual layout with floating shapes and complex art

## Feature summary

| Capability | Status |
| --- | --- |
| Existing `.docx` validation | Yes |
| Existing `.docx` formal polish | Yes |
| Request / plan / report / regulation / meeting profiles | Yes |
| Cursor skill bundle | Yes |
| Synthetic example generator | Yes |
| Strict red-head issuing template | Not yet |
| Visual diff / screenshot verification | Not yet |

## Install

From GitHub:

```bash
pip install "git+https://github.com/Yuhamixli/formal-docx-polish.git"
```

For local development:

```bash
pip install -e .
```

Requires:

- Python 3.11+
- `python-docx`

For local development with tests:

```bash
pip install -e .[dev]
```

## CLI

Validate a document:

```bash
formal-docx-polish validate "input.docx" --kind request --strict
```

Polish into a new file:

```bash
formal-docx-polish polish "input.docx" "output.docx" --kind request
```

Generate synthetic examples:

```bash
python examples/generate_synthetic_examples.py
```

Supported document kinds:

- `generic`
- `request`
- `plan`
- `report`
- `regulation`
- `meeting`

## Python API

```python
from formal_docx_polish import polish_file, validate_file

result = validate_file("request-source.docx", document_kind="request")
print(result["ok"], result["issues"])

polish_file(
    "request-source.docx",
    "request-polished.docx",
    document_kind="request",
)
```

## Typical validation output

```json
{
  "ok": false,
  "document_kind": "request",
  "issues": [
    "top_margin_cm: expected 3.7, got 3.2",
    "heading1 line spacing mismatch: '一、请示背景' expected 28.0, got null"
  ]
}
```

## Repo layout

```text
formal-docx-polish/
├── pyproject.toml
├── src/formal_docx_polish/
│   ├── cli.py
│   ├── profile.py
│   ├── polish.py
│   ├── validate.py
│   └── profiles/
├── cursor-skill/formal-docx-polish/
│   ├── SKILL.md
│   ├── reference.md
│   └── scripts/
├── examples/
│   └── generate_synthetic_examples.py
└── tests/
```

## Cursor skill

The `cursor-skill/formal-docx-polish/` directory can be copied into:

- project skill dir: `.cursor/skills/formal-docx-polish/`
- personal skill dir: `~/.cursor/skills/formal-docx-polish/`

The Cursor skill expects the Python package to be installed first:

```bash
pip install "git+https://github.com/Yuhamixli/formal-docx-polish.git"
```

or for a local clone:

```bash
pip install -e .
```

The skill is intentionally thin. It wraps the same CLI and keeps the workflow
stable:

1. validate source
2. polish into versioned output
3. validate polished output

## Profile customization

The default profile lives in:

- `src/formal_docx_polish/profiles/soe-formal-docx-v1.json`

You can duplicate and adjust it for your own standards.

## Example documents

Run:

```bash
python examples/generate_synthetic_examples.py
```

This creates sanitized synthetic examples under `examples/generated/`, so the
repo can demonstrate the workflow without publishing internal enterprise files.

## Roadmap

- stricter request-ending and主送 checks
- regulation chapter/article continuity checks
- meeting-material structure checks
- optional PyPI publishing
- richer visual verification

## Status

Current version is a practical baseline for SOE/public-formal materials. It is
best used as a repeatable brushing and normalization layer, then followed by a
final human review for strict issuing requirements.

## License

MIT
