# Cpong
cpong is a clone of the classic pong game with a twist that you're trying to get the highest volley count you can 
playing with both hands instead of against another player.

## Getting Started
---
Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.
```
python3 -m pip install raylib
```
After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.```

python3 cpong 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the 
project folder. Select the main module inside the hunter folder and click the "run" icon.
```
Use the 'e' and 'd' keys to move the left racket up and down and use the 'i' and 'k' keys to move the right racket up and down
Add a volley with each 'touch' of the racket. (With the animation, sometimes more than one!)
```

## Project Structure
---
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- cpong               (source code for game)
  +-- game              (specific game classes)
    +-- casting         (various actor classes)
    +-- directing       (director and scene manager classes)
    +-- scripting       (various action classes)
    +-- services        (various service classes)
  +-- __main__.py       (entry point for program)
  +-- constants.py      (game constants)
+-- README.md           (general info)
```

## Required Technologies
---
* Python 3.8.0
* Raylib Python CFFI 3.7

## Authors
---
* Matt Manley (manleym@byui.edu)