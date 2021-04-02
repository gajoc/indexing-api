# genei

**genealogy indexing is not so boring stuff!**

## Introduction

Bored with nightly indexing of genealogical stuff? Switching between windows to 
put some value info about your ancestors? Inputting repeatable data in to your 
workbook or editor?

How about inserting just crucial data? Clicking web pages, saving links to scan 
pages with voice commands?

Lets make it quicker!
Introduce to you `genei`!


## Installation

Application uses selenium to interact with web browser. `Chrome` browser is supported 
only at the moment. You need to have a proper browser driver. You can download it from.:

<https://chromedriver.chromium.org/downloads>

Pay attention that downloaded driver needs to be in the same version of your 
browser. You can check your current browser version here chrome://settings/help.
Extracted chrome driver copy to project\`s bin folder.

Note! PyAudio is required in host system. Here are some tips below how to set it up on 
Windows and linux.

<ins>Windows PyAudio</ins>

PyAudio in Windows needs `Microsoft Visual C++ Build Tools` to compile. You can install 
this from here 

<https://visualstudio.microsoft.com/pl/downloads/?rr=https%3A%2F%2Fwww.google.com%2F>

or get a already compiled python wheel from here 

<https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio>

Note! PyAudio requires to be installed with python interpreter on host. Virtualenv 
installation fails.

<ins>Linux pyaudio</ins>

Note! PyAudio for linux requires following packages to be installed.

```sudo apt-get install python3-dev portaudio19-dev python3-pyaudio```

For linux PyAudio python package name is ```pyaudio```. Change it first in `requirements.txt` 
file. In linux pyaudio works fine in venv.



Finally install python requirements

```pip install requirements.txt```


## Run

Run Chrome browser in debug mode:

windows

```chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\remote-chrome-profile"```

linux

```google-chrome --remote-debugging-port=9222 --user-data-dir=remote-chrome-profile```

In project directory run application

```python run.py [voice|keyboard]```

Mandatory argument ```voice|keyboard``` sets application control method.

Application will connect automatically with Chrome process.

Login to your genealogy sources portal (fs support at the moment) and start 
working with it.

`Genei` is a console app. To keep console window pinned on top of other windows 
use `AutoHotkey` for Windows OS. You can get it from here

<https://www.autohotkey.com>

After installation run `scripts\window-on-top.ahk`. Open console window and press
`Ctrl + space`. Window will be pinned on top. To unpin press `Ctrl + space` again.

In linux terminal window can be pinned on top of other windows by selectiong `Always on Top` option from terminal menu. 
