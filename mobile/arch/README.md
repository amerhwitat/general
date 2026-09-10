# Arch Linux on Chimera II OS Mobile Edition

Arch is integrated as an ARM64 userspace/profile above Koronos rather than replacing the Chimera kernel. This preserves Chimera's boot, HAL, capability, graphics, networking and N-bit execution contracts while adopting Arch's minimal, user-controlled package model.

Current reference: Arch Linux ARM generic AArch64 userspace, pacman, systemd-compatible services, 16 KiB page profile, Aurora Wayland shell, Spotnik networking and lazy N-bit acceleration.

The generic AArch64 Arch Linux ARM installation is intended for developers who provide their own boot functionality, which maps cleanly to the Chimera Spit Fire/Jasper/Koronos stack. citeturn0search11

Arch's current ARM64 package ecosystem includes pacman and systemd, so those remain the baseline userspace components rather than reimplementing package management. citeturn0search0turn0search1

Use `tools/bootstrap-arch-arm64.sh` to stage the root filesystem. The script intentionally does not install a kernel: Koronos/HAL owns the mobile boot boundary.
