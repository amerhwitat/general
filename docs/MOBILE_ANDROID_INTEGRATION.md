# Chimera II OS Mobile / Android-Compatible Edition

## Scope

`general` is now the isolated home for the Chimera II OS Mobile Edition. Existing Chimera repositories remain untouched by this mobile implementation.

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

## Compatibility strategy

1. Preserve Android application concepts where useful.
2. Keep the Chimera ABI and kernel ownership authoritative.
3. Provide Android-like APIs/adapters instead of coupling Koronos to Android internals.
4. Allow AOSP components to run in a compatibility environment when their license and dependency closure permit it.
5. Prefer native Chimera implementations for core mobile services.
6. Record every upstream component, license and version in the provenance manifest.

## Security

Package installation requires a signature flag in the initial API. Production implementation must add cryptographic verification, rollback protection, per-package UID/GID isolation, SELinux-equivalent policy or a Chimera capability policy, verified boot and encrypted user storage.

## Performance research basis

Current AOSP compatibility documentation emphasizes frame-latency consistency, task switching, storage I/O, power attribution and sustained performance. Linux Energy Aware Scheduling provides an established model for heterogeneous CPU power/performance decisions. These are adopted as engineering targets and design inputs, not as claims that the current prototype already meets them.

## Build

```bash
cmake -S mobile -B build/mobile -DCMAKE_BUILD_TYPE=Release
cmake --build build/mobile -j
ctest --test-dir build/mobile --output-on-failure
```
