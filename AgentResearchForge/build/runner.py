from __future__ import annotations
import subprocess
from pathlib import Path

COMMANDS = {
    'c': [['gcc', 'main.c', '-O2', '-o', 'main']],
    'cpp': [['g++', 'main.cpp', '-O2', '-o', 'main']],
    'rust': [['rustc', 'main.rs', '-O', '-o', 'main']],
    'go': [['go', 'build', '-o', 'main', 'main.go']],
    'java': [['javac', 'main.java']],
    'kotlin': [['kotlinc', 'main.kt', '-include-runtime', '-d', 'main.jar']],
    'swift': [['swiftc', 'main.swift', '-O', '-o', 'main']],
    'objective-c': [['clang', 'main.m', '-framework', 'Foundation', '-o', 'main']],
    'csharp': [['dotnet', 'build', '--nologo']],
}

def build(language: str, project_dir: str, approved: bool = False, timeout: int = 120) -> dict:
    if not approved:
        raise PermissionError('Explicit build approval is required')
    commands = COMMANDS.get(language.lower())
    if not commands:
        return {'language': language, 'built': False, 'reason': 'No fixed compiler recipe for this language; use its normal toolchain manually.'}
    root = Path(project_dir).resolve()
    if not root.is_dir(): raise FileNotFoundError(root)
    results=[]
    for command in commands:
        proc = subprocess.run(command, cwd=root, capture_output=True, text=True, timeout=timeout, check=False)
        results.append({'command': command, 'returncode': proc.returncode, 'stdout': proc.stdout[-4000:], 'stderr': proc.stderr[-4000:]})
        if proc.returncode != 0: return {'language': language, 'built': False, 'results': results}
    return {'language': language, 'built': True, 'results': results}
