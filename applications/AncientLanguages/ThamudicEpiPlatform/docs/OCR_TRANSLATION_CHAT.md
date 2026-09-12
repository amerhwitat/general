# Shared OCR / translation / chatbot integration

The General repository mirrors the canonical `nlp/ThamudicEpiPlatform` contracts so applications can consume the same APIs without maintaining separate scholarly logic.

## Recognition

Supports horizontal LTR/RTL, vertical top-to-bottom/bottom-to-top, spiral and reverse hypotheses, skew/perspective correction and weathered/low-contrast preprocessing. Geometry is a hypothesis and is retained in provenance.

## Chinese/Japanese

Chinese and Japanese are first-class source and target languages. Historical/classical forms may use vertical writing and right-to-left column order; modern BCP-47/CLDR locale targets are supported.

## Translation

Literal, meaning, interlinear and scholarly modes preserve uncertainty and provenance. No OCR result is silently promoted to a historical reading.

## Chatbot

Applications may connect a self-hosted/local LLM or another approved provider through the canonical `/api/chat` interface. Evidence and citations must accompany research answers.

## Research references

- [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) — multilingual OCR, orientation and unwarping.
- [EasyOCR](https://github.com/JaidedAI/EasyOCR) — multilingual OCR including Chinese and Japanese.
- [Kraken](https://github.com/mittagessen/kraken) — historical/non-Latin OCR.
- [Rasa](https://github.com/RasaHQ/rasa) — conversational AI architecture.
- [LangChain](https://github.com/langchain-ai/langchain) — LLM application framework.
- [Unicode](https://www.unicode.org/standard/supported.html) — script repertoire.
- [CLDR](https://cldr.unicode.org/) — locale and language data.

These are public implementation references; external source code and model assets are not copied unless their licenses permit redistribution.
