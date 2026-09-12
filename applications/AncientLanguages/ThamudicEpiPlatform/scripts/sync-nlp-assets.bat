@echo off
setlocal
for %%I in ("%~dp0..\..\..\..") do set "ROOT=%%~fI"
set "NLP=%ROOT%\..\nlp"
if not exist "%NLP%" (echo Missing canonical nlp checkout: %NLP% & exit /b 2)
for /f %%S in ('git -C "%NLP%" rev-parse HEAD') do set "SHA=%%S"
> "%ROOT%\applications\AncientLanguages\ThamudicEpiPlatform\data\sync-status.json" echo {"canonical_repository":"amerhwitat/nlp","canonical_sha":"%SHA%","path":"ThamudicEpiPlatform"}
echo Canonical nlp revision: %SHA%
endlocal
