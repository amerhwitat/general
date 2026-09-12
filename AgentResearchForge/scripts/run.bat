@echo off
call .venv\Scripts\activate.bat
uvicorn AgentResearchForge.api.app:app --host %AGENT_HOST% --port %AGENT_PORT%
