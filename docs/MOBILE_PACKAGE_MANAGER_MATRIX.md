# Mobile package-manager matrix

| Ecosystem | Format | Native adapter | Mobile policy |
|---|---|---|---|
| Arch | pkg.tar.* | pacman/libalpm | Native ARM64 userspace |
| Debian | .deb | dpkg + apt/apt-get | Transactional + signed |
| Ubuntu/Debian derivatives | .deb | apt/apt-get | Transactional + signed |
| Fedora/RHEL | .rpm | rpm + dnf | Transactional + signed |
| Legacy Fedora/RPM | .rpm | rpm + yum | Compatibility path |
| Alpine | .apk | apk | Native/isolated |
| Nix | derivation/store | nix | Declarative/user scoped |
| Flatpak | flatpak bundle | flatpak | Sandboxed/portal |
| Snap | snap | snap | Sandboxed/service policy |
| AppImage | AppImage | extractor/runner | Portable sandbox |
| Android | APK | Android target | Namespace/container sandbox |
| Swift | SwiftPM | swift package | Swift runtime sandbox |
| Git/GitHub | source | git/gh | Source-build sandbox |

The goal is compatibility, not semantic flattening. Each ecosystem retains its dependency, update and trust model while Chimera adds a common provenance/capability layer.
