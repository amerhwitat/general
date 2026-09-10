# Android + iOS compatibility boundaries

## Android

Chimera Mobile supports APK metadata and an isolated Android target. The target follows the Linux-container model used by Waydroid: Linux namespaces isolate user, PID, UTS, network, mount and IPC domains. citeturn1search13

The Android compatibility target maps Android lifecycle and Binder-style IPC to the existing Mobile Runtime/Binder layer. Hardware access remains under Koronos HAL policy.

## iOS-inspired Swift

Complete iOS is proprietary. Chimera does not claim or copy private Apple framework source. Instead, the compatible application layer uses open-source Swift components: Swift Package Manager, Swift Foundation/corelibs and SwiftNIO. citeturn1search0turn1search2turn1search3

Aurora supplies the Wayland graphics surface and Spotnik supplies networking primitives. This creates an iOS-inspired development model without falsely presenting proprietary iOS frameworks as open source.

## Store behavior

Aurora Store identifies each application by format, target runtime, ABI, capabilities, sandbox level, signature state and update channel. The user sees these before installation.
