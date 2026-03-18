# Publishing

This repo is prepared as a standalone public repository scaffold.

## 1. Create a clean standalone repo

Recommended: copy or move the `formal-docx-polish/` directory out as its own
repository root before publishing.

## 2. Initialize git

```bash
git init
git add .
git commit -m "Initial public release"
```

## 3. Create GitHub repo with `gh`

```bash
gh repo create formal-docx-polish --public --source=. --remote=origin --push
```

If you want a description:

```bash
gh repo create formal-docx-polish --public --description "Chinese SOE/public-formal DOCX polish and validation toolkit" --source=. --remote=origin --push
```

## 4. Suggested first release checklist

1. Replace placeholder author / URLs in `pyproject.toml` if needed.
2. Add sanitized example documents under `examples/`.
3. Add one screenshot or GIF showing before/after polishing.
4. Add badges for PyPI and GitHub Actions if you later publish them.
5. Verify the Cursor skill path examples in `README.md`.

## 5. Optional next steps

- publish to PyPI
- add GitHub Actions for tests
- add more profiles for stricter issuing formats
- add semantic release / version tags
