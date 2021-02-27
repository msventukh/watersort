## Water sort puzzle
It's a simple game inspired by this [game](https://play.google.com/store/apps/details?id=com.gma.water.sort.puzzle)
for Android platform. The main goal of the game is to sort squares by colors so that every color would be present in
exactly one row.

### How to play
Every row (aka container) has the same number of "layers" (i.e., slots for blocks). You can move one block at a time.
Blocks can be moved either to an empty container or to a container that has free layers, and the most right block in the
container has the same color as the block you move. You can move only the right blocks. 

1. First, choose the container that you want to take a block from (by entering its number).
2. Then, choose the container that you want to but the block to (by entering its number).
3. If the move is possible, the state will change and you can proceed to the next move.

## How to run
The game requires Python 3.x (written and test on 3.9.1)

* `python main.py` runs the game with default settings
* `python main.py -h` shows help and possible options
* `python main.py -c <number>` runs the game with selected number of colors
* `python main.py -l <number>` runs the game with selected number of layers
Options `-c` and `-l` can be used together.
  
Enjoy!