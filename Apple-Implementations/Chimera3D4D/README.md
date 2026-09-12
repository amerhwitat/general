# Chimera 3D/4D Studio

Chimera 3D/4D Studio is an open-source-oriented digital-content-creation platform for modeling, sculpting, texturing, rigging, animation, motion capture, tracking, VFX, simulation, color, rendering and time-varying 3D/4D scenes.

It is implemented as an independent application. Commercial DCC products such as ZBrush, Maya, 3ds Max and Cinema 4D are capability references only; proprietary source, assets and undocumented implementations are not copied.

## Current foundation

- 3D vector math, transforms, triangle meshes, bounds and topology validation
- deterministic scene/entity IDs and validated time samples
- 4D time-varying transforms with interpolation; time remains distinct from spatial coordinates
- optional 128-component scene/entity state metadata for perception/semantic context
- procedural primitives and mesh transforms
- sculpt brush with falloff and symmetry-ready contract
- UV/PBR texture-layer abstractions
- keyframe animation, skeleton/constraint/retargeting contracts and motion streams
- deterministic dynamics stepping boundary
- backend-neutral rendering, PBR materials and color-space metadata
- particles/fields, procedural nodes and compositor contracts
- USD/USDZ, glTF and Alembic interchange boundary
- macOS Objective-C/Metal shell plus iOS/iPadOS UIKit Metal shell
- Flutter cross-platform workspace shell
- PlayCanvas WebGL/WebGPU browser viewport
- local-first RNN/LLM scene intelligence in `ai/`
- CMake, PowerShell, shell scripts and GitHub Actions CI definitions

## Complete source-code citation index

| Module | Source |
|---|---|
| Core geometry | [core/src/geometry.cpp](core/src/geometry.cpp), [geometry.hpp](core/include/chimera3d4d/geometry.hpp) |
| Scene system | [core/src/scene.cpp](core/src/scene.cpp), [scene.hpp](core/include/chimera3d4d/scene.hpp) |
| AI/RNN/LLM | [ai/rnn_llm_engine.py](ai/rnn_llm_engine.py), [ai/README.md](ai/README.md) |
| Animation | [animation/src/animation.cpp](animation/src/animation.cpp), [animation/include/animation.hpp](animation/include/animation.hpp) |
| Modeling | [modeling/src/modeling.cpp](modeling/src/modeling.cpp), [modeling/include/modeling.hpp](modeling/include/modeling.hpp) |
| Sculpting | [sculpt/src/sculpt.cpp](sculpt/src/sculpt.cpp), [sculpt/include/sculpt.hpp](sculpt/include/sculpt.hpp) |
| Rigging | [rigging/src/rigging.cpp](rigging/src/rigging.cpp), [rigging/include/rigging.hpp](rigging/include/rigging.hpp) |
| Motion | [motion/src/motion.cpp](motion/src/motion.cpp), [motion/include/motion.hpp](motion/include/motion.hpp) |
| Dynamics | [dynamics/src/dynamics.cpp](dynamics/src/dynamics.cpp), [dynamics/include/dynamics.hpp](dynamics/include/dynamics.hpp) |
| Rendering | [rendering/src/rendering.cpp](rendering/src/rendering.cpp), [rendering/include/rendering.hpp](rendering/include/rendering.hpp) |
| Materials | [materials/src/materials.cpp](materials/src/materials.cpp), [materials/include/materials.hpp](materials/include/materials.hpp) |
| Color | [color/src/color.cpp](color/src/color.cpp), [color/include/color.hpp](color/include/color.hpp) |
| VFX | [vfx/src/vfx.cpp](vfx/src/vfx.cpp), [vfx/include/vfx.hpp](vfx/include/vfx.hpp) |
| Nodes | [nodes/src/nodes.cpp](nodes/src/nodes.cpp), [nodes/include/nodes.hpp](nodes/include/nodes.hpp) |
| Compositor | [compositor/src/compositor.cpp](compositor/src/compositor.cpp), [compositor/include/compositor.hpp](compositor/include/compositor.hpp) |
| USD | [usd/src/usd_adapter.cpp](usd/src/usd_adapter.cpp), [usd/include/usd_adapter.hpp](usd/include/usd_adapter.hpp) |
| iOS shell | [apple/ios/CH3D4DiOSViewController.m](apple/ios/CH3D4DiOSViewController.m), [CH3D4DiOSViewController.h](apple/ios/CH3D4DiOSViewController.h) |
| Metal | [apple/metal/CH3D4DRenderer.m](apple/metal/CH3D4DRenderer.m), [CH3D4DRenderer.h](apple/metal/CH3D4DRenderer.h) |
| macOS Objective-C shell | [apple/objc/CH3D4DAppDelegate.m](apple/objc/CH3D4DAppDelegate.m), [CH3D4DViewport.m](apple/objc/CH3D4DViewport.m) |
| Flutter | [flutter/lib/main.dart](flutter/lib/main.dart) |
| Web TypeScript | [web/src/main.ts](web/src/main.ts), [web/src/viewport.ts](web/src/viewport.ts) |
| Web shell | [web/index.html](web/index.html), [web/package.json](web/package.json) |
| Build automation | [scripts/](scripts/), [CMakeLists.txt](CMakeLists.txt) |
| Tests | [tests/core_tests.cpp](tests/core_tests.cpp) |
| CI | [.github/workflows/chimera-3d4d.yml](.github/workflows/chimera-3d4d.yml) |
| Architecture/docs | [ARCHITECTURE.md](ARCHITECTURE.md), [docs/](docs/) |

## RNN/LLM scene intelligence

`ai/rnn_llm_engine.py` provides bounded recurrent scene memory, time-series observation, explainable recommendations and an optional PyTorch GRU next-token backend. It can consume authorized scene descriptions, animation/motion events and optional 128D semantic metadata. It does not automatically mutate production scenes.

## Repository layout

```text
Chimera3D4D/
├── core/ geometry/ modeling/ sculpt/ texture/
├── animation/ rigging/ motion/ dynamics/
├── rendering/ materials/ color/ vfx/ nodes/ compositor/
├── usd/ pipeline/ docs/
├── ai/ apple/ flutter/ web/
├── scripts/ tests/
└── CMakeLists.txt
```

## Open-source integration strategy

The architecture uses adapter boundaries around OpenUSD, MaterialX, OpenColorIO, OpenImageIO, OpenVDB, OpenSubdiv, CGAL and libigl. The core does not require these libraries to compile. See `THIRD_PARTY.md` and `LICENSES.md` before enabling optional adapters.

## 3D versus 4D

The core treats spatial geometry as 3D coordinates and time as a separate dimension of state. A 4D object can therefore be represented as geometry sampled/evolving over time without treating time as an additional spatial coordinate.

## 128D extension

Optional metadata can attach a 128-component state vector to a scene/entity for perception, semantic state, provenance, simulation context and observer-dependent interpretation. The geometry remains conventional 3D/4D data.

## Build

### C++
```bash
./scripts/build-linux.sh
```

### Web
```bash
./scripts/build-web.sh
```

### Flutter
```bash
./scripts/build-flutter.sh
```

### Apple
```bash
./scripts/build-macos.sh
```

Actual signed Apple distribution requires macOS/Xcode and the appropriate signing configuration.

## Capability and implementation status

See `docs/FEATURE_MATRIX.md`, `ROADMAP.md` and `BUILD_STATUS.md` for implementation and verification boundaries.

## License

GPL-3.0-or-later for original project code. Third-party libraries and assets retain their own licenses.
