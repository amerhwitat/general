from __future__ import annotations
import hashlib, json, zipfile
from pathlib import Path
from dataclasses import dataclass

@dataclass
class ArtifactStore:
    root: Path = Path('data/artifacts')

    def save_project(self, name: str, files: dict[str, str], metadata: dict | None = None) -> dict:
        project = self.root / name
        project.mkdir(parents=True, exist_ok=True)
        for rel, content in files.items():
            target = project / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding='utf-8')
        manifest = {'name': name, 'files': sorted(files), 'metadata': metadata or {}}
        (project / 'artifact.json').write_text(json.dumps(manifest, indent=2), encoding='utf-8')
        digest = hashlib.sha256((project / 'artifact.json').read_bytes()).hexdigest()
        archive = self.root / f'{name}.zip'
        with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as zf:
            for path in project.rglob('*'):
                if path.is_file():
                    zf.write(path, path.relative_to(project))
        return {'directory': str(project), 'archive': str(archive), 'sha256': digest, 'files': sorted(files)}

    def save_binary(self, name: str, data: bytes) -> str:
        target = self.root / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        return str(target)
