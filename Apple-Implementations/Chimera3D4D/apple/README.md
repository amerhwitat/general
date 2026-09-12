# Apple implementation

The Apple frontend is split by platform:

- `objc/` — native macOS application shell and Metal viewport.
- `metal/` — backend boundary for Metal rendering.
- `ios/` — shared UIKit controller for iPhone/iPad and Apple Pencil/touch-ready interaction.
- `project.yml` — XcodeGen specification for macOS, iOS and iPadOS device families.

The native UI is intentionally thin: scene evaluation belongs to the C++ core and GPU work belongs to Metal adapters. Build/sign/package operations require macOS with Xcode and valid signing configuration.
