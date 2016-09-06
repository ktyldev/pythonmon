# pythonmon

Pythonmon is an attempt at replicating the game engine of the [3rd generation Pokemon games](http://pokemon.wikia.com/wiki/Generation_III) and to provide a data-based interface to allow map building and scripting game object behaviours without have to edit the source code.

* [Python 3.5.1](https://www.python.org/downloads/)
* [Pygame for Python 3.5](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame)
* [Guide for installing pygame](https://skellykiernan.wordpress.com/2015/01/04/python-pygame-install/)

## Configuration

Various pieces of configuration can be found in `_config.cfg`. It is not recommended to edit this unless using the engine for a different game.

## To Do

* **edit tiles in editor mode**
* **implement some sort of testing framework**
* logging levels
* rename modules to make more sense (suggestions very welcome)
* implement instruction set for building scenes
* remove binaries from repo
* optimise map data file layout (it's horrendously inefficient)

## In Progress

* game/editor loop
* player movement (implement running)

## Completed

* tile engine
* overworld graphics engine
* scene > entity > component object composition
* input
* collision

## Contributors

* [Cat Flynn](https://github.com/monodokimes)

## DISCLAIMER

I'm still very new to software design, source control and open-source projects in general. If there's anything I could be doing better *please, please* tell me and I will do my best to make sure that I take your advice on board!
