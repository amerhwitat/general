# Chimera Mobile Universal Packaging Implementation Plan

Goal: unify Debian, Android, iOS/Swift-inspired and Linux package ecosystems under a signed, sandboxed Mobile Package Fabric while keeping Koronos as kernel authority.

Architecture: adapters for pacman, dpkg/apt, rpm/dnf/yum, apk, nix, flatpak, snap, AppImage and source/git; isolated Android target inspired by Waydroid; open-source SwiftPM/Foundation/SwiftNIO compatibility target; Aurora Glass application store.

Constraints: changes only in `amerhwitat/general`; .deb is supported transactionally; untrusted maintainer scripts cannot bypass security; proprietary Apple/iOS source is not claimed as open source; upstream ecosystems are acquired reproducibly; N-bit state remains lazy.

Sequence: package fabric core; Linux adapters; Debian .deb path; Android/APK target; Swift/iOS target; unified store/CLI; documentation/provenance/CI; review/merge.

Tests: CMake/CTest for package detection, ABI targeting, signature/hash policy, transactions, command routing, Android/iOS target selection and store filtering. Device bring-up remains a separate hardware gate.
