# Chimera II OS Mobile / Android-Compatible Edition

## Scope

`general` is the isolated home for the Chimera II OS Mobile Edition. Existing Chimera repositories remain untouched by this mobile implementation.

The design uses AOSP as a reference and selectively imports compatible open-source components through reproducible upstream manifests. It does not pretend that the entire Android source tree can be safely copied into a small repository.

## Android architectural components mapped into Chimera

| Android/AOSP concept | Chimera Mobile component |
|---|---|
| Binder IPC | `mobile/include/chimera/mobile/binder.hpp` |
| Activity/task lifecycle | `mobile/include/chimera/mobile/runtime.hpp` |
| PackageManager | `mobile/include/chimera/mobile/package_manager.hpp` |
| PowerManager | `mobile/include/chimera/mobile/power.hpp` |
| Surface/compositor path | `mobile/include/chimera/mobile/graphics.hpp` |
| HAL | Koronos/HAL contracts in the parent Chimera architecture |
| ART/runtime | Future `mobile/runtime/art-bridge` compatibility boundary |
| init/service manager | Kore-compatible mobile service profile |
| VFS | Existing Chimera universal VFS |
| Networking | Spotnik |

## Resharpening principle

**One mobile policy plane, many execution engines.** Application importance, frame deadlines, memory pressure, thermal headroom, battery state, network state and accelerator queues become one scheduling signal. This avoids the common gap where lifecycle, scheduler, compositor and power manager each optimize locally while harming the device globally.

## Performance-derived design decisions

AOSP's current compatibility requirements emphasize consistent frame latency, low task-switch latency, storage I/O, per-component power accounting and sustained-performance behavior. Linux Energy Aware Scheduling provides an established heterogeneous-CPU energy model. Chimera therefore keeps power policy explicit rather than burying it in a single frequency governor. citeturn0search0turn0search3

AOSP now supports 16 KiB page-size builds on ARM64, and current Android common kernels include 16 KiB GKI builds. Chimera Mobile therefore treats 16 KiB pages as the reference ARM64 configuration while keeping allocations page-size aware. citeturn1search0turn1search4

Thermal management is a first-class service boundary: AOSP's current thermal architecture exposes thermal data and policy-driven throttling to the framework. Chimera's Adaptive Resource Fabric follows the same separation while keeping the policy implementation native to Chimera. citeturn1search14

## Compatibility strategy

1. Preserve Android application concepts where useful.
2. Keep the Chimera ABI and kernel ownership authoritative.
3. Provide Android-like APIs/adapters instead of coupling Koronos to Android internals.
4. Allow AOSP components to run in a compatibility environment when their license and dependency closure permit it.
5. Prefer native Chimera implementations for core mobile services.
6. Record every upstream component, license and version in the provenance manifest.

## Security

Package installation requires a signature flag in the initial API. Production implementation must add cryptographic verification, rollback protection, per-package UID/GID isolation, SELinux-equivalent policy or a Chimera capability policy, verified boot and encrypted user storage.

## Build

```bash
cmake -S mobile -B build/mobile -DCMAKE_BUILD_TYPE=Release
cmake --build build/mobile -j
ctest --test-dir build/mobile --output-on-failure
```
