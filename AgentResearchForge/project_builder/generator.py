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
        ext = {'python':'py','typescript':'ts','javascript':'js','c':'c','cpp':'cpp','csharp':'cs','java':'java','kotlin':'kt','go':'go','rust':'rs','swift':'swift','objective-c':'m','php':'php','ruby':'rb','dart':'dart','julia':'jl','r':'R','lua':'lua','bash':'sh','powershell':'ps1','sql':'sql','html':'html','css':'css','webassembly':'wat'}[manifest.language]
        templates = {
            'python': 'def main():\n    print("Generated project; review before execution.")\n\nif __name__ == "__main__":\n    main()\n',
            'typescript': 'export function main(): void { console.log("Generated project; review before execution."); }\nmain();\n',
            'javascript': 'function main() { console.log("Generated project; review before execution."); }\nmain();\n',
            'c': '#include <stdio.h>\nint main(void) { puts("Generated project; review before execution."); return 0; }\n',
            'cpp': '#include <iostream>\nint main() { std::cout << "Generated project; review before execution.\\n"; }\n',
            'csharp': 'using System;\nclass Program { static void Main() => Console.WriteLine("Generated project; review before execution."); }\n',
            'java': 'class Main { public static void main(String[] args) { System.out.println("Generated project; review before execution."); } }\n',
            'kotlin': 'fun main() = println("Generated project; review before execution.")\n',
            'go': 'package main\nimport "fmt"\nfunc main() { fmt.Println("Generated project; review before execution.") }\n',
            'rust': 'fn main() { println!("Generated project; review before execution."); }\n',
            'swift': 'print("Generated project; review before execution.")\n',
            'objective-c': '#import <Foundation/Foundation.h>\nint main(void) { @autoreleasepool { NSLog(@"Generated project; review before execution."); } return 0; }\n',
            'php': '<?php echo "Generated project; review before execution.\\n";\n',
            'ruby': 'puts "Generated project; review before execution."\n',
            'dart': 'void main() { print("Generated project; review before execution."); }\n',
            'julia': 'println("Generated project; review before execution.")\n',
            'r': 'cat("Generated project; review before execution.\\n")\n',
            'lua': 'print("Generated project; review before execution.")\n',
            'bash': '#!/usr/bin/env bash\nset -euo pipefail\necho "Generated project; review before execution."\n',
            'powershell': 'Write-Output "Generated project; review before execution."\n',
            'sql': 'SELECT \'Generated project; review before execution.\' AS message;\n',
            'html': '<!doctype html><html><body><h1>Generated project</h1><p>Review before deployment.</p></body></html>\n',
            'css': 'body { font-family: system-ui, sans-serif; }\n/* Generated project; review before deployment. */\n',
            'webassembly': '(module (func (export "main")))\n',
        }
        manifest.files['README.md'] = f'# {manifest.name}\n\n{manifest.description}\n\nGenerated artifact; review before execution or deployment.\n'
        manifest.files[f'main.{ext}'] = templates[manifest.language]
        manifest.files['LICENSE-NOTICE.md'] = 'Generated from AgentResearchForge templates. Verify third-party licenses for any retrieved code before redistribution.\n'
        return manifest
