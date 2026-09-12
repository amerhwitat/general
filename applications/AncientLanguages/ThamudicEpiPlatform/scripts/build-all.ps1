$ErrorActionPreference = 'Stop'
$RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot '..\..\..\..')).Path
$Nlp = Join-Path (Split-Path $RepoRoot -Parent) 'nlp\ThamudicEpiPlatform'
if (-not (Test-Path $Nlp)) { throw "Canonical nlp checkout not found: $Nlp" }
$venv = Join-Path $Nlp '.venv'
python -m venv $venv
& (Join-Path $venv 'Scripts\python.exe') -m pip install -r (Join-Path $Nlp 'server\requirements.txt')
& (Join-Path $venv 'Scripts\python.exe') -m pytest (Join-Path $Nlp 'server\tests') -q
if (Get-Command npm -ErrorAction SilentlyContinue) { Push-Location (Join-Path $Nlp 'web'); npm ci; npm run build; Pop-Location }
Write-Host 'AncientLanguages build/test completed.'
