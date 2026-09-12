@echo off
setlocal
cd /d "%~dp0.."
echo === Email Extractor dependency installer ===
where py >nul 2>&1
if errorlevel 1 (echo Python launcher not found. & exit /b 1)
if not exist .venv\Scripts\python.exe py -3 -m venv .venv
.venv\Scripts\python.exe -m pip install --upgrade pip setuptools wheel
.venv\Scripts\python.exe -m pip install -e .
where dotnet >nul 2>&1 && dotnet restore core_csharp\EmailExtractor.CSharp.csproj
where npm >nul 2>&1 && if exist ui_js\package.json (cd ui_js && npm install && cd ..)
where mvn >nul 2>&1 && mvn -f core_java\pom.xml dependency:go-offline
where composer >nul 2>&1 && if exist core_php\composer.json composer install --working-dir core_php --no-interaction
where cargo >nul 2>&1 && cargo fetch --manifest-path core_rust\Cargo.toml
where cmake >nul 2>&1 && cmake --version
echo Dependency installation completed for available toolchains.
endlocal
