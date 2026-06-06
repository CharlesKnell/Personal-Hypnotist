# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this project is

Personal Hypnotist is a single-file Windows desktop app (`personal_hypnotist.pyw`) that plays an MP3 audio file (selected by the user at launch) while displaying a fullscreen, animated black-and-white hypnotic spiral. The `.pyw` extension suppresses the Windows console window.

## Running the app

```
# From the project root (Windows)
.venv\Scripts\activate
python personal_hypnotist.pyw
```

## Building the Windows executable

```
cd C:\Users\charl\OneDrive\Desktop\PYTHON\personal_hypnotist
.venv\Scripts\activate
pyinstaller --onefile --add-data=formulas:formulas --name PersonalHypnotist --version-file version_info.txt personal_hypnotist.pyw
```

Output lands in `dist/PersonalHypnotist.exe`. The `formulas/` folder is bundled so the file picker opens there by default.

After building, compile the Inno Setup installer from `Inno-Install/Setup.iss` using the Inno Setup compiler (GUI or `iscc`).

## Dependencies

`pygame`, `numpy` — installed in `.venv`.

## Architecture

The entire app is `main()` in `personal_hypnotist.pyw`. There are no modules, classes, or other files involved at runtime.

**Spiral rendering** uses precomputed polar coordinate arrays (`r`, `theta` via `np.meshgrid`) that are computed once at startup for the full screen resolution. Each frame only updates a single scalar (`rotation`) and recomputes `spiral_val = (base + rot_norm) % 1.0`, then writes black/white directly into the pygame surface via `pygame.surfarray.pixels3d`. The `.T` transpose on the mask reconciles numpy's (row, col) = (y, x) ordering with pygame surfarray's (x, y) ordering.

The `exp = 0.38` exponent in `r_norm` controls band density: lower = narrower bands near the center, wider bands toward the edges.

**`resource_path()`** resolves asset paths both in development (relative to the script) and inside a PyInstaller `--onefile` bundle (via `sys._MEIPASS`).

## Version bumping

Two files must be updated together when releasing a new version:
- `version_info.txt` — `filevers`, `prodvers`, and `ProductVersion` fields
- `Inno-Install/Setup.iss` — `#define MyAppVersion` and `OutputBaseFilename`

## Formulas folder

The `formulas` folder in the project root holds MP3 audio tracks and optional `.txt` companion scripts. It has two roles:

- **PyInstaller bundle**: the formulas folder and content is embedded in the exe via `--add-data=formulas:formulas`. Used as the file-picker `initialdir` fallback when running in dev mode (i.e. `Documents\personal-hypnotist` does not exist).
- **Inno installer source**: the formulas content is copied verbatim to `Documents\personal-hypnotist\` on the user's machine during install (`onlyifdoesntexist` flag preserves any files the user has added or modified on reinstall).

At runtime, `get_documents_folder()` calls `SHGetFolderPathW` (Windows) or `~/Documents` (Linux) to locate the user's actual Documents folder — this handles OneDrive redirection. The app then prefers `Documents\personal-hypnotist` if it exists, otherwise falls back to the bundled copy via `resource_path("formulas")`.
