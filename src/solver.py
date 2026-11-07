class IDAStar:
    """Class for solving the puzzle with IDA* algorithm

    Attributes:
        heuristic: The function used to estimate remaining moves
    """

    def __init__(self, heuristic):
        """Constructor for the solver

        Args:
            heuristic: A function that takes a puzzle and returns its estimate
        """
        self.heuristic = heuristic

    def solve(self, puzzle):
        """Start the search using the heuristic value as the first limit

        Args:
            puzzle: The puzzle to solve

        Returns:
            The moves for the correct solution or None if no solution is found
        """
        limit = self.heuristic(puzzle)
        moves = []

        while True:
            result = self._search(puzzle, 0, limit, moves)
            if result == "solved":
                return moves
            if result == float("inf"):
                return None
            limit = result

    def _search(self, puzzle, depth, limit, moves):
        """Check the search limit and goal before exploring moves
        """
        cost = depth + self.heuristic(puzzle)
        if cost > limit:
            return cost
        if puzzle.is_solved():
            return "solved"
