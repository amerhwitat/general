$ErrorActionPreference='Stop'
$Root=(Resolve-Path "$PSScriptRoot\..\..\..\..").Path
$Nlp=Join-Path (Split-Path $Root -Parent) 'nlp'
if(-not (Test-Path $Nlp)){throw "Missing canonical nlp checkout: $Nlp"}
$Sha=(git -C $Nlp rev-parse HEAD 2>$null)
$Status=@{canonical_repository='amerhwitat/nlp';canonical_sha=$Sha;path='ThamudicEpiPlatform';checked_at=(Get-Date).ToUniversalTime().ToString('o')}
$Status | ConvertTo-Json | Set-Content (Join-Path $Root 'applications\AncientLanguages\ThamudicEpiPlatform\data\sync-status.json')
Write-Host "Canonical nlp revision: $Sha"
