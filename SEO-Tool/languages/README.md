# Language adapters

SEO-Tool exposes a stable JSONL boundary so applications can embed the crawler from many programming languages. `generate_adapters.py` creates the adapter track directories for Python, JavaScript, TypeScript, C, C++, C#, Java, Kotlin, Go, Rust, Swift, Objective-C, PHP, Ruby, Dart, Julia, R, Lua, Bash, PowerShell, SQL, HTML/CSS and WebAssembly.

The canonical implementation remains in `SEO_Tool/`. Language adapters are integration surfaces rather than duplicated crawler engines, which keeps audit behavior consistent across languages.
