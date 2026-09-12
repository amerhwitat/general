# Apple-Implementations

Central Apple-platform implementation tree for the Amer Hwitat portfolio.

## Architecture

Each application has an independent directory containing:

- `objc/` — native Objective-C / Objective-C++ implementation for Xcode, iOS and macOS.
- `flutter/` — Flutter application layer targeting iOS and macOS.
- `docs/` — Apple-specific architecture, performance and integration notes.
- `scripts/` — macOS build/bootstrap helpers.

## Source-code citation index

The application source is intentionally kept beside its implementation-specific README. Use these direct trees as the authoritative navigation points:

- [BizX](BizX/) — Flutter and Objective-C bridge sources.
- [BizXtreme](BizXtreme/) — Flutter and Objective-C bridge sources.
- [Chimera3D4D](Chimera3D4D/) — C++ geometry/scene engine, AI, Apple Metal/UIKit/AppKit shell, Flutter and web implementation.
- [ChimeraIIOS](ChimeraIIOS/) — Apple compatibility/application boundary.
- [CPU4096](CPU4096/) — Apple compatibility/application boundary.
- [CPU4096Simulator](CPU4096Simulator/) — Apple compatibility/application boundary.
- [PDFreaderPY](PDFreaderPY/) — Apple compatibility/application boundary.
- [nlp](nlp/) — Apple compatibility/application boundary.
- [eth-key-check](eth-key-check/) — Apple compatibility/application boundary.
- [bruteforce](bruteforce/) — Apple compatibility/application boundary.
- [keygen](keygen/) — Apple compatibility/application boundary.
- [test](test/) — Apple compatibility/application boundary.
- [general](general/) — Apple compatibility/application boundary.
- [VanG](VanG/) — Apple compatibility/application boundary.
- [amerhwitat.github.io](amerhwitat.github.io/) — Apple compatibility/application boundary.
- [Shared scripts](scripts/) — native Apple bootstrap/build automation.

### Detailed Chimera3D4D source references

- [Geometry](Chimera3D4D/core/src/geometry.cpp) and [scene](Chimera3D4D/core/src/scene.cpp)
- [RNN/LLM scene engine](Chimera3D4D/ai/rnn_llm_engine.py)
- [Animation](Chimera3D4D/animation/src/animation.cpp)
- [Modeling](Chimera3D4D/modeling/src/modeling.cpp)
- [Sculpt](Chimera3D4D/sculpt/src/sculpt.cpp)
- [Rigging](Chimera3D4D/rigging/src/rigging.cpp)
- [Motion](Chimera3D4D/motion/src/motion.cpp)
- [Dynamics](Chimera3D4D/dynamics/src/dynamics.cpp)
- [Rendering](Chimera3D4D/rendering/src/rendering.cpp)
- [Materials](Chimera3D4D/materials/src/materials.cpp)
- [Color](Chimera3D4D/color/src/color.cpp)
- [VFX](Chimera3D4D/vfx/src/vfx.cpp)
- [Nodes](Chimera3D4D/nodes/src/nodes.cpp)
- [Compositor](Chimera3D4D/compositor/src/compositor.cpp)
- [USD adapter](Chimera3D4D/usd/src/usd_adapter.cpp)
- [iOS shell](Chimera3D4D/apple/ios/CH3D4DiOSViewController.m)
- [Metal renderer](Chimera3D4D/apple/metal/CH3D4DRenderer.m)
- [macOS app delegate](Chimera3D4D/apple/objc/CH3D4DAppDelegate.m)
- [Web entry point](Chimera3D4D/web/src/main.ts)
- [Web viewport](Chimera3D4D/web/src/viewport.ts)
- [Flutter entry point](Chimera3D4D/flutter/lib/main.dart)

## Applications

- BizX
- BizXtreme
- ChimeraIIOS
- CPU4096
- CPU4096Simulator
- PDFreaderPY
- nlp
- eth-key-check
- bruteforce
- keygen
- test
- general
- VanG
- amerhwitat.github.io

## Apple targets

- iOS arm64
- iOS Simulator arm64
- macOS arm64
- macOS x86_64 where supported by the selected Flutter/Xcode toolchain

## Native performance policy

- Keep Flutter UI work off blocking native calls.
- Use background queues for I/O, hashing, parsing and synchronization.
- Marshal UIKit/AppKit mutations to the main thread.
- Use Objective-C++ only for CPU/graphics/native interoperability where needed.
- Prefer Metal-backed rendering and hardware acceleration.
- Reuse buffers and avoid unnecessary JSON copies on high-frequency paths.
- Keep camera/microphone access explicit and permission-gated.
- Keep cryptographic secrets outside source control.

## Xcode project generation

XcodeGen specifications are used where practical so generated `.xcodeproj` files do not become the source of truth. XcodeGen consumes YAML/JSON project specifications and generates Xcode projects from the repository tree.

## Dependencies

CocoaPods remains supported for Objective-C dependencies that genuinely need it; Swift Package Manager is preferred where an upstream package provides it.

## Building on macOS

```bash
cd Apple-Implementations/<Application>/flutter
flutter pub get
flutter build ios --release
flutter build macos --release
```

For native projects:

```bash
cd Apple-Implementations/<Application>/objc
xcodegen generate
xcodebuild -scheme <Application> -sdk iphonesimulator -configuration Release build
xcodebuild -scheme <Application> -sdk macosx -configuration Release build
```

A signed IPA requires an Apple signing identity/provisioning configuration and must be performed on macOS with Xcode. No certificates, provisioning profiles or secrets are committed here.

## Scope boundary

This repository centralizes Apple implementations; canonical non-Apple source remains in each original repository. The Apple copies/adapters are designed to preserve application behavior while using Apple-native execution paths.
