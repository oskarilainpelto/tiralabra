class Puzzleboard:
    """Class for the 15-puzzle board

    Attributes:
        board: The puzzle board
    """

    def __init__(self, board):
        """Constructor for the puzzle board
        """
        self.board = [row[:] for row in board]

    def is_solved(self):
        """Return True if puzzle is in solved state"""
        return self.board == [[1, 2, 3, 4],
                              [5, 6, 7, 8],
                              [9, 10, 11, 12],
                              [13, 14, 15, 0]]

    def move(self, direction):
        """Return a new board after moving the empty square

        Args:
            direction: The direction where the empty square moves to which are "up", "down", "left" or "right"

        Returns:
            A new board with the empty square and tile next to it swapped
        """
        directions = {"up": (-1, 0), "down": (1, 0),
                      "left": (0, -1), "right": (0, 1)}

        for row in range(4):
            for col in range(4):
                if self.board[row][col] == 0:
                    row_change, col_change = directions[direction]
                    new_row = row + row_change
                    new_col = col + col_change
                    new_board = Puzzleboard(self.board)
                    new_board.board[row][col] = new_board.board[new_row][new_col]
                    new_board.board[new_row][new_col] = 0
                    return new_board
