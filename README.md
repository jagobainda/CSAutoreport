
# CSAutoreport

A simple script to automate mass reporting in Counter-Strike 2 using a bug in the reporting menu. I have sent it to the development team; maybe they will fix it at some point.


## Requirements

* To run this script, you need to have Python installed and Pip to install the libraries. It should work well with any relatively recent version of Python.

* You need to run these commands to install the necessary libraries:

```bash
  pip install colorama
```

```bash
  pip install pyautogui
```

```bash
  pip install keyboard
```

## How to Exploit the Bug

* The bug consists of the report button on the players' card in the in-game scoreboard allowing multiple clicks, which can be used to automate mass reports. 

* The report button I mentioned allows multiple clicks, opening a report window for each click without any limit as far as I have tested. 

* My script is quite simple, but something more complex in the wrong hands could ruin the gaming experience for legitimate players, who could end up receiving unfair bans for disruptive behavior or seeing their trust factor decrease.