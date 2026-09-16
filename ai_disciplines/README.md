# Unified AI Disciplines Architecture

This directory defines a provider-neutral architecture for six complementary AI disciplines:

1. Machine Learning (ML) — statistical learning over structured/tabular and mixed data.
2. Deep Learning (DL) — multi-layer neural architectures for text, audio, images and other high-dimensional data.
3. Reinforcement Learning (RL) — agent/environment interaction optimized through reward signals.
4. Symbolic AI / Expert Systems — explicit rules, logic, ontologies and deterministic inference.
5. Computer Vision (CV) — image/video/geometry processing, detection, segmentation and spatial reasoning.
6. Natural Language Processing (NLP) — tokenization, linguistic analysis, embeddings, transformers, translation and generation.

The architecture deliberately separates **discipline**, **model family**, **data contract**, **training/inference**, **evaluation**, and **deployment runtime** so implementations can use different languages and libraries without changing the application-level contract.

## Reference ecosystem

The implementation is designed to interoperate with established open-source ecosystems rather than copying their source code: scikit-learn for classical ML, PyTorch for DL, Gymnasium and Stable-Baselines3 for RL, SymPy for symbolic computation, OpenCV/scikit-image for CV, spaCy and Transformers for NLP, MLflow/Kubeflow for lifecycle orchestration, and Apache TVM/ONNX for portable model deployment.

See `registry.json` for capability metadata and `contracts/` for language-neutral schemas.

## Safety and reproducibility

- External models and datasets are referenced, not silently downloaded.
- Credentials and cloud mutation remain external and explicit.
- Model provenance, dataset version, seed, framework and metrics belong in experiment manifests.
- Generated AI code is treated as source requiring validation, tests and review.
