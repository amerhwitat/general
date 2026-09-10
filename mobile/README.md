# Chimera II OS Mobile Edition

Android-like mobile platform for Chimera II OS, maintained exclusively in `amerhwitat/general`.

This is a native Chimera implementation with Android/AOSP compatibility boundaries, not a fork of the entire Android tree. It targets ARM64 mobile devices first and leaves clean extension points for R8192/C8192 acceleration.

## Current prototype

- application lifecycle/runtime
- Binder-like IPC bus
- package manager model
- adaptive power/thermal policy
- compositor/surface contract
- CMake build and conformance test
- AOSP provenance/import tooling

## Roadmap

1. Koronos mobile HAL and boot path
2. capability-based app sandbox
3. ART-compatible runtime bridge
4. Android API compatibility layer
5. GPU/display/input/camera/audio/sensor HALs
6. modem/Wi-Fi/Bluetooth/NFC/location services
7. encrypted storage and verified boot
8. Perfetto-compatible tracing and device benchmark suite
9. real ARM64 reference board/phone bring-up
