# general

General-purpose utilities, experiments and shared research material in the Amer Hwitat repository family.

## Start here

1. Inspect the top-level directories and language-specific READMEs.
2. Run the repository build orchestrator if present:
   - Windows: `build-tools/build.bat`
   - PowerShell: `build-tools/build.ps1`
   - POSIX: `build-tools/build.sh`
3. Build only the detected language targets with `--only` where supported.

## Tooling

The build layer reports dependency detection, compilation, linking, packaging and artifact paths. It does not assume that every repository contains every language; unsupported targets are reported as skipped.

## CI

GitHub Actions is the reproducible CI path for Windows, Linux and macOS. Local builds should use the same manifests and entry points as CI.

## Generated artifacts

Build outputs belong under ignored build/dist/out directories or CI artifacts. Do not commit compiler-generated binaries unless they are intentional releases.
