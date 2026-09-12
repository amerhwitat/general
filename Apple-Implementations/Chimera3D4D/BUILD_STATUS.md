# Build status

## Repository-side verification

- CMake target now includes core geometry, modeling, sculpt, texture, animation, rigging, motion, dynamics, rendering, materials, color, VFX, nodes, compositor and USD adapter sources.
- Core smoke tests cover vector math, mesh bounds/validation and 4D time interpolation.
- Objective-C/Metal XcodeGen specification covers macOS, iOS and iPadOS targets.
- Flutter and Web application manifests/source are present, including strict TypeScript configuration.
- GitHub Actions workflow definitions exist for C++, Web, Flutter and Apple builds.

## Verification limitations

The execution environment cannot resolve external GitHub hosts from the container, so a local clone/build could not be run here. No native compiler, Xcode, Apple SDK, Flutter SDK or Node dependency installation was executed by the repository-editing session.

The GitHub Actions workflow had no observable run for the checked commit at the time of this update. Therefore this document does **not** claim successful compilation, signed IPA/macOS application, Flutter bundle or Web production bundle. CI or a developer machine with the required toolchains must establish those results.
