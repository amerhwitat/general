$ErrorActionPreference = 'Stop'
py -3 -m venv .venv
& .\.venv\Scripts\python.exe -m pip install --upgrade pip
& .\.venv\Scripts\python.exe -m pip install -e '.[api,documents]'
New-Item -ItemType Directory -Force data/uploads, data/artifacts, data/builds | Out-Null
Write-Host 'AgentResearchForge setup complete.'
Write-Host 'Set AGENT_SEARCH_URL and AGENT_LIBRARY_PATH before starting deep research.'
