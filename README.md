# Amer Hwitat — General / Integration Repository

This repository is a general integration and research workspace within the Amer Hwitat GitHub portfolio. It complements the canonical `ChimeraIIOS` repository and provides shared experiments, host-side integration material and compatibility boundaries.

## Central Apple implementations

`Apple-Implementations/` is the portfolio-wide Apple source tree. Each application has its own subdirectory with Objective-C/Xcode and Flutter iOS/macOS implementations, Apple-specific documentation and build boundaries. The structure preserves the owning repositories while providing a centralized Apple implementation surface.

## Chimera 3D/4D Studio

`Apple-Implementations/Chimera3D4D/` is the new unified 3D/4D digital-content-creation application foundation. It combines a portable C++ scene/geometry core with modeling, sculpting, materials, animation, rigging, motion, rendering, VFX, procedural-node, interchange, Objective-C/Metal, Flutter and Web foundations.

The design uses open standards and open-source adapter boundaries including OpenUSD/Hydra, MaterialX, OpenColorIO, OpenImageIO, OpenVDB, OpenSubdiv, CGAL, libigl and PlayCanvas. Public Blender/OpenUSD/OpenDCC/geometry documentation is recorded as training/reference material. Commercial DCC products are capability references only; proprietary source and assets are not copied.

The 4D model treats time as a separate evolving state dimension for animated/deforming geometry and simulations. An optional 128-component semantic/perception state is attached as metadata without replacing ordinary 3D geometry.

## Apple applications

Existing `Apple-Implementations/` application directories contain Objective-C/Flutter companions. `Chimera3D4D/apple/project.yml` adds a native Objective-C + Metal macOS shell; the architecture is extensible to iOS/iPadOS targets. IPA archive/export requires macOS/Xcode and operator-controlled signing.

## Apple performance

Apple implementations use background queues for expensive work, explicit native/Flutter boundaries, buffer reuse, Metal-compatible rendering and main-thread UI marshaling. Flutter's performance model separates UI, raster, platform and I/O paths; blocking those paths is avoided.

## Build

For Chimera 3D/4D:

```bash
cd Apple-Implementations/Chimera3D4D
./scripts/build-linux.sh
```

On macOS, use `scripts/build-macos.sh`; XcodeGen can generate the native project from `apple/project.yml`. Web and Flutter builds are available through `scripts/build-all.ps1` or their platform-specific tools.

## Chimera 128D

Applications and experiments can model state using the portfolio-wide 128D semantic framework: geometry, time, observer/perspective, light/shadow/material response, events, objects, properties and interaction rules, with extensible perception/cognition/vector dimensions.

## Authenticated P2P

The repository follows the common Chimera P2P contract for opt-in peer identity, capability negotiation, request/response, publish, snapshots and deltas. State is accepted only after local authorization and validation of sequencing, payload integrity and optional signatures.

The protocol excludes unsolicited network scanning, credential/private-key exchange, arbitrary executable transfer and remote command execution.

## Portfolio relationships

- `ChimeraIIOS` — canonical OS and interoperability contracts.
- `CPU4096` / `CPU4096Simulator` — processor and simulation research.
- `nlp` / `PDFreaderPY` — linguistic and document research.
- `keygen` / `test` — Java and host integration tracks.
- `BizX` / `BizXtreme` — application/game tracks.
- `eth-key-check` / `bruteforce` — bounded cryptographic research.

## Licensing

Original project code is released under GNU GPL v3 or later. Third-party code and assets retain applicable licenses.
