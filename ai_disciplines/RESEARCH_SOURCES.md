# AI ecosystem research sources

The implementation was researched against current public documentation and public GitHub repositories. It does **not** copy upstream source code into these repositories.

| Discipline / layer | Reference implementation/ecosystem | Use in this architecture |
|---|---|---|
| ML | scikit-learn | classical supervised/unsupervised/statistical ML |
| DL | PyTorch | neural networks and tensor workloads |
| RL | Gymnasium + Stable-Baselines3 | environment API and RL algorithms |
| Symbolic AI | SymPy | symbolic algebra, logic-adjacent computation and code generation |
| CV | OpenCV / scikit-image | image/video processing and spatial features |
| NLP | spaCy / Hugging Face Transformers | linguistic pipelines and transformer models |
| MLOps | MLflow / Kubeflow | experiment tracking, model lifecycle and Kubernetes-native AI |
| Deployment | ONNX / Apache TVM | model interchange and optimized portable deployment |

Important distinction: these projects are external dependencies/providers. The Chimera/BizX/general interfaces define local contracts and adapters so applications can remain portable.

## Licensing/provenance rule

Upstream code should only be incorporated after its repository license and individual file provenance are checked. Otherwise the implementation should use a clean-room adapter/API contract rather than copying source files.
