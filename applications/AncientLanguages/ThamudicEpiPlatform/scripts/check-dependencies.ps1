$ErrorActionPreference='Stop'
$Root=Resolve-Path "$PSScriptRoot\.."; Set-Location $Root
py -3 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
$NlpRoot=Resolve-Path "$Root\..\..\..\..\..\nlp\ThamudicEpiPlatform"
.\.venv\Scripts\python.exe -m pip install -r "$NlpRoot\server\requirements.txt"
if($env:INSTALL_OCR_EXTRAS -eq '1'){.\.venv\Scripts\python.exe -m pip install 'kraken>=7,<8' 'easyocr>=1.7,<2' 'paddleocr>=3,<4'}
.\.venv\Scripts\python.exe -c "import PIL,numpy,cv2,fastapi,pypdf,reportlab; print('OCR/API dependencies: OK')"
