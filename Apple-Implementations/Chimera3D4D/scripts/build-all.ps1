$ErrorActionPreference = 'Stop'
$root = Split-Path -Parent $PSScriptRoot
Push-Location $root
try {
  cmake -S . -B build -DCMAKE_BUILD_TYPE=Release
  cmake --build build --parallel
  ctest --test-dir build --output-on-failure

  if (Get-Command flutter -ErrorAction SilentlyContinue) {
    Push-Location flutter
    try { flutter pub get; flutter analyze; flutter build web --release } finally { Pop-Location }
  }

  if (Get-Command npm -ErrorAction SilentlyContinue) {
    Push-Location web
    try { npm install; npm run build } finally { Pop-Location }
  }
} finally {
  Pop-Location
}
