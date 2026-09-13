# Python GUI Standard

Account-wide standard for Python applications maintained under `amerhwitat`.

- Executable Python applications are GUI-first.
- Existing business logic and importable libraries remain reusable and headless-safe.
- CLI/headless operation remains available where useful for automation and CI.
- Long-running work runs off the GUI event thread.
- GUIs expose inputs, progress, logs, errors, results, import/export, and settings where applicable.
- Native file/folder pickers are preferred.
- Tkinter is the default lightweight desktop choice; richer applications may retain their established GUI framework.
- Every independently runnable Python application has a local `requirements.txt`.
- Tests and CI remain headless where practical.
- Security-sensitive tools keep their existing authorization and safety boundaries.

Do not inject UI code into pure domain modules. Put the GUI at the application boundary and keep the core API testable.
