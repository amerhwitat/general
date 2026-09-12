@echo off
if /I not "%1"=="--approved" (echo Refusing to build without explicit --approved & exit /b 2)
set LANGUAGE=%2
set PROJECT=%3
.venv\Scripts\python.exe -c "from AgentResearchForge.build.runner import build; import sys; print(build(sys.argv[1], sys.argv[2], approved=True))" "%LANGUAGE%" "%PROJECT%"
