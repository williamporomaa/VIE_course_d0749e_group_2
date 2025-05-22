# VIE_course_d0749e_group_2
Group 2 project repository for VIE course. The project is a simplistic 2d game engine that reads of a json structure, and an accompanying tool. 
Documentation can be found in the repository, in the readme and further in the documentation folder (WIP).

# Installation
To install, simply clone the repository, and while in the repository directory (VIE_course_d0749e_group_2), and run the exectuable "Main_Widget.exe" in dist/Main_widget.

To test run a demo game, click the play button and then locate the "chessgame.json" file either within the chessGame folder or in "dist/Main_Widget/_internal/chessGame/chessgame.json".

To add own images to the game, firstly add them to the image folder located at "dist/Main_Widget/_internal/chessGame/images" and then press the "add" button to add an image to the scene.

A json can be saved anywhere, but keep in mind that the game can only correctly run a game if the images for the game are located in the correct directory.

# If it doesnt work for some reason:
- Requirements:
  - Python version 3.13.3 or later
  - PIP version 25.0.1 or later

OBS:
If not running windows, an executable file should also be achievable by running the pyinstaller command, which requires you to have a python installation with pyinstaller installed:

```
pip install pyinstaller
pyinstaller --add-data "chessGame/;chessGame" .\tool_ui\Main_Widget.py
```
Note that pyinstaller can be run in other folders but the "--add-data" property needs to be kept to properly display images.

If the user wishes to run with python directly instead of through an executable the following packages are required:
```
pip install pyside6
pip install pygame
pip install --editable .
```
and then run "Main_widget.py" in tool_ui **from the VIE_course_d7049e_group_2 folder!**

To run the engine, run the python file "Main_widget.py" and the tool will start, a premade game of chess can be loaded from within the tool and run from within the tool. Alternatively a game handler object could be created from any class and it should also function as a game engine.
