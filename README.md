# Road Blocks

A turn-based, two-player game where the goal is to get to the other side
before your opponent.

## Source Code

* `Board`: A class that represents the game board.
   * `Board.Builder`: A Builder pattern that constructs boards.
* `PathFinder`: A class that finds the shortest path between two points,
   if any, respecting all walls.

## Running Tests

To run the tests we use `unittest` framework. All test files are named after the 
corresponding classes with `-test` suffix. For example `pf-test.py` are the tests
for the code in the `pf.py` file.

> Note: If the class is too involved, there may be other files named
> `<file>-test-<something>`, to better organize the tests.

To run from the command line, replacing `file-to-test.py` with the file to run the
tests:

    python -m unittest <file-to-test.py>

Example:

    $ python -m unittest pf_test.py
    ...........
    ----------------------------------------------------------------------
    Ran 11 tests in 0.020s
    
    OK