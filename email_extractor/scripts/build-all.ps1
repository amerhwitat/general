[CmdletBinding()]
param([ValidateSet('Debug','Release')][string]$Configuration='Release')
$ErrorActionPreference='Continue'
$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root
function Run($label,$cmd,[string[]]$args) { Write-Host "`n--- $label ---" -ForegroundColor Cyan; if (Get-Command $cmd -ErrorAction SilentlyContinue) { & $cmd @args; if ($LASTEXITCODE -ne 0) { Write-Warning "$label failed ($LASTEXITCODE)" } } else { Write-Warning "$cmd not found; skipped $label" } }
if (Test-Path '.venv/Scripts/python.exe') { Run 'Python compile' '.venv/Scripts/python.exe' @('-m','compileall','core_py','utils') } elseif (Test-Path '.venv/bin/python') { Run 'Python compile' '.venv/bin/python' @('-m','compileall','core_py','utils') } else { Run 'Python compile' 'python' @('-m','compileall','core_py','utils') }
Run 'C# build' 'dotnet' @('build','core_csharp/EmailExtractor.CSharp.csproj','-c',$Configuration)
Run 'Java build' 'mvn' @('-f','core_java/pom.xml','-DskipTests','package')
Run 'JavaScript dependency/build' 'npm' @('--prefix','ui_js','run','build')
Run 'PHP syntax check' 'php' @('-l','core_php/extractor.php')
Run 'Rust build' 'cargo' @('build','--manifest-path','core_rust/Cargo.toml')
Run 'C/C++ CMake configure' 'cmake' @('-S','native','-B','native/build','-DCMAKE_BUILD_TYPE='+$Configuration)
Run 'C/C++ CMake build' 'cmake' @('--build','native/build','--config',$Configuration)
Write-Host "`nBuild sweep completed. Missing toolchains were skipped; failures are reported above." -ForegroundColor Green
