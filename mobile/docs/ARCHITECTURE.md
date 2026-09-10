# Chimera II OS Mobile Edition

## Purpose

This is a native mobile platform layer for Chimera II OS, inspired by the architectural lessons of Android/AOSP but implemented as a Chimera-native runtime. It is intended for ARM64 first, with future R8192/C8192 acceleration and x86-64 development/emulation.

## Stack

```text
Mobile Apps / Chimera Activities
        |
Compatibility APIs (Android-like lifecycle, Binder-like IPC, package model)
        |
Mobile System Services
 Activity | Package | Power | Input | Sensor | Connectivity | Media
        |
Aurora Mobile Compositor / Surface Manager
        |
Chimera Mobile Runtime + Adaptive Resource Fabric
        |
Koronos + Spotnik + Chimera VFS + HAL
        |
ARM64 / R8192 / C8192 / GPU / NPU / ISP / Modem / Sensors
```

## Adaptive Resource Fabric (ARF)

The missing cross-layer mechanism is an explicit policy plane joining frame deadlines, thermal state, battery state, memory pressure, foreground importance and accelerator availability. ARF continuously chooses performance, quality and background quotas instead of treating CPU frequency, application lifecycle, graphics and power as independent subsystems.

The first implementation is deterministic and testable in `mobile/src/power.cpp`. Hardware backends can later feed measured energy models, thermal zones and GPU/NPU telemetry.

## Android-derived compatibility boundary

The project intentionally separates API compatibility from source-code ownership. Binder-like transactions, activity lifecycle, package metadata, power modes and surface composition are native Chimera components. AOSP components are referenced through `third_party/aosp/UPSTREAMS.md` and may be imported only where their upstream licenses and build constraints permit.

## Performance targets

- 60/90/120/144 Hz frame scheduling without blocking the kernel.
- Foreground relaunch target below 1 s where hardware and storage permit.
- Bounded background work under thermal/battery pressure.
- Zero-copy buffers for large media/network transfers where ownership cost is lower than copying.
- 16 KiB page-size capable ARM64 memory model.
- ARM64 NEON/SVE and future Chimera vector/tensor acceleration.
- Measured, not assumed, thermal sustained-performance behavior.
