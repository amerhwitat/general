# Mobile upstream provenance

## Linux packaging
- Debian: dpkg / apt / apt-get
- Arch: pacman / libalpm
- Fedora/RPM: rpm / dnf / yum compatibility
- Alpine: apk
- Nix: nix
- Flatpak: flatpak
- Snap: snap

## Mobile compatibility
- Android Open Source Project: Android runtime and APK ecosystem
- Waydroid: Linux Android container architecture
- Anbox: historical container architecture; archived upstream
- Swift Package Manager
- swift-foundation / swift-corelibs-foundation
- SwiftNIO

## Rule
Use official upstream acquisition and retain each upstream's license/NOTICE. Do not vendor proprietary Apple iOS frameworks. Do not claim Android system images or third-party applications are owned by Chimera.
