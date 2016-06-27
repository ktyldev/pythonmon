# pythonmon

Pythonmon is an attempt at replicating the game engine of the [3rd generation Pokemon games](http://pokemon.wikia.com/wiki/Generation_III) and to provide a data-based interface to allow map building and scripting game object behaviours without have to edit the source code.

* [Python 3.5.1](https://www.python.org/downloads/)
* [Pygame for Python 3.5](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame)
* [Guide for installing pygame](https://skellykiernan.wordpress.com/2015/01/04/python-pygame-install/)

Tools must be developed to be able to use the engine, as the data-driven aspect of this engine relies mostly on piles of JSON files.

* [Tile map maker (currently only available as a Windows Form)](https://github.com/monodokimes/pythonmontilemapmaker)
* Scene Builder (work not started)
* Map Builder (work not started)

## Configuration

Various pieces of configuration can be found in `_config.cfg`. It is not recommended to edit this unless using the engine for a different game.

## Current goals

* write a tool to build scene data
* remove binaries from git
* a bunch of other stuff probably
* optimise map data file layout (it's horrendously ineffecient)

## Contributors

* [Cat Flynn](https://github.com/monodokimes)
