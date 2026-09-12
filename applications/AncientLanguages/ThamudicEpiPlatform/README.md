# Ancient Languages / ThamudicEpiPlatform Integration

This directory is the integration/deployment layer for the canonical implementation maintained in `amerhwitat/nlp/ThamudicEpiPlatform`.

## Capabilities

- Historical-object PDF import/export with provenance.
- Intelligent OCR for RTL/LTR, top-to-bottom/bottom-to-top, spiral/reverse hypotheses, skew/perspective correction and weathered/low-contrast material.
- Kraken/Tesseract adapters plus optional PaddleOCR/EasyOCR integrations.
- Chinese and Japanese as both source and target languages, including classical/vertical-writing metadata.
- BCP-47/CLDR target-language resolution.
- Literal, meaning, interlinear and scholarly translation contracts.
- Proof layer for neural/RNN/Transformer/LLM candidates and speech/phoneme records.
- Provider-neutral research chatbot API.
- KPI dashboard contract shared by API and language clients.
- SQLite, PostgreSQL and MySQL schemas; JSON/CSV flat-file interchange; optional Access/ODBC exchange.
- Bash, PowerShell and Windows CMD dependency/build automation.

## Source of truth

Application code and canonical language data remain in the `nlp` repository. This `general` directory deliberately avoids silently becoming a divergent fork.

Canonical application: [amerhwitat/nlp](https://github.com/amerhwitat/nlp/tree/main/ThamudicEpiPlatform)

## OCR and translation contract

Recognition is not translation. OCR hypotheses retain source hash, engine, model, confidence, geometry and warnings. Translation is separately labelled literal or meaning-preserving and retains alternatives/proof status.

The canonical API exposes:

- `POST /api/ocr/scan`
- `POST /api/ocr/geometry`
- `POST /api/translation/proof`
- `POST /api/speech/proof`
- `POST /api/chat`
- `GET /api/kpis/summary`
- `GET /api/kpis/languages`

## Research references

- [Unicode supported scripts](https://www.unicode.org/standard/supported.html)
- [Unicode 18.0](https://www.unicode.org/versions/Unicode18.0.0/)
- [CLDR](https://cldr.unicode.org/)
- [BCP 47 extensions](https://cldr.unicode.org/index/bcp47-extension)
- [Unicode Transliteration Guidelines](https://cldr.unicode.org/index/cldr-spec/transliteration-guidelines)
- [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)
- [EasyOCR](https://github.com/JaidedAI/EasyOCR)
- [Kraken](https://github.com/mittagessen/kraken)
- [Tesseract](https://github.com/tesseract-ocr/tesseract)
- [Rasa](https://github.com/RasaHQ/rasa)
- [LangChain](https://github.com/langchain-ai/langchain)
- [Cuneiform sign detection](https://github.com/CompVis/cuneiform-sign-detection-code)
- [CuReD](https://github.com/DigitalPasts/CuReD)

These are public research/architecture references; no third-party proprietary source, model or database is silently republished.
