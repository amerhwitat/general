# Apple-Implementations

Central Apple-platform implementation tree for the Amer Hwitat portfolio.

## Architecture

Each application has an independent directory containing:

- `objc/` — native Objective-C / Objective-C++ implementation for Xcode, iOS and macOS.
- `flutter/` — Flutter application layer targeting iOS and macOS.
- `docs/` — Apple-specific architecture, performance and integration notes.
- `scripts/` — macOS build/bootstrap helpers.

Flutter is the shared UI/application layer; Objective-C is the native Apple integration layer for APIs requiring direct UIKit/AppKit/Foundation/AVFoundation/Metal access. Flutter officially supports Objective-C host code on iOS and macOS through platform channels, and supports native platform integration through Pigeon/platform channels. citeturn0search0

Flutter Impeller is retained as the Apple rendering path. It is the supported renderer on iOS and is enabled by default on supported macOS releases. citeturn0search1

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

Current Flutter documentation supports iOS arm64 and macOS arm64/x86_64 deployment, with Apple Silicon being the preferred target for new macOS development. citeturn0search2

## Native performance policy

- Keep Flutter UI work off blocking native calls.
- Use background queues for I/O, hashing, parsing and synchronization.
- Marshal UIKit/AppKit mutations to the main thread.
- Use Objective-C++ only for CPU/graphics/native interoperability where needed.
- Prefer Metal-backed rendering and hardware acceleration.
- Reuse buffers and avoid unnecessary JSON copies on high-frequency paths.
- Keep camera/microphone access explicit and permission-gated.
- Keep cryptographic secrets outside source control.

Flutter's performance guidance separates UI, raster, platform and I/O work; blocking those threads can degrade frame performance. citeturn0search6

## Xcode project generation

XcodeGen specifications are used where practical so generated `.xcodeproj` files do not become the source of truth. XcodeGen consumes YAML/JSON project specifications and generates Xcode projects from the repository tree. citeturn0search5

## Dependencies

CocoaPods remains supported for Objective-C dependencies that genuinely need it; Swift Package Manager is preferred where an upstream package provides it. CocoaPods is an Objective-C/Swift dependency manager with a large public library ecosystem. citeturn0search9

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
