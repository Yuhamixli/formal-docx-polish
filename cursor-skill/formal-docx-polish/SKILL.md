---
name: formal-docx-polish
description: Polishes Chinese SOE/public-formal DOCX files and validates margins, fonts, heading hierarchy, line spacing, tables, and cover layout. Use when the user mentions 国标公文格式, 国企正式版式, Word刷稿, DOCX精修, 页边距, 行间距, 字体字号, 标题层级, or formal report formatting.
---

# Formal DOCX Polish

Use this skill when a Word document is already content-stable and now needs
formal polishing.

## Goal

Turn an existing `.docx` into a repeatable SOE/public-formal version with:

- stable margins and page size
- stable font / size / line spacing
- stable heading hierarchy
- stable table styling
- a validation loop instead of eyeballing

## Document-kind mapping

- `01` 请示 -> `request`
- `02` / `04` 方案 -> `plan`
- `03` 研究报告 -> `report`
- `05` 制度框架 -> `regulation`
- `06` 大会方案及主报告 -> `meeting`
- unclear case -> `generic`

## Preferred workflow

1. Validate the source file.
2. Fix source content first if structure is wrong.
3. Polish into a versioned output file.
4. Validate the polished output in strict mode.
5. Report which issues were auto-fixed and which still need manual review.

## Prerequisite

Install the Python package first:

```bash
pip install "git+https://github.com/Yuhamixli/formal-docx-polish.git"
```

## Commands

```bash
python "cursor-skill/formal-docx-polish/scripts/validate_docx.py" "input.docx" --kind request --strict
python "cursor-skill/formal-docx-polish/scripts/polish_docx.py" "input.docx" "output.docx" --kind request
```

## Wrapper scripts

- `run-polish.cmd`
- `run-polish.ps1`
- `validate-docx.cmd`
- `validate-docx.ps1`

## Additional reference

- See [reference.md](reference.md) for profile details and limitations.
