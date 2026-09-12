param([switch]$Approved, [Parameter(Mandatory=$true)][string]$Language, [Parameter(Mandatory=$true)][string]$Project)
if (-not $Approved) { throw 'Refusing to build without -Approved' }
& .\.venv\Scripts\python.exe -c "from AgentResearchForge.build.runner import build; import sys; print(build(sys.argv[1], sys.argv[2], approved=True))" $Language $Project
