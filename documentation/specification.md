# Basic Specification
The project will be done in Python, and all documentation will be written in English.

I can review projects written in Python.

My study programme is tietojenkäsittelytieteen kandidaatti (TKT).

# Problem and Algorithm
Project is going to be about solving the 15-puzzle using IDA* algorithm.

15 puzzle is made of 4x4 square which is filled with 15 numbered tiles from 1-15.
Tiles can be moved vertically and horizontally to empty squares and the object is to place the numbered tiles in numerical order from smallest to biggest.

Program will try to find the smallest amount of moves for the given solvable game that will reach the goal.
The puzzle will be represented as a list of lists where each row is its own list using 16 integers, where 0 represents the empty square.
The program will receive a puzzle as input and return a sequence of moves that solves it using the minimum number of moves.

I will use the IDA* algorithm to solve the puzzle which is an algorithm that combines depth-first search with a heuristic function.
For heuristics I will use Manhattan distance and a combination of Manhattan distance and Linear Conflict.
I will be comparing the number of explored search nodes and execution time for these.

Time complexity is O(n^2) and space complexity is O(n).


# Sources
The following will be used as sources:
 - [Iterative deepening A* (Wikipedia)](https://en.wikipedia.org/wiki/Iterative_deepening_A*)
 - [Richard E. Korf and Larry A. Taylor, "Finding Optimal Solutions to the Twenty-Four Puzzle" from AAAI-96 Proceedings](https://cdn.aaai.org/AAAI/1996/AAAI96-178.pdf)
