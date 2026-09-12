# Amer Hwitat — General / Integration Repository

This repository is a general integration and research workspace within the Amer Hwitat GitHub portfolio. It complements the canonical `ChimeraIIOS` repository and provides shared experiments, host-side integration material and compatibility boundaries.

## Apple applications

`apple/project.yml` defines native SwiftUI iOS/iPadOS and macOS application targets generated with XcodeGen. The Apple shell provides a portable integration surface while source-of-truth application logic remains in its owning repositories. IPA archive/export requires macOS/Xcode and operator-controlled signing.

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

Original project code is released under GNU GPL v3 or later. Third-party code and assets retain their applicable licenses.
