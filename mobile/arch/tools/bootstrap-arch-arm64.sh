#!/usr/bin/env bash
set -euo pipefail
ROOTFS="${1:-rootfs}"
MIRROR="${ARCH_MIRROR:-https://os.archlinuxarm.org/os/}"
TARBALL="${ARCH_TARBALL:-ArchLinuxARM-aarch64-latest.tar.gz}"
WORK="${TMPDIR:-/tmp}/chimera-arch"
mkdir -p "$ROOTFS" "$WORK" "$ROOTFS/etc/chimera/mobile" "$ROOTFS/etc/mkinitcpio.d"
if command -v curl >/dev/null; then curl -fL "$MIRROR$TARBALL" -o "$WORK/$TARBALL"; elif command -v wget >/dev/null; then wget -O "$WORK/$TARBALL" "$MIRROR$TARBALL"; else echo 'curl or wget required' >&2; exit 2; fi
bsdtar -xpf "$WORK/$TARBALL" -C "$ROOTFS"
cat > "$ROOTFS/etc/chimera/mobile/profile.conf" <<'EOF'
ARCHITECTURE=aarch64
PAGE_SIZE=16384
DISPLAY_SERVER=wayland
DESKTOP=AURORA
KERNEL_OWNER=koronos
NETWORK_OWNER=spotnik
SERVICE_OWNER=kore
EXECUTION=ARM64,R8192,C8192,NBIT
EOF
echo "Arch Linux ARM64 userspace staged for Chimera II Mobile: $ROOTFS"
