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
only at the moment. It is compatible with `MS Windows` platform only. You need to 
have a proper browser driver. You can download it from.:

<https://chromedriver.chromium.org/downloads>

Pay attention that downloaded driver needs to be in the same version of your 
browser. You can check your current browser version here chrome://settings/help.

Install python requirements

```pip install requirements.txt```

Note! PyAudio needs `Microsoft Visual C++ Build Tools` to compile. You can install 
this from here 

<https://visualstudio.microsoft.com/pl/downloads/?rr=https%3A%2F%2Fwww.google.com%2F>

or get a already compiled python wheel from here 

<https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio>

Note! PyAudio requires to be installed with python interpreter on host. Virtualenv 
installation fails.


## Run

Run Chrome browser in debug mode

```chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\AutomationProfile"```

In project directory run application

```python run.py```

Application will connect automatically with Chrome process.

Login to your genealogy sources portal (fs support at the moment) and start 
working wit it.

`Genei` is a console app. To keep console window pinned on top of other windows 
use `AutoHotkey`. You can get it from here

<https://www.autohotkey.com>

After installation run `scripts\window-on-top.ahk`. Open console window and press
`Ctrl + space`. Window will be pinned on top. To unpin press `Ctrl + space` again.
