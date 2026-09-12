[CmdletBinding()]
param([string[]]$Urls=@('https://example.com'))
$ErrorActionPreference='Continue'
$Root=Split-Path -Parent $PSScriptRoot; Set-Location $Root
function Start-App($label,$exe,[string[]]$args) { if (Get-Command $exe -ErrorAction SilentlyContinue) { Write-Host "Starting $label" -ForegroundColor Cyan; & $exe @args } else { Write-Warning "$exe not found; skipped $label" } }
$py = if (Test-Path '.venv/Scripts/python.exe') { '.venv/Scripts/python.exe' } elseif (Test-Path '.venv/bin/python') { '.venv/bin/python' } else { 'python' }
if (Test-Path 'ui_pyqt/main.py') { Start-App 'Python PyQt UI' $py @('ui_pyqt/main.py') }
if (Test-Path 'core_java/target/classes') { Start-App 'Java CLI/UI' 'java' @('-cp','core_java/target/classes','EmailExtractorUI') }
if (Test-Path 'ui_php/index.php') { Start-App 'PHP development server' 'php' @('-S','127.0.0.1:8080','-t','ui_php') }
if (Test-Path 'ui_js/package.json') { Start-App 'JavaScript UI' 'npm' @('--prefix','ui_js','run','start') }
if (Test-Path 'ui_rust/Cargo.toml') { Start-App 'Rust UI' 'cargo' @('run','--manifest-path','ui_rust/Cargo.toml') }
Write-Host 'Run sweep finished. GUI/server processes may remain attached to their terminals.' -ForegroundColor Green
