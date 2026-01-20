import numpy as np 

class Board:
    def __init__(self):
        self.board = np.zeros((8, 8), dtype=int)

    def set_start(self):
        starting_position = [
            [4, 3, 2, 5, 6, 2, 3, 4],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [-1,-1,-1,-1,-1,-1,-1,-1],
            [-4,-3,-2,-5,-6,-2,-3,-4]
        ]
        self.board = np.array(starting_position)

    def print_board(self):
        print(self.board)


board = Board()
board.set_start()
board.print_board()