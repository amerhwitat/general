# Apple implementation

This directory is the Apple-native companion implementation for its corresponding portfolio application.

## Targets

- Objective-C / Objective-C++ for Xcode-native integration.
- Flutter/Dart for shared UI and application orchestration.
- iOS arm64 and iOS Simulator arm64.
- macOS arm64, with Intel support where the selected Flutter/Xcode release permits it.

## Native boundary

Objective-C owns Apple framework integration, lifecycle, permissions, audio/video, filesystem, networking and high-performance native services. Flutter owns reusable UI/state and invokes native services asynchronously through platform channels.

## Performance

Avoid blocking the Flutter UI/raster/platform threads. Move hashing, parsing, synchronization and large I/O to background queues. Use explicit autorelease pools for long native loops and reuse buffers for streaming workloads.

## Security

Camera and microphone access is explicit and permission-gated. No credentials or signing material are stored in source control. P2P remains opt-in, authenticated and capability-scoped.

## Build

```bash
flutter pub get
flutter build ios --release --no-codesign
flutter build macos --release
cd ../objc
xcodegen generate
```
