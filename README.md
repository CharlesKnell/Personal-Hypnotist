# Personal Hypnotist

Personal Hypnotist plays an MP3 audio file while displaying a fullscreen, animated black-and-white hypnotic spiral. 
When launched, a file picker lets you choose from the available MP3 files to play. I have found that watching this 
classic hypnotic spiral very helpful in trance induction.

I have included MP3 files, "Welcome-to-Hypnosis-by-Roger-Elliott" and "First-Time-Hypnosis-by-Roger-Elliott", 
from http://hypnosisdownloads. If you are new to hypnosis, Use the "Welcome..." file first. I'm not affiliated with 
"uncommon knowledge" in any way. There are over 1300 self hypnosis audio files available there.

## Windows Installation

https://drive.google.com/file/d/1LkLzdhL6W2WR2k3mjepLqPGSJf3Vjz3o/view?usp=drive_link

You will encounter warnings about this file because I'm not willing to purchase a security certificate for an 
application which I'm giving away for free.

## Linux Installation
```
sudo apt update
sudo apt install python3-venv
```
Install git and Personal Hypnotist files in the project directory. I'm using ~/Programs as the project directory.
Then, copy the contents of the formulas directory to the user directory.
```
sudo apt install git
git --version          (verify correct git install)
cd ~/Programs          (change to the project directory)
git clone https://github.com/CharlesKnell/Personal-Hypnotist.git      (download the application files)
mkdir ~/Documents/personal-hypnotist    (use if the directory doesn't already exist)
cp ~/Programs/Personal-Hypnotist/formulas/* ~/Documents/personal-hypnotist
```

Set up a virtual environment (venv) in ~/Programs/Personal-Hypnotist and install dependencies:
```
python3 -m venv .venv      (creates a venv)
source .venv/bin/activate  (activates the venv)
pip install pygame numpy
```

## Audio File Storage

The default and user audio files (MP3) are stored in:
```
Windows:
Documents\personal-hypnotist

Linux:
~/Documents/personal-hypnotist
```
Add your own MP3 files to this directory. They will appear in the file picker at launch. When this folder exists, 
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

## Invocation
Run from a terminal in the project folder:
```
.venv/bin/python3 personal_hypnotist.pyw
```