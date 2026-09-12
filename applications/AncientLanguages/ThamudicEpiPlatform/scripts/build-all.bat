@echo off
setlocal enabledelayedexpansion
for %%I in ("%~dp0..\..\..\..") do set "GENERAL=%%~fI"
set "NLP=%GENERAL%\..\nlp\ThamudicEpiPlatform"
if not exist "%NLP%" (
  echo Canonical nlp checkout not found: %NLP%
  exit /b 2
)
python -m venv "%NLP%\.venv"
"%NLP%\.venv\Scripts\python.exe" -m pip install -r "%NLP%\server\requirements.txt"
"%NLP%\.venv\Scripts\python.exe" -m pytest "%NLP%\server\tests" -q
where npm >nul 2>nul
if %errorlevel%==0 (
  pushd "%NLP%\web"
  call npm ci
  call npm run build
  popd
)
echo AncientLanguages build/test completed.
endlocal
