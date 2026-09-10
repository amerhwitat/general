# Chimera II OS Mobile Edition

A unified ARM64 mobile platform combining Chimera native applications with Arch/Debian/RPM/Alpine/Nix/Flatpak/Snap, Android APK and open-source Swift application targets.

## Platform
- Koronos kernel/HAL authority
- Spotnik networking
- Aurora Wayland Glass mobile shell and application store
- Adaptive Resource Fabric
- 16 KiB ARM64 profile
- lazy 64..16384-bit and arbitrary N-bit execution

## Universal application model

The Mobile Package Fabric preserves each ecosystem's semantics while adding a common identity, ABI, provenance, signature, capability and transaction layer.

Supported package/application paths include:
- Arch `pacman`
- Debian `dpkg`, `apt`, `apt-get`, `aptitude`, including `.deb`
- RPM `rpm`, `dnf`, `yum`
- Alpine `apk`
- Nix
- Flatpak
- Snap
- AppImage
- Git/GitHub source builds
- Android APK in isolated compatibility runtime
- Swift Package Manager/Foundation/SwiftNIO

Debian's documented model is preserved: dpkg is the low-level package manager and APT/apt-get provides dependency resolution/front-end functionality. citeturn0search3turn0search11

Arch's pacman/libalpm model remains the native mobile userspace baseline. citeturn0search2

## Android Edition

APK applications execute through an isolated Android compatibility target inspired by Waydroid's Linux namespace/container architecture. citeturn1search13

## iOS-inspired Edition

Chimera does not claim Apple's proprietary iOS frameworks are open source. Instead it provides a Swift application target using the open-source Swift Package Manager, Swift Foundation/corelibs and SwiftNIO ecosystem. citeturn1search0turn1search2turn1search3

## Store

Aurora Store presents package source, format, ABI, sandbox, capabilities, signature state and update channel before installation.

## Build and test

```bash
cmake -S mobile -B build/mobile -DCMAKE_BUILD_TYPE=Release
cmake --build build/mobile --parallel
ctest --test-dir build/mobile --output-on-failure
```

## Security

Every package path is expected to use hashes/signatures and a transactional install boundary. Untrusted package scripts cannot acquire host privileges simply because they were requested by a package. Flatpak's sandbox/portal model is a reference for this capability boundary. citeturn0search6turn0search8

Production phone bring-up still requires verified boot, hardware-backed keys, encrypted storage, modem isolation, GPU/camera/audio/sensor HALs and physical-device performance/thermal validation.
