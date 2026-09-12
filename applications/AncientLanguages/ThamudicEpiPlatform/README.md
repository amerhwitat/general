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

Unicode CLDR provides language/locale data and BCP 47 extensions for machine-readable language identification; its transliteration guidance explicitly distinguishes transliteration from translation. citeturn0search0turn0search2

## KPI scope

The dashboard tracks objects, readings, review status, translations, confidence, PDF imports/exports, errors, and processing performance. Metrics are API-derived rather than hardcoded in the UI.
