from aocd import get_data
import numpy as np

input_data = get_data(year=2020, day=11)

test_data = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""

class Board:
    def __init__(self, raw_input):
        self.setup_board(raw_input)

    def setup_board(self, raw_input):
        self.board = np.array([[c for c in row] for row in raw_input.split('\n')])

    def get_surrounding(self, row, col):
        surround = []
        for i in range(row-1,row+2):
            if i < 0 or i >= len(self.board):
                continue
            for j in range(col-1, col+2):
                if j < 0 or j >= len(self.board[i]):
                    continue
                if not (i==row and j==col):
                    surround.append(self.board[i][j])
        return surround

    def count_surrounding(self, surrounding):
        number_occupied = sum([1 for seat in surrounding if seat == '#'])
        return number_occupied

    def run_game(self):
        num_updated = 1
        round = 0
        while num_updated > 0:
            print(round)
            num_updated = self.run_round()
            round += 1
        print('Number occupied:', np.sum(self.board=='#'))

    def run_round(self):
        occupy = []
        empty = []
        for i, row in enumerate(self.board):
            for j, seat in enumerate(row):
                number_occupied = self.count_surrounding(self.get_surrounding(i,j))
                if seat == 'L' and number_occupied == 0:
                    occupy.append((i,j))
                if seat == '#' and number_occupied >= 4:
                    empty.append((i,j))
        number_to_update = len(occupy) + len(empty)
        self.update_board(occupy, empty)
        return number_to_update

    def update_board(self, occupy, empty):
        new_board = self.board.copy()
        for row, col in occupy:
            new_board[row][col] = '#'
        for row, col in empty:
            new_board[row][col] = 'L'
        self.board = new_board

b = Board(input_data)
b.run_game()