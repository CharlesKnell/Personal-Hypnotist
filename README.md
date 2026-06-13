# Personal Hypnotist

Personal Hypnotist plays an MP3 audio file while displaying a fullscreen, animated black-and-white hypnotic spiral. 
When launched, a file picker lets you choose from the available MP3 files to play. I have found that watching this 
classic hypnotic spiral very helpful in trance induction.

I have included MP3 files, "Welcome-to-Hypnosis-by-Roger-Elliott" and "First-Time-Hypnosis-by-Roger-Elliott", 
from http://hypnosisdownloads. If you are new to hypnosis, Use the "Welcome..." file first. I'm not affiliated with 
"uncommon knowledge" in any way. There are over 1300 self hypnosis audio files available there.


## Windows Installation

https://drive.google.com/file/d/1LkLzdhL6W2WR2k3mjepLqPGSJf3Vjz3o/view?usp=drive_link

You will encounter warnings about this file because I'm not willing to purchase a certificate for an application 
which I'm giving away for free.


## Linux Installation

Install system dependencies:
```
sudo apt install python3-tk python3-numpy python3-venv
```

Copy `personal_hypnotist.pyw` to a project folder of your choice, then set up a virtual environment (venv) in that 
same folder:
```
python3 -m venv .venv      (creates a venv)
source .venv/bin/activate  (activates the venv)
pip install pygame
```

Place your MP3 files in `~/Documents/personal-hypnotist/`. If that folder does not exist, the app falls back to a 
`formulas/` folder in the same directory as `personal_hypnotist.pyw`.

Run from a terminal in the project folder:
```
.venv/bin/python3 personal_hypnotist.pyw
```


## Audio File Storage

Audio files (MP3) are stored in:

```
Documents\personal-hypnotist\
```

Add your own MP3 files to this folder and they will appear in the file picker at launch. When this folder exists, 
a Windows reinstallation of the Personal Hypnotist will not overwrite it.


## Runtime Controls

| Key                  | Action                                         |
|----------------------|------------------------------------------------|
| `LEFT` arrow         | Decrease spiral rotation speed                 |
| `RIGHT` arrow        | Increase spiral rotation speed                 |
| `SPACE`              | Pause / Unpause audio                          |
| `S`                  | Hide spiral (minimize to taskbar); audio plays |
| `windows` down arrow | minimize window                                |
| `ESC`                | Exit                                           |
