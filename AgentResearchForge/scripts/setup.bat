@echo off
setlocal
py -3 -m venv .venv
call .venv\Scripts\activate.bat
python -m pip install --upgrade pip
python -m pip install -e ".[api,documents]"
if not exist data\uploads mkdir data\uploads
if not exist data\artifacts mkdir data\artifacts
if not exist data\builds mkdir data\builds
echo AgentResearchForge setup complete.
echo Set AGENT_SEARCH_URL and AGENT_LIBRARY_PATH before starting deep research.
