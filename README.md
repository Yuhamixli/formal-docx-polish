# formal-docx-polish

Reusable Chinese SOE/public-formal DOCX polishing toolkit.

This repo packages three things together:

1. a Python library for polishing and validating existing `.docx` files
2. a CLI for repeatable batch polishing / validation
3. a Cursor skill bundle for Word brushing workflows

It is designed for high-frequency scenarios such as:

- 国企正式材料刷稿
- 公文/请示/方案/制度/会议材料版式统一
- Word 文档页边距、行距、字号、字体、标题层级统一
- “先校验 -> 再精修 -> 再校验”的可重复流程

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

## Install

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

Supported document kinds:

- `generic`
- `request`
- `plan`
- `report`
- `regulation`
- `meeting`

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
└── tests/
```

## Cursor skill

The `cursor-skill/formal-docx-polish/` directory can be copied into:

- project skill dir: `.cursor/skills/formal-docx-polish/`
- personal skill dir: `~/.cursor/skills/formal-docx-polish/`

The Cursor skill expects the Python package to be installed first:

```bash
pip install formal-docx-polish
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

## Status

Current version is a practical baseline for SOE/public-formal materials. It is
best used as a repeatable brushing and normalization layer, then followed by a
final human review for strict issuing requirements.

## License

MIT
