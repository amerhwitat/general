@echo off
setlocal
cd /d "%~dp0.."
if exist .venv\Scripts\python.exe .venv\Scripts\python.exe -m compileall core_py utils
where dotnet >nul 2>&1 && dotnet build core_csharp\EmailExtractor.CSharp.csproj -c Release
where mvn >nul 2>&1 && mvn -f core_java\pom.xml -DskipTests package
where npm >nul 2>&1 && if exist ui_js\package.json (cd ui_js && npm run build && cd ..)
where php >nul 2>&1 && php -l core_php\extractor.php
where cargo >nul 2>&1 && cargo build --manifest-path core_rust\Cargo.toml
where cmake >nul 2>&1 && cmake -S native -B native\build -DCMAKE_BUILD_TYPE=Release
where cmake >nul 2>&1 && cmake --build native\build --config Release
echo Build sweep completed. Missing toolchains are skipped.
endlocal
