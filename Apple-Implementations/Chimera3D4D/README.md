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
- CMake, PowerShell, shell scripts and GitHub Actions CI definitions

## Repository layout

```text
Chimera3D4D/
├── core/ geometry/ modeling/ sculpt/ texture/
├── animation/ rigging/ motion/ dynamics/
├── rendering/ materials/ color/ vfx/ nodes/ compositor/
├── usd/ pipeline/ docs/
├── apple/ flutter/ web/
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

On Windows PowerShell:

```powershell
./scripts/build-all.ps1
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

The Apple script can generate an Xcode project when XcodeGen is installed. Actual signed iOS/iPadOS IPA and production macOS distribution still require macOS/Xcode, signing identities/profiles and the appropriate Apple SDKs.

## Capability and implementation status

See `docs/FEATURE_MATRIX.md` for the distinction between the implemented foundation and the remaining production DCC layers. See `ROADMAP.md` for the next engineering stages and `BUILD_STATUS.md` for verification status.

## Hosted web and collaboration

`docs/HOSTED_WEB.md` describes a deployment architecture for static web assets, authenticated scene APIs, live collaboration and future trusted Chimera P2P integration. No credentials or production endpoints are embedded.

## Research and training references

- Blender Manual: https://docs.blender.org/manual/en/5.2/
- OpenUSD tutorials: https://openusd.org/dev/tut_usd_tutorials.html
- OpenUSD developer guides: https://openusd.org/dev/api/_developer__guides.html
- CGAL: https://www.cgal.org/
- libigl: https://igl.ethz.ch/code/
- OpenDCC: https://github.com/shapefx/OpenDCC
- PlayCanvas Engine: https://github.com/playcanvas/engine

See `TRAINING_GUIDES.md` and `THIRD_PARTY.md` for attribution and integration notes.
