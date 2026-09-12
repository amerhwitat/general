# RNN / ML assistant

The assistant is designed as a pluggable local inference service. Initial capabilities:
- event-sequence anomaly scoring
- workload and delivery trend forecasting
- work-item classification and priority suggestions
- sprint risk summaries
- incident clustering and probable-cause hints
- deployment-health correlation
- natural-language project/service summaries

Recommended production stack: PyTorch or TensorFlow for model training/inference, ONNX Runtime for portable inference, and the existing Chimera neural-network engine as an optional backend. Models must expose provenance, confidence and an explanation/feature summary where practical. AI never changes production infrastructure directly: actions become proposed workflow changes requiring policy/approval.

Training data must be explicitly authorized. Team messages, source code, credentials and customer data are not silently used for training.
