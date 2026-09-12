# Chimera II OS Mobile Edition

A unified ARM64 mobile platform combining Chimera native applications with Arch/Debian/RPM/Alpine/Nix/Flatpak/Snap, Android APK and open-source Swift application targets.

## Source-code citation index

| Area | Source |
|---|---|
| Build definition | [CMakeLists.txt](CMakeLists.txt) |
| Runtime | [src/runtime.cpp](src/runtime.cpp), [include/chimera/mobile/runtime.hpp](include/chimera/mobile/runtime.hpp) |
| Package manager | [src/package_manager.cpp](src/package_manager.cpp), [include/chimera/mobile/package_manager.hpp](include/chimera/mobile/package_manager.hpp) |
| Package fabric | [src/package_fabric.cpp](src/package_fabric.cpp), [include/chimera/mobile/package_fabric.hpp](include/chimera/mobile/package_fabric.hpp) |
| Package adapters | [src/package_adapters.cpp](src/package_adapters.cpp), [include/chimera/mobile/package_adapters.hpp](include/chimera/mobile/package_adapters.hpp) |
| Binder | [src/binder.cpp](src/binder.cpp), [include/chimera/mobile/binder.hpp](include/chimera/mobile/binder.hpp) |
| Graphics | [src/graphics.cpp](src/graphics.cpp), [include/chimera/mobile/graphics.hpp](include/chimera/mobile/graphics.hpp) |
| Power | [src/power.cpp](src/power.cpp), [include/chimera/mobile/power.hpp](include/chimera/mobile/power.hpp) |
| App-store boundary | [src/app_store.cpp](src/app_store.cpp), [include/chimera/mobile/app_store.hpp](include/chimera/mobile/app_store.hpp) |
| N-bit execution | [include/chimera/mobile/nbit.hpp](include/chimera/mobile/nbit.hpp) |
| Architecture profile | [include/chimera/mobile/arch_profile.hpp](include/chimera/mobile/arch_profile.hpp) |
| Android target | [include/chimera/mobile/android_target.hpp](include/chimera/mobile/android_target.hpp), [android/android-runtime.toml](android/android-runtime.toml) |
| Swift target | [include/chimera/mobile/swift_target.hpp](include/chimera/mobile/swift_target.hpp), [ios/swift-runtime.toml](ios/swift-runtime.toml) |
| Aurora web shell | [aurora/index.html](aurora/index.html), [aurora/store/index.html](aurora/store/index.html), [aurora/AuroraGlassBackground.svg](aurora/AuroraGlassBackground.svg) |
| Debian packaging | [debian/chimera-deb-policy.toml](debian/chimera-deb-policy.toml), [debian/install-deb.sh](debian/install-deb.sh) |
| Arch tooling | [arch/tools/bootstrap-arch-arm64.sh](arch/tools/bootstrap-arch-arm64.sh), [arch/systemd/aurora-mobile.service](arch/systemd/aurora-mobile.service) |
| Package matrix | [packaging/manifests/package-manager-matrix.toml](packaging/manifests/package-manager-matrix.toml) |
| Tests | [tests/](tests/) |
| Architecture docs | [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md), [arch/README.md](arch/README.md) |

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

## Android Edition

APK applications execute through an isolated Android compatibility target. The architecture keeps compatibility boundaries separate from the native mobile runtime.

## iOS-inspired Edition

Chimera does not claim Apple's proprietary iOS frameworks are open source. Instead it provides a Swift application target using the open-source Swift Package Manager, Swift Foundation/corelibs and SwiftNIO ecosystem.

## Store

Aurora Store presents package source, format, ABI, sandbox, capabilities, signature state and update channel before installation.

## Build and test

```bash
cmake -S mobile -B build/mobile -DCMAKE_BUILD_TYPE=Release
cmake --build build/mobile --parallel
ctest --test-dir build/mobile --output-on-failure
```

## Security

Every package path is expected to use hashes/signatures and a transactional install boundary. Untrusted package scripts cannot acquire host privileges simply because they were requested by a package. Production phone bring-up still requires verified boot, hardware-backed keys, encrypted storage, modem isolation, GPU/camera/audio/sensor HALs and physical-device performance/thermal validation.
