# Ancient Languages / ThamudicEpiPlatform Integration

This directory is the integration/deployment layer for the canonical implementation maintained in `amerhwitat/nlp/ThamudicEpiPlatform`.

## Capabilities

- Historical-object PDF import with bounded extraction and page provenance.
- Research PDF export containing objects, scripts, scholarly transliteration, literal/meaning translations, confidence, provenance and citations.
- **Intelligent OCR scanner integration** for historical inscriptions and manuscript images, with image-quality analysis, pluggable Kraken/Tesseract adapters, confidence, script routing, bounding boxes and SHA-256 provenance.
- KPI dashboard contract shared by the API and language clients.
- Integration manifests and SHA-256 verification for synchronized registries.
- Bash, PowerShell and Windows CMD automation with dependency checks/install steps.

## Source of truth

Application code and canonical language data remain in the `nlp` repository. This `general` directory deliberately avoids silently becoming a divergent fork. `scripts/sync-nlp-assets.*` verifies or updates the integration manifest against the canonical repository.

## OCR contract

The general-repository contract is `ocr/api-contract.json` and the research/integration notes are in `ocr/README.md`. The canonical endpoint is `POST /api/ocr/scan`.

Recognition is not translation. The returned OCR hypothesis must remain associated with its source hash, engine, model (when configured), confidence and warnings before transliteration or translation is accepted as scholarly data.

## Research standards

Transliteration is kept separate from translation. Unicode/CLDR language identifiers and transformed-content metadata are used for language and script routing. See the canonical implementation's `docs/SOURCES.md` and `docs/PDF_CITATIONS.md`.

References:

- [Unicode supported scripts](https://www.unicode.org/standard/supported.html)
- [Unicode 18.0](https://www.unicode.org/versions/Unicode18.0.0/)
- [Unicode CLDR Project](https://cldr.unicode.org/) — language and locale data.
- [Unicode BCP 47 Extensions](https://cldr.unicode.org/index/bcp47-extension) — machine-readable language/locale extensions.
- [Unicode Transliteration Guidelines](https://cldr.unicode.org/index/cldr-spec/transliteration-guidelines) — transliteration guidance and its distinction from translation.
- [Kraken OCR](https://github.com/mittagessen/kraken) — historical/non-Latin OCR reference.
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract) — general OCR reference.
- [Cuneiform sign detection](https://github.com/CompVis/cuneiform-sign-detection-code) — sign-detection research reference.
- [Electronic Babylonian Literature cuneiform OCR](https://github.com/ElectronicBabylonianLiterature/cuneiform-ocr) — cuneiform OCR/data reference.

## KPI scope

The dashboard tracks objects, readings, review status, translations, confidence, PDF imports/exports, OCR jobs/errors, and processing performance. Metrics are API-derived rather than hardcoded in the UI.
