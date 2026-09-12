[CmdletBinding()]
param([switch]$Upgrade)
$ErrorActionPreference = 'Stop'
$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root
function Has($x) { return $null -ne (Get-Command $x -ErrorAction SilentlyContinue) }
Write-Host "== Email Extractor dependency installer ==" -ForegroundColor Cyan
if (-not (Has python)) { throw 'Python 3 is required.' }
if (-not (Test-Path '.venv')) { python -m venv .venv }
$Py = if (Test-Path '.venv/Scripts/python.exe') { '.venv/Scripts/python.exe' } else { '.venv/bin/python' }
& $Py -m pip install --upgrade pip setuptools wheel
& $Py -m pip install -e .
if (Has dotnet) { dotnet restore core_csharp/EmailExtractor.CSharp.csproj } else { Write-Warning 'dotnet not found; C# skipped.' }
if (Has npm) {
  if (Test-Path 'ui_js/package.json') { Push-Location ui_js; npm install; Pop-Location }
  if (Test-Path 'electron/package.json') { Push-Location electron; npm install; Pop-Location }
} else { Write-Warning 'npm not found; JavaScript skipped.' }
if (Has mvn) { mvn -f core_java/pom.xml dependency:go-offline } else { Write-Warning 'Maven not found; Java skipped.' }
if (Has composer) { composer install --working-dir core_php --no-interaction } else { Write-Warning 'Composer not found; PHP package setup skipped.' }
if (Has cargo) { cargo fetch --manifest-path core_rust/Cargo.toml } else { Write-Warning 'Cargo not found; Rust skipped.' }
if (Has cmake) { Write-Host 'CMake detected; native dependencies are toolchain-managed.' } else { Write-Warning 'CMake not found; native C/C++ skipped.' }
Write-Host 'Dependency installation completed (available toolchains only).' -ForegroundColor Green
