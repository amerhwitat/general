# Language adapter contract

AgentResearchForge uses a language-neutral JSONL protocol: one request object per line and one response object per line. Adapters may wrap the core service or implement the same request/response contract in the host language. Generated source is returned as text and is never executed by the adapter.

Supported tracks: Python, TypeScript, JavaScript, C, C++, C#, Java, Kotlin, Go, Rust, Swift, Objective-C, PHP, Ruby, Dart, Julia, R, Lua, Bash, PowerShell, SQL, HTML/CSS and WebAssembly.
