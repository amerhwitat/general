# Amer Hwitat — General / Integration Repository

This repository is a general integration and research workspace within the Amer Hwitat GitHub portfolio. It complements the canonical `ChimeraIIOS` repository and provides shared experiments, host-side integration material and compatibility boundaries.

## Repository-wide source citation index

Every maintained application is cited from this README by its canonical source tree, and flagship components have exact source-file links. These links are the source-of-record navigation points for the code tracked here.

- [AgentResearchForge](AgentResearchForge/)
- [SEO-Tool](SEO-Tool/)
- [WebContactCrawler](applications/WebContactCrawler/)
- [Email Extractor](email_extractor/)
- [WorkflowStudio](WorkflowStudio/)
- [Apple-Implementations](Apple-Implementations/)
- [mobile](mobile/)
- [kotlin](kotlin/)
- [apple](apple/)
- [web](web/)
- [docs](docs/)
- [third_party](third_party/)

### Exact flagship source files

- [Email Extractor Python core](email_extractor/core_py/extractor.py)
- [Email Extractor Python SQLite/CSV storage](email_extractor/utils/storage.py)
- [Email Extractor SQLite/CSV/JSON persistence](email_extractor/core_py/persistence.py)
- [Email Extractor Visual Studio solution](email_extractor/EmailExtractor.sln)
- [Email Extractor PyQt UI](email_extractor/ui_pyqt/main.py)
- [Email Extractor C# core](email_extractor/core_csharp/Extractor.cs)
- [Email Extractor C# storage](email_extractor/core_csharp/Storage.cs)
- [Email Extractor C# project](email_extractor/core_csharp/EmailExtractor.CSharp.csproj)
- [Email Extractor native C/C++/ASM CMake](email_extractor/native/CMakeLists.txt)
- [Email Extractor Code::Blocks project](email_extractor/native/CodeBlocks.EmailExtractor.cbp)
- [Email Extractor Node.js core](email_extractor/core_js/extractor.js)
- [Email Extractor Node.js storage](email_extractor/core_js/storage.js)
- [Email Extractor Electron integration](email_extractor/electron/main.js)
- [Email Extractor Java core](email_extractor/core_java/Extractor.java)
- [Email Extractor Java storage](email_extractor/core_java/Storage.java)
- [Email Extractor Maven project](email_extractor/core_java/pom.xml)
- [Email Extractor PHP core](email_extractor/core_php/extractor.php)
- [Email Extractor PHP storage](email_extractor/core_php/storage.php)
- [Email Extractor Rust core](email_extractor/core_rust/extractor.rs)
- [Email Extractor Rust storage](email_extractor/core_rust/storage.rs)
- [Email Extractor Cargo project](email_extractor/core_rust/Cargo.toml)
- [Email Extractor Rust TUI](email_extractor/ui_rust/src/main.rs)
- [SEO crawler](SEO-Tool/SEO_Tool/core.py)
- [SEO CLI](SEO-Tool/SEO_Tool/cli.py)
- [SEO GUI](SEO-Tool/SEO_Tool/gui.py)
- [SEO research](SEO-Tool/SEO_Tool/research.py)
- [SEO document extraction](SEO-Tool/SEO_Tool/documents.py)
- [SEO language manifest](SEO-Tool/languages/manifest.json)
- [WebContactCrawler engine](applications/WebContactCrawler/python/webcontactcrawler.py)
- [WebContactCrawler import/export](applications/WebContactCrawler/python/import_export.py)
- [WebContactCrawler schema](applications/WebContactCrawler/schema/contact.schema.json)
- [WorkflowStudio Python entry](WorkflowStudio/services/python/main.py)
- [WorkflowStudio RNN/LLM](WorkflowStudio/services/python/rnn_llm_engine.py)
- [WorkflowStudio C++ core](WorkflowStudio/core/cpp/main.cpp)
- [WorkflowStudio web client](WorkflowStudio/clients/web/src/App.tsx)
- [WorkflowStudio Android client](WorkflowStudio/clients/android/Main.kt)
- [WorkflowStudio iOS client](WorkflowStudio/clients/ios/WorkflowClient.swift)
- [Mobile C++ runtime](mobile/src/runtime.cpp)
- [Mobile package fabric](mobile/src/package_fabric.cpp)
- [Chimera 3D/4D geometry](Apple-Implementations/Chimera3D4D/core/src/geometry.cpp)
- [Chimera 3D/4D scene](Apple-Implementations/Chimera3D4D/core/src/scene.cpp)
- [Chimera 3D/4D RNN/LLM](Apple-Implementations/Chimera3D4D/ai/rnn_llm_engine.py)

## Email Extractor

`email_extractor/` is the cross-language public/authorized-web contact discovery application. It includes extraction, title/provenance handling and DNS/MX validation cores for Python, C#, Node.js, Java, PHP and Rust, native C/C++/ASM build scaffolding, and desktop/web interfaces. SQLite persistence and CSV export are standardized across the language cores. IDE/build metadata is included for Visual Studio, Code::Blocks, CMake, PyCharm/IntelliJ, VS Code, Eclipse, Maven, Cargo, Node/Electron and PHP workflows.

## AgentResearchForge

`AgentResearchForge/` provides local-first AI research, bounded public-web retrieval, local document retrieval, public code/API research, authorized onion retrieval, evidence synthesis, project generation, artifacts and document export.

## SEO-Tool

`SEO-Tool/` provides bounded HTTP/HTTPS technical SEO auditing, metadata/structured-data analysis, reports, GUI/CLI operation, document capture and an explicitly configured authorized `.onion` research boundary.

## AI architecture layer

The portfolio uses local-first RNN/LLM patterns with bounded state, explicit memory, retrieval/vector boundaries, provenance/confidence and human/policy approval before consequential mutations.

## WebContactCrawler

`applications/WebContactCrawler/` provides bounded public-web contact discovery, keyword-focused crawling, robots-aware scheduling, public email extraction, provenance, deduplication, progress telemetry and import/export.

## WorkflowStudio

`WorkflowStudio/` is the cross-platform project/service-management foundation with a local-first RNN/LLM assistant.

## Central Apple implementations

`Apple-Implementations/` contains the portfolio's Objective-C/Xcode and Flutter iOS/macOS implementation boundaries.

## Chimera 3D/4D and 128D

`Apple-Implementations/Chimera3D4D/` provides the 3D/4D application foundation. Portfolio applications can use the 128D semantic model spanning geometry, time, observer/perspective, light/material response, events, objects, properties and interaction rules, with extensible perception/cognition dimensions.

## Portfolio relationships

- `ChimeraIIOS` — canonical OS/interoperability repository.
- `CPU4096` / `CPU4096Simulator` — processor/simulation research.
- `nlp` / `PDFreaderPY` — language/document research.
- `BizX` / `BizXtreme` — application/game tracks.

## Licensing

Original project code is released under GNU GPL v3 or later. Third-party code and assets retain applicable licenses.
