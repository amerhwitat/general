# Chimera II OS Mobile Edition — Universal Application and Package Architecture

## 1. One Mobile Edition, multiple application worlds

```text
Aurora Wayland Glass Store
          |
     Mobile Package Fabric
          |
 +--------+---------+----------------+
 |        |         |                |
 .deb    RPM      pacman/APK     Flatpak/Snap
 |        |         |                |
 dpkg   rpm/dnf   libalpm/apk      sandbox
          |
   Android APK container       Swift/SwiftPM
          |                         |
          +-----------+-------------+
                      |
             Koronos + HAL + ARF
                      |
       ARM64 / N-bit / GPU / NPU / ISP
```

The central abstraction is package identity + target ABI + provenance + signature + sandbox + transaction. Package managers remain semantically distinct; Chimera routes them through one security and lifecycle policy.

## 2. Debian edition

Debian uses `dpkg` as the low-level package manager and APT as the higher-level resolver/front end. `apt-get` remains appropriate for scripts while `apt` provides the human-facing interface. citeturn0search3turn0search11

Chimera Mobile therefore permits `.deb` installation but puts it through an atomic staging transaction, ARM64 architecture validation, digest/signature checks and sandboxed maintainer-script policy.

## 3. Arch edition

`pacman` manages installed packages, dependencies, package groups and repository synchronization and is backed by `libalpm`. citeturn0search2

Arch remains the reference native userspace for the Mobile Edition.

## 4. RPM edition

The RPM family is represented by `rpm`, `dnf` and the legacy-compatible `yum` command path. Fedora documents DNF as the successor to YUM and the higher-level manager around RPM. citeturn0search0turn0search12

## 5. Alpine edition

`apk` is represented as the Alpine Package Keeper adapter. Alpine documents it as its primary package-management mechanism with repository/mirror concepts. citeturn0search16

## 6. Sandboxed universal applications

Flatpak is integrated as a sandboxed application target with explicit portals and permissions. Its model isolates host files, network, devices and processes by default and grants access through explicit permissions/portals. citeturn0search6turn0search8

Snap is represented as a separate bundle/store target; its store/distribution model is retained rather than translated into Debian packages. citeturn0search10

Nix is represented as a declarative/user-environment target, preserving its separate model instead of pretending it is a conventional mutable package database. citeturn0search5

## 7. Android Edition

Android runs as a compatibility target/container rather than replacing Koronos. Waydroid is the current architectural reference because it uses Linux namespaces to run a full Android system and provides Android applications on Linux; Anbox is historical because its repository is archived. citeturn1search13turn1search10

APK is therefore a first-class package format, but Android privileges and hardware access remain controlled by Chimera's capability/security layer.

## 8. iOS-inspired Edition

There is no open-source copy of Apple's complete iOS framework stack. Chimera therefore integrates the open-source Swift ecosystem instead: Swift Package Manager, Swift Foundation/corelibs and SwiftNIO. Swift Foundation provides portable Foundation APIs for non-Darwin systems, while SwiftNIO supplies cross-platform non-blocking networking. citeturn1search0turn1search2turn1search3

Proprietary Apple frameworks are explicitly outside the open-source integration boundary.

## 9. New method: Universal Package Graph

The Mobile Package Fabric builds a graph where each application has:
- package format
- target ABI
- runtime
- dependency edges
- signature/provenance
- permissions
- resource budget
- rollback snapshot

The same application can therefore expose a Debian build, RPM build, Flatpak bundle, APK, Swift package or source build without collapsing their distinct security semantics.

## 10. New method: Capability Translation Layer

Instead of translating package managers only, Chimera translates requested capabilities: filesystem, network, camera, sensors, GPU, microphone, notification, background execution and privileged services. The Aurora Store can show these capabilities before installation and the runtime enforces them after installation.

This combines the Android permission/lifecycle idea, iOS capability-oriented app model, Flatpak portal model and Chimera's existing capability enforcement into one mobile policy plane.

## 11. N-bit integration

Native ARM64 remains the default. N-bit execution is promoted only for workloads requiring 4096/8192/16384-bit or arbitrary-width state, matching the existing RegisterN direction in the Library. fileciteturn17file0L106-L140

## 12. Provenance rule

The repository stores adapters, manifests, compatibility code and acquisition scripts. It does not silently vendor complete AOSP, iOS, Debian, Arch, Fedora, Alpine, Flatpak, Snap or Nix trees. Each upstream remains separately licensed and reproducibly acquired.
