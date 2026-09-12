# Intelligent OCR Scanner Integration

The canonical OCR implementation lives in `amerhwitat/nlp/ThamudicEpiPlatform/server/ocr_scanner.py`. This directory is the general-repository integration contract and launcher layer.

## Engines

- `auto` — try configured historical/non-Latin OCR first, then the general OCR adapter.
- `kraken` — optional engine for historical and non-Latin material; a compatible model is required.
- `tesseract` — optional general OCR adapter for installed traineddata.
- `quality-only` — image quality and provenance analysis without recognition.

Kraken is designed for historical/non-Latin material and supports RTL, BiDi and top-to-bottom layouts; its API also supports ALTO, PageXML and hOCR workflows. Tesseract 5 provides an LSTM-based OCR engine and is Apache-2.0 licensed. Cuneiform sign-detection research has demonstrated line segmentation and sign detection with weak/supervised learning, which informs the plugin boundary here. The application does not copy third-party model weights or source code into this repository.

## Intelligent pipeline

1. Validate file size and compute SHA-256.
2. Measure resolution, contrast and blur.
3. Run configured OCR engines and retain confidence per candidate.
4. Normalize recognized text to Unicode NFC.
5. Score script candidates from Unicode ranges.
6. Return bounding boxes when the engine supplies them.
7. Preserve warnings and provenance.
8. Keep recognition separate from transliteration and translation; scholarly review is required.

## References

- [Unicode supported scripts](https://www.unicode.org/standard/supported.html)
- [Unicode 18.0 draft/implementation data](https://www.unicode.org/versions/Unicode18.0.0/)
- [Kraken OCR](https://github.com/mittagessen/kraken)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [Cuneiform sign detection research code](https://github.com/CompVis/cuneiform-sign-detection-code)
- [Electronic Babylonian Literature cuneiform OCR](https://github.com/ElectronicBabylonianLiterature/cuneiform-ocr)
- [CuReD cuneiform transliteration OCR](https://github.com/DigitalPasts/CuReD)

All third-party references are integration/provenance references. Their licenses remain authoritative.
