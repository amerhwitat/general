# Python GUI Migration Manifest

## Verified changes in this pass

- `amerhwitat/BizX` — GUI-first Python package entry, native Tkinter GUI, requirements declarations for Python applications, authorized InternetScanner GUI, documentation updates.
- `amerhwitat/BizXtreme` — GUI-first Python package entry, native Tkinter GUI, requirements declarations, documentation updates.
- `amerhwitat/PDFreaderPY` — native PDF desktop GUI for file selection/page navigation/preview; root requirements declaration.
- `amerhwitat/nlp` — native Thamudic/Ancient North Arabian Tkinter GUI; Python requirements declaration.
- `amerhwitat/eth-key-check` — normalized Python requirements declaration; existing crypto GUI applications retained.
- `amerhwitat/bruteforce` — Python requirements declaration; existing research GUI retained. No new unrestricted attack capability was added.

## Boundary rule

Pure Python libraries are not converted by injecting UI code into every module. GUI behavior belongs at application boundaries so the underlying APIs remain importable, testable and usable by CI/headless services.

Repositories without a verified Python application entry point are intentionally not modified blindly. They remain in the account-wide audit queue until their complete tree can be classified.
