# Amer Hwitat — General / Integration Repository

This repository is a general integration and research workspace within the Amer Hwitat GitHub portfolio. It complements the canonical `ChimeraIIOS` repository and provides shared experiments, host-side integration material and compatibility boundaries.

## Central Apple implementations

`Apple-Implementations/` is now the portfolio-wide Apple source tree. Each application has its own subdirectory with Objective-C/Xcode and Flutter iOS/macOS implementations, Apple-specific documentation and build boundaries. The structure preserves the owning repositories while providing a centralized Apple implementation surface.

Flutter officially supports Objective-C host code on iOS and macOS through platform channels, and its Apple tooling uses Xcode for device/simulator builds. citeturn0search0turn0search8 Flutter's Impeller renderer is the supported iOS renderer and is enabled by default on supported macOS releases. citeturn0search1

## Apple applications

`apple/project.yml` defines native SwiftUI iOS/iPadOS and macOS application targets generated with XcodeGen. `Apple-Implementations/` contains the Objective-C + Flutter companion implementations for BizX, BizXtreme, ChimeraIIOS, CPU4096, CPU4096Simulator, PDFreaderPY, nlp, eth-key-check, bruteforce, keygen, test, general, VanG and amerhwitat.github.io. IPA archive/export requires macOS/Xcode and operator-controlled signing.

## Apple performance

The Apple implementations use background queues for expensive work, explicit native/Flutter boundaries, buffer reuse, Metal/Impeller-compatible rendering, main-thread UI marshaling and permission-gated camera/microphone services. Flutter's performance model separates UI, raster, platform and I/O threads; blocking those paths is avoided. citeturn0search6

XcodeGen is used where appropriate to generate Xcode projects from source-controlled YAML specifications rather than storing generated projects as the source of truth. citeturn0search5 CocoaPods remains an available Objective-C dependency manager when an upstream dependency genuinely requires it; Swift Package Manager is preferred where available. citeturn0search9

## Build

```bash
cd Apple-Implementations
./scripts/bootstrap-macos.sh
./scripts/build-all.sh
```

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
