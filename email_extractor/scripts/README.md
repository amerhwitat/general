# Email Extractor Automation

Cross-platform automation for dependency installation, build verification, and launching the language-specific implementations.

## Commands

| Platform | Install | Build | Run |
|---|---|---|---|
| Windows CMD | `install-all.bat` | `build-all.bat` | `run-all.bat` |
| PowerShell | `install-all.ps1` | `build-all.ps1` | `run-all.ps1` |
| Linux/macOS/WSL | `bash install-all.sh` | `bash build-all.sh` | `bash run-all.sh` |

## Toolchains handled

- Python: local `.venv`, pip, package metadata
- C#: .NET SDK/NuGet restore and build
- Java: Maven dependency resolution and package build
- JavaScript/Electron: npm dependency installation and UI build
- PHP: Composer when available plus PHP syntax validation
- Rust: Cargo dependency fetch and build
- C/C++/ASM: CMake configure/build; compiler and assembler remain toolchain-specific

The scripts are intentionally idempotent where practical and detect missing tools rather than attempting privileged system modifications. Install OS-level toolchains separately when a machine does not have them.

## Build policy

Build scripts continue through the matrix so one unavailable language toolchain does not prevent unrelated implementations from being checked. A warning is printed for skipped or failed components. This is a build sweep, not a claim that every target can compile on every operating system.

## Run policy

The run scripts launch available application entry points. GUI and development-server processes may remain attached to their terminal/session. Review the target UI's README before using production deployment commands.

## Network and crawler policy

Automation only prepares and runs the existing public/authorized-web application. It does not add credential handling, access-control bypass, CAPTCHA evasion, robots bypass, private-network discovery, or anti-bot circumvention.
