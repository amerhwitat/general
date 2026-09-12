# Chimera 3D/4D capability matrix

This matrix separates the desired professional-DCC capability set from the currently implemented foundation. It prevents documentation from implying feature parity that has not yet been engineered and verified.

| Domain | Foundation | Target implementation |
|---|---|---|
| Modeling | Procedural mesh + translation | Half-edge topology, modifiers, booleans, subdivision, remesh |
| Sculpting | Radius/falloff brush | Multires, masks, alphas, symmetry, stroke recording, GPU deformation |
| UV/Texturing | UV/channel contracts | UV unwrap/pack, paint, bake, UDIM, image codecs |
| Materials | PBR contract | MaterialX graphs, texture nodes, shader compilation |
| Animation | Linear keyframes + time samples | Bezier/stepped curves, Dope Sheet, NLA, procedural animation |
| Rigging | Skeleton/constraints/retarget map | IK/FK solvers, skinning, constraints, pose tools |
| Motion | Timestamped transform stream | Mocap ingestion, camera/object tracking, solve/reconstruction |
| Dynamics | Solver boundary | Particles, rigid, cloth, fluid, soft body, destruction |
| VFX | Particle/field contracts | GPU particles, volumetrics, OpenVDB caches, effects graph |
| Compositing | Pass/image contracts | Node compositor, masks, keying, color transforms, render layers |
| Rendering | Backend-neutral camera/frame | Metal/OpenGL/WebGPU render graph, PBR/path tracing backends |
| Color | Color-space metadata | OpenColorIO configuration and display/view transforms |
| Interchange | Adapter boundary | OpenUSD/USDZ, glTF, Alembic, MaterialX production round-trip |
| Procedural | Node graph contract | Geometry nodes, simulation nodes, shader nodes, caching |
| Collaboration | Architecture boundary | Hosted sessions, versioned assets, authenticated P2P contracts |
| Apple | macOS/iOS/iPadOS shells | Production Metal renderer, Pencil sculpting, packaging/signing |
| Web | PlayCanvas viewport | Shared scene editor, WebGPU compute/rendering, hosted deployment |

Commercial DCC applications are capability references only. No proprietary implementation or asset is copied into this project.
