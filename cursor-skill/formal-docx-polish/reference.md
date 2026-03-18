# Formal DOCX Polish Reference

## What this repo gives you

This repo combines:

- a Python package
- a CLI
- a Cursor skill

The Cursor skill is intentionally thin. It should call the same toolkit rather
than re-implement the formatting logic.

## Recommended install for Cursor users

Copy:

- `cursor-skill/formal-docx-polish/`

into either:

- `.cursor/skills/formal-docx-polish/`
- `~/.cursor/skills/formal-docx-polish/`

Then make sure the toolkit itself is installed:

```bash
pip install "git+https://github.com/Yuhamixli/formal-docx-polish.git"
```

## What the validator checks

- margins
- cover completeness
- sampled line spacing
- sampled first-line indent
- sampled font size
- first table header emphasis

## Limits

- not a full red-head/government-issuing template engine
- not a visual pixel-perfect diff tool
- best used for iterative brushing of formal materials
