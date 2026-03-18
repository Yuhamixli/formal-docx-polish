# Contributing

Thanks for contributing to `formal-docx-polish`.

## Development setup

```bash
pip install -e .[dev]
```

## Before opening a PR

Run:

```bash
pytest -q
```

If you change behavior or profiles, also try the CLI manually on one synthetic
example:

```bash
python examples/generate_synthetic_examples.py
formal-docx-polish validate "examples/generated/request-source.docx" --kind request
formal-docx-polish polish "examples/generated/request-source.docx" "examples/generated/request-polished.docx" --kind request
```

## Design rules

- Keep the scope narrow: brushing and normalization, not a full issuing system.
- Prefer profile-driven behavior over hard-coded special cases.
- Avoid embedding organization-specific secrets, templates, or internal samples.
- Keep Cursor skill wrappers thin; the Python package should stay the canonical logic owner.
- Add or update tests when changing polish or validation behavior.

## Good contribution areas

- new document profiles
- better validation rules
- safer table normalization
- sanitized synthetic example generation
- packaging and release improvements

## Out of scope for now

- seals, stamps, and signature images
- full red-head issuing templates
- heavyweight Word COM-only workflows as the default path
