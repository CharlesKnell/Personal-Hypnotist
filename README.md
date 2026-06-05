# Personal Hypnotist

Personal Hypnotist plays an MP3 audio file while displaying a fullscreen, animated black-and-white hypnotic spiral. 
When launched, a file picker lets you choose from the available MP3 files to play.

## Formulas

Audio files (MP3) are stored in:

```
Documents\personal-hypnotist\
```

Add your own MP3 files to this folder and they will appear in the file picker at launch.

## Runtime Controls

| Key                  | Action                                         |
|----------------------|------------------------------------------------|
| `LEFT` arrow         | Decrease rotation speed                        |
| `RIGHT` arrow        | Increase rotation speed                        |
| `SPACE`              | Pause / Unpause audio                          |
| `S`                  | Hide spiral (minimize to taskbar); audio plays |
| `windows` down arrow | minimize window                                |
| `ESC`                | Exit                                           |

## Linux

Install tkinter and numpy before running:
```
sudo apt install python3-tk
sudo apt install python3-numpy
```
