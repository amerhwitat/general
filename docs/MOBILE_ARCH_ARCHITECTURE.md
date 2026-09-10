# Chimera II OS Mobile Edition — Arch + N-bit + Aurora

## Architecture

```text
                Aurora Wayland Glass
                         |
             Android-like Mobile APIs
                         |
        Activity / Binder / Package / Media
                         |
                 Adaptive Resource Fabric
            /             |              \
       thermal         memory          frame
       battery          network       accelerator
                         |
                     Koronos
                         |
        +----------------+----------------+
        |                |                |
     Spotnik          Chimera VFS        HAL
        |                                 |
   Arch ARM64 userspace          ARM64 / GPU / NPU / ISP
                                          |
                         +----------------+----------------+
                         |        N-bit execution         |
                         | 64/128/256/512/1024/2048/...   |
                         | 4096 / 8192 / 16384 / runtime N|
                         +--------------------------------+
```

### Arch boundary
Arch Linux supplies the configurable userspace and package ecosystem. Koronos remains the kernel and device authority. This follows the Arch ARM generic AArch64 model, where developers provide their own boot functionality. citeturn0search11

The package baseline is `pacman` plus the Arch ARM64 systemd userspace. Current Arch Linux ARM packages demonstrate both are available for AArch64. citeturn0search0turn0search1

### Wayland/Aurora boundary
Wayland's model is client/compositor based: clients submit buffers and the compositor arbitrates presentation and input. Aurora implements the Chimera mobile policy and visual shell above this protocol rather than replacing the protocol itself. citeturn0search2turn0search19

### N-bit boundary
The N-bit layer is a software-defined execution facility. The supplied Chimera specifications describe 8192-bit registers, 128×64-bit logical lanes and R8192/C8192 modes as research targets rather than existing silicon. The mobile design therefore keeps ordinary ARM64 application contexts compact and promotes wide state lazily for workloads that need it. fileciteturn13file2L222-L228

The fixed-width implementation covers 64 through 16384 bits, while `WideInt` supports arbitrary runtime widths. This preserves the earlier 4096→8192→N-bit direction without forcing every thread to carry the largest context.

## Aurora visual reference

The canonical visual source is the Library asset `Aurora Wayland Glass Desktop.png`, which shows the intended translucent launcher, top bar, system widgets, dock, mountain/lake background and Aurora identity. The mobile implementation keeps those design cues and collapses them responsively into a touch-first layout. fileciteturn14file10L67-L71

The repo's HTML shell deliberately uses a lightweight CSS fallback so it remains buildable without embedding a large raster file. The exact Library image remains the design reference and can be packaged into device images when the distribution artifact pipeline is enabled.

## Performance policy

16 KiB pages are the reference ARM64 mobile profile. AOSP currently publishes 16 KiB GKI release builds, so the choice is compatible with the direction of modern Android ARM64 systems. citeturn0search18

ARF combines frame deadline, thermal, battery, memory and accelerator signals. It is deliberately a policy plane, not a benchmark claim; real phones must supply measured telemetry and sustained-performance data.
