from dataclasses import dataclass, field

SUPPORTED = ('python','typescript','javascript','c','cpp','csharp','java','kotlin','go','rust','swift','objective-c','php','ruby','dart','julia','r','lua','bash','powershell','sql','html','css','webassembly')

@dataclass
class ProjectManifest:
    name: str
    description: str
    language: str
    files: dict[str, str] = field(default_factory=dict)
    execute_after_review: bool = False

class ProjectGenerator:
    def plan(self, description: str, language: str = 'python') -> ProjectManifest:
        language = language.lower()
        if language not in SUPPORTED:
            raise ValueError(f'Unsupported language: {language}')
        name = ''.join(c if c.isalnum() else '-' for c in description.lower()).strip('-')[:48] or 'generated-project'
        return ProjectManifest(name, description, language)

    def render(self, manifest: ProjectManifest) -> ProjectManifest:
        if manifest.language == 'python':
            manifest.files['README.md'] = f'# {manifest.name}\n\n{manifest.description}\n'
            manifest.files['main.py'] = 'def main():\n    print("Generated project; review before execution.")\n\nif __name__ == "__main__":\n    main()\n'
        elif manifest.language in {'typescript','javascript'}:
            ext = 'ts' if manifest.language == 'typescript' else 'js'
            manifest.files[f'main.{ext}'] = 'console.log("Generated project; review before execution.");\n'
        else:
            manifest.files['README.md'] = f'# {manifest.name}\n\n{manifest.description}\n\nGenerated artifact; review before execution.\n'
        return manifest
