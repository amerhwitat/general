# Ancient Languages / ThamudicEpiPlatform Integration

This directory is the integration/deployment layer for the canonical implementation maintained in `amerhwitat/nlp/ThamudicEpiPlatform`.

## Capabilities

- Historical-object PDF import with bounded extraction and page provenance.
- Research PDF export containing objects, scripts, scholarly transliteration, literal/meaning translations, confidence, provenance and citations.
- KPI dashboard contract shared by the API and language clients.
- Integration manifests and SHA-256 verification for synchronized registries.
- Bash, PowerShell and Windows CMD automation.

## Source of truth

Application code and canonical language data remain in the `nlp` repository. This `general` directory deliberately avoids silently becoming a divergent fork. `scripts/sync-nlp-assets.*` verifies or updates the integration manifest against the canonical repository.

## Research standards

Transliteration is kept separate from translation. Unicode/CLDR language identifiers and transformed-content metadata are used for language and script routing. See the canonical implementation's `docs/SOURCES.md` and `docs/PDF_CITATIONS.md`.

References:

- [Unicode CLDR Project](https://cldr.unicode.org/) — language and locale data.
- [Unicode BCP 47 Extensions](https://cldr.unicode.org/index/bcp47-extension) — machine-readable language/locale extensions.
- [Unicode Transliteration Guidelines](https://cldr.unicode.org/index/cldr-spec/transliteration-guidelines) — transliteration guidance and its distinction from translation.

## KPI scope

The dashboard tracks objects, readings, review status, translations, confidence, PDF imports/exports, errors, and processing performance. Metrics are API-derived rather than hardcoded in the UI.
