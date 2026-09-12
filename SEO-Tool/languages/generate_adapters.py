from pathlib import Path
LANGS={'python':('python','python -m SEO_Tool.cli'),'javascript':('javascript','node'),'typescript':('typescript','npx tsx'),'c':('c','./seo-tool'),'cpp':('cpp','./seo-tool'),'csharp':('csharp','dotnet run'),'java':('java','java'),'kotlin':('kotlin','kotlin'),'go':('go','go run'),'rust':('rust','cargo run'),'swift':('swift','swift run'),'objective-c':('objective-c','./seo-tool'),'php':('php','php'),'ruby':('ruby','ruby'),'dart':('dart','dart run'),'julia':('julia','julia'),'r':('r','Rscript'),'lua':('lua','lua'),'bash':('bash','bash'),'powershell':('powershell','pwsh'),'sql':('sql','sqlite3'),'html':('html','browser'),'css':('css','browser'),'webassembly':('webassembly','wasmtime')}
root=Path(__file__).parent
for name,(label,runner) in LANGS.items():
    d=root/name; d.mkdir(parents=True,exist_ok=True)
    (d/'README.md').write_text(f'# SEO-Tool {label} adapter\n\nLanguage integration uses the stable JSONL boundary and delegates crawling to the local SEO-Tool engine.\n\nRunner: `{runner}`\n',encoding='utf-8')
print(f'generated {len(LANGS)} language tracks')
