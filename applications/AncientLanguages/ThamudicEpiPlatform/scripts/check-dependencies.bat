@echo off
setlocal
cd /d "%~dp0.."
py -3 -m venv .venv
.venv\Scripts\python.exe -m pip install --upgrade pip
set "NLP_ROOT=%~dp0..\..\..\..\nlp\ThamudicEpiPlatform"
.venv\Scripts\python.exe -m pip install -r "%NLP_ROOT%\server\requirements.txt"
if "%INSTALL_OCR_EXTRAS%"=="1" .venv\Scripts\python.exe -m pip install "kraken>=7,<8" "easyocr>=1.7,<2" "paddleocr>=3,<4"
.venv\Scripts\python.exe -c "import PIL,numpy,cv2,fastapi,pypdf,reportlab; print('OCR/API dependencies: OK')"
