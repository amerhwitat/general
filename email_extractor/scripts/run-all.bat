@echo off
setlocal
cd /d "%~dp0.."
if exist ui_pyqt\main.py if exist .venv\Scripts\python.exe start "Email Extractor Python" .venv\Scripts\python.exe ui_pyqt\main.py
if exist core_java\target\classes start "Email Extractor Java" java -cp core_java\target\classes EmailExtractorUI
if exist ui_php\index.php start "Email Extractor PHP" cmd /c "php -S 127.0.0.1:8080 -t ui_php"
if exist ui_js\package.json start "Email Extractor JS" cmd /c "cd /d ui_js && npm run start"
if exist ui_rust\Cargo.toml start "Email Extractor Rust" cmd /c "cargo run --manifest-path ui_rust\Cargo.toml"
echo Run sweep launched available applications.
endlocal
