# Examples

This repo prefers sanitized or synthetic examples instead of internal enterprise
materials.

## Generate examples

```bash
python examples/generate_synthetic_examples.py
```

Generated files will be written to:

- `examples/generated/request-source.docx`
- `examples/generated/request-polished.docx`
- `examples/generated/plan-source.docx`
- `examples/generated/regulation-source.docx`
- `examples/generated/request-validation.json`

These examples are intended for:

- manual smoke testing
- README screenshots later
- CI-adjacent local verification
