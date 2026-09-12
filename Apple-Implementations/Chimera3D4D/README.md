# Chimera 3D/4D Studio

Chimera 3D/4D Studio is a new open-source-oriented digital-content-creation platform for modeling, sculpting, texturing, rigging, animation, motion capture, tracking, VFX, simulation, color, rendering and time-varying 3D/4D scenes.

It is implemented as an independent application. Commercial DCC products such as ZBrush, Maya, 3ds Max and Cinema 4D are treated as capability references only; proprietary source, assets and undocumented implementations are not copied.

## Feature foundation

- polygon/procedural modeling and mesh editing
- subdivision, remeshing and topology adapters
- sculpting brush/stroke framework
- UV and PBR texture layers
- MaterialX-oriented material graph
- OpenColorIO color-management boundary
- rigging, IK/FK, constraints and retargeting contracts
- keyframe/curve animation and time-sampled geometry
- motion capture and camera/object tracking interfaces
- particles, rigid bodies, cloth/fluid/dynamics interfaces
- procedural node graphs and compositing
- OpenUSD/USDZ, glTF and other interchange adapters
- Metal/OpenGL/WebGPU rendering boundaries
- Objective-C macOS/iOS/iPadOS application shell
- Flutter cross-platform shell
- WebGPU/WebGL browser application
- optional Chimera 128D scene/perception metadata

## Repository layout

```text
Chimera3D4D/
├── core/ geometry/ modeling/ sculpt/ texture/
├── animation/ rigging/ motion/ dynamics/
├── rendering/ materials/ color/ vfx/ nodes/ compositor/
├── usd/ pipeline/
├── apple/ flutter/ web/
├── scripts/ tests/ docs/
└── CMakeLists.txt
```

## Open-source integration strategy

The architecture uses adapters around OpenUSD, MaterialX, OpenColorIO, OpenImageIO, OpenVDB, OpenSubdiv, CGAL and libigl. OpenUSD provides scene composition, animation and interchange concepts; CGAL and libigl provide geometry-processing algorithms; browser deployment can use WebGPU/WebGL engines such as PlayCanvas.

## 3D versus 4D

The core treats spatial geometry as 3D coordinates and time as a separate dimension of state. A 4D object can therefore be represented as geometry sampled/evolving over time rather than assuming that time is simply another spatial axis.

## 128D extension

Optional metadata can attach a 128-component state vector to a scene/entity for perception, semantic state, provenance, simulation context and observer-dependent interpretation. The geometry remains conventional 3D/4D data.

## Build status

The repository contains the cross-platform source foundation and build specifications. Actual signed iOS IPA/macOS application builds require macOS/Xcode and appropriate signing assets. Build results must be recorded by CI or a macOS developer machine; this repository does not claim an IPA was produced merely because project files exist.

## Research and training references

- Blender Manual: https://docs.blender.org/manual/en/5.2/
- OpenUSD tutorials: https://openusd.org/dev/tut_usd_tutorials.html
- OpenUSD developer guides: https://openusd.org/dev/api/_developer__guides.html
- CGAL: https://www.cgal.org/
- libigl: https://igl.ethz.ch/code/
- OpenDCC: https://github.com/shapefx/OpenDCC
- PlayCanvas Engine: https://github.com/playcanvas/engine

See `TRAINING_GUIDES.md` and `THIRD_PARTY.md` for attribution and integration notes.
