$ErrorActionPreference = 'Stop'
$hostAddress = if ($env:AGENT_HOST) { $env:AGENT_HOST } else { '127.0.0.1' }
$port = if ($env:AGENT_PORT) { $env:AGENT_PORT } else { '8000' }
& .\.venv\Scripts\uvicorn.exe AgentResearchForge.api.app:app --host $hostAddress --port $port
