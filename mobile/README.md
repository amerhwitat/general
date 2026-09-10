# Chimera II OS Mobile Edition

Android-like, Arch-based mobile platform for Chimera II OS, maintained exclusively in `amerhwitat/general`.

This is a native Chimera implementation with Android/AOSP compatibility boundaries. It is not a fork of the entire Android tree. ARM64 is the primary mobile target; R8192/C8192 and arbitrary N-bit execution are acceleration/emulation paths.

## Integrated stack

- Koronos kernel boundary
- Spotnik networking boundary
- Arch Linux ARM64 userspace/profile with pacman + systemd-compatible services
- Aurora Wayland Glass touch-first shell
- Android-like application lifecycle and Binder-like IPC
- Package, power, thermal and graphics contracts
- Adaptive Resource Fabric (ARF)
- 16 KiB ARM64 page profile
- 64/128/256/512/1024/2048/4096/8192/16384-bit fixed-width registers
- arbitrary runtime-width `WideInt` N-bit emulation
- lazy wide-context execution selection
- reproducible Arch ARM64 rootfs bootstrap
- Library provenance and implementation manifest

## N-bit model

`RegisterN<Bits>` is width-parametric for every positive width divisible by 64. Named aliases cover 64 through 16384 bits. `WideInt` covers arbitrary runtime widths. Ordinary mobile threads retain compact ARM64 state; wide state is promoted only for workloads that request it.

## Arch model

Arch is the userspace distribution/profile, not the kernel. Koronos owns boot/HAL/capability/device policy; Arch supplies the familiar POSIX/GNU userspace and pacman package workflow. The reference rootfs follows the generic Arch Linux ARM AArch64 developer model.

## Aurora model

Aurora is the default Wayland-oriented graphical shell. The supplied `Aurora Wayland Glass Desktop.png` Library artwork is the canonical visual reference. The repository shell provides a responsive touch UI and a lightweight CSS fallback; the exact raster asset can be inserted by the device-image packaging stage without coupling the runtime to a large binary.

## Build and test

```bash
cmake -S mobile -B build/mobile -DCMAKE_BUILD_TYPE=Release
cmake --build build/mobile --parallel
ctest --test-dir build/mobile --output-on-failure
```

## Security gates before production-phone claims

Verified boot, package signature verification, capability sandboxing, rollback protection, encrypted user storage, hardware-backed keys, modem/network isolation and target-device thermal/power validation remain mandatory production gates.
