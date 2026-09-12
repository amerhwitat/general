$ErrorActionPreference = 'Stop'
$RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..\..\..\..')).Path
$Nlp = Join-Path (Split-Path $RepoRoot -Parent) 'nlp\ThamudicEpiPlatform'
if (-not (Test-Path $Nlp)) { throw "Canonical nlp checkout not found: $Nlp" }
& (Join-Path $Nlp 'scripts\check-dependencies.ps1')
$python = Join-Path $Nlp '.venv\Scripts\python.exe'
& $python -m pytest (Join-Path $Nlp 'server\tests') -q
if (Get-Command npm -ErrorAction SilentlyContinue) { Push-Location (Join-Path $Nlp 'web'); npm ci; npm run build; Pop-Location }
Write-Host 'AncientLanguages build/test completed with OCR dependency checks.'
