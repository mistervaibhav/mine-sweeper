import random


class Board:
    def __init__(self, dimensions, bombs) -> None:
        self.dimensions = dimensions
        self.bombs = bombs

        self.board = self.make_new_board()

        self.dug = set()

    def make_new_board(self):
        # * 2D board
        board = [[None for _ in range(self.dimensions)] for _ in range(self.dimensions)]

        bombs_planted = 0

        while bombs_planted < self.bombs:
            location = random.randint(0, self.dimensions ** 2 - 1)
            row = location // self.dimensions
            column = location % self.dimensions

            if board[row][column] == "*":
                continue

            board[row][column] == "*"


# ─── PLAY THE GAME ──────────────────────────────────────────────────────────────
def play(dimensions=10, bombs=10) -> None:
    """
    * step 1: create the board and plant the bombs
    * step 2: show the user the baord and ask for where they want to dig
    * step 3a: if the location is a bomb, show game over message
    * step 3b: if the location is not a bomb, dig recursively until each square
    *          is at least next to a bomb
    * step 5: repeat 2 and 3a/b until there are no more places to dig
    """

    pass
