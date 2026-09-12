# Architecture

The application is divided into a deterministic C++ core and platform adapters.

- `core`: scene IDs, mesh topology, transforms, time samples and optional 128D metadata.
- `modeling`: procedural and interactive mesh operations.
- `sculpt`: pressure/falloff brush primitives.
- `animation`: keyframes and interpolation.
- `rigging`/`motion`: skeleton, constraints and timestamped motion streams.
- `dynamics`/`vfx`: simulation contracts; production solvers remain replaceable adapters.
- `materials`/`color`: PBR and color-management contracts.
- `rendering`: backend-neutral camera/frame/render interfaces.
- `usd`: OpenUSD interchange boundary.
- `apple`: Objective-C and Metal application layer.
- `flutter`: cross-platform workspace UI.
- `web`: browser/WebGPU/WebGL UI and viewport.

Long-running geometry, simulation and rendering work must remain off UI threads. GPU backends should use command-buffer/resource lifetimes appropriate to their platform. The Web frontend is a deployment surface, not a separate scene format.

## 4D and 128D

4D is modeled as time-varying 3D state. Each object can carry timestamped transforms and future modules can attach sampled geometry, simulation fields and animation curves. The optional 128-component state vector is semantic/perceptual metadata and does not redefine Euclidean geometry.
