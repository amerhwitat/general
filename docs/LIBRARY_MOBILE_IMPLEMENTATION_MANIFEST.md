# Library → Chimera II Mobile implementation manifest

The mobile extension was cross-checked against the saved project corpus. The following sources are explicitly represented:

- `Chimera II OS Developer Guide.txt` — HAL, Chronos, memory/security fabrics, Aurora and CHIMERA HAL.
- `Chimera_II_OS_Comprehensive_Redesign_Research_Report.pdf` — 4096/8192/N-bit scaling, Koronos, VFS, Aurora, security and emulation.
- `Chimera_II_OS_8192_High_Low_Level_Technical_Specification.pdf` — R8192/C8192, 1024 GPRs, 128×64-bit lanes, vector/tensor registers.
- `8192-ChimeraII-OS-Summary(1).docx` and `8192-ChimeraII-OS-Summary.docx` — earlier wide-register and networking code.
- `CPU4096-ARM-and_X86.docx` — ARM64/x86 compatibility.
- `Chimera II OS - crash dump.docx` — diagnostics and failure context.
- `Complete_Research_and_Project_Knowledge_Archive.pdf` — consolidated research history.
- `Chimera II Web Runtime & Desktop Integration` — Aurora/Web Runtime and sandbox model.
- `Integrating Linux 7.x, Retro Emulation, and Future Computing into Chimera II Web OS` — Linux/retro integration.
- `AmigaGuruBook[ENG]FullSearch(1).txt` — Amiga/retro compatibility reference.
- `Aurora Wayland Glass Desktop.png` — canonical Aurora visual reference.
- `Chimera II OS Aurora Showcase.png` — N-bit/Aurora feature reference.
- `Chimera II Multidimensional Computing Architecture.png` — multidimensional/128D reference.

Implementation rule: research documents and historical code archives are not blindly copied into the mobile runtime. Their relevant interfaces, policies and compatibility boundaries are implemented or recorded as provenance. This keeps licensing, size, maintainability and security boundaries explicit.
