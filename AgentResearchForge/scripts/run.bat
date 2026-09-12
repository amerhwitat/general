@echo off
set "AGENT_HOST=%AGENT_HOST:127.0.0.1%"
if "%AGENT_HOST%"=="" set "AGENT_HOST=127.0.0.1"
set "AGENT_PORT=%AGENT_PORT:8000%"
if "%AGENT_PORT%"=="" set "AGENT_PORT=8000"
call .venv\Scripts\activate.bat
uvicorn AgentResearchForge.api.app:app --host %AGENT_HOST% --port %AGENT_PORT%
