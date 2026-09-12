# Roadmap

## Foundation implemented

- scene/entity/mesh/time-sample contracts with deterministic validation
- 3D vector operations, bounds and topology validation
- 4D time-sampled transform evaluation (3D geometry + independent time state)
- optional 128D scene/entity state vector
- procedural cube and mesh translation
- sculpt brush/falloff primitive
- UV and PBR texture-layer contracts
- keyframe interpolation
- skeleton, constraints and retargeting contracts
- motion-stream contracts
- deterministic dynamics stepping boundary
- PBR material and backend-neutral renderer abstractions
- color-space metadata boundary
- particle, field, node and compositor foundations
- USD/glTF/Alembic interchange adapter boundary
- Objective-C + Metal macOS shell
- UIKit Metal shell for iOS/iPadOS, ready for touch/Pencil interaction work
- XcodeGen targets for macOS, iOS and iPadOS
- Flutter UI shell
- PlayCanvas WebGL/WebGPU viewport foundation
- strict TypeScript configuration
- CMake, PowerShell and macOS/Linux/Web/Flutter build scripts
- GitHub Actions CI definitions for C++, Web, Flutter and Apple
- open-source/training/license documentation

## Next implementation layers

1. half-edge/topology kernel, subdivision and remeshing
2. multiresolution sculpting, symmetry, stamping and brush alphas
3. UV packing, texture painting, baking and image I/O
4. MaterialX graph compiler and OCIO-managed color pipeline
5. GPU render graph and production Metal/OpenGL/WebGPU backends
6. skeletal pose solver, IK/FK and production retargeting
7. mocap/video tracking ingestion and camera solving
8. particles, rigid bodies, cloth, fluids and volumetric simulation
9. OpenVDB volumes and production compositor
10. OpenUSD live import/export, layers/variants and Hydra integration
11. asset browser, procedural graph editor, Python/C++ plugin SDK
12. collaborative hosted scene service and authenticated Chimera P2P integration
13. production iOS/iPadOS touch/Apple Pencil sculpt workflow
14. macOS production build, signing, notarization and packaging
15. regression/performance suite, GPU profiling and large-scene stress tests
