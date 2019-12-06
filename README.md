# genei

**genealogy indexing is not so boring stuff!**

## Introduction

Bored with nightly indexing of genealogical stuff? Swiching between window to put some value info about your ancestors? Inputing repeatable data in to your workbook?

How about inserting just crucial data? Clicking webpages, saving links to scan pages with voice command?

Let`s make it quicker!
Itroduce to you genei!


## Installation

Application uses selenium to interact with webbrowser. Chrome browser is supported only at the moment. You need to have a proper webbrowser driver. You can download it from https://chromedriver.chromium.org/downloads. Pay attention that downloaded driver need to be in the same version of your webbrowser. You can check your current version here chrome://settings/help.

## Run

Run Chrome browser in debug mode

```chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\AutomationProfile"```

In project directory run application

```python run.py```

Application will connect automatically with Chrome process.

Login to your genealogy sources portal (fs support at the moment) and start working wit it.