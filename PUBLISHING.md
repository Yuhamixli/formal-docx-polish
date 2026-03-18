# Publishing

Repository URL:

- `https://github.com/Yuhamixli/formal-docx-polish`

## 1. Local development

```bash
pip install -e .[dev]
pytest -q
python examples/generate_synthetic_examples.py
```

## 2. Commit changes

```bash
git add .
git commit -m "Describe the change"
```

## 3. Push to GitHub

```bash
git push
```

## 4. Suggested release checklist

1. Regenerate synthetic examples if profile behavior changed.
2. Add one screenshot or GIF showing before/after polishing.
3. Verify install instructions in `README.md`.
4. Verify Cursor skill paths and wrapper scripts.
5. Check GitHub Actions CI status after push.

## 5. Optional next steps

- publish to PyPI
- add GitHub Actions for tests
- add more profiles for stricter issuing formats
- add semantic release / version tags
