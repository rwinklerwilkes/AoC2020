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
            # print(round)
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

class BoardTwo(Board):
    def __init__(self, raw_input):
        super().__init__(raw_input)
        self.set_surrounding()

    def set_surrounding(self):
        self.surrounding = {}
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] in ('#','L'):
                    self.surrounding[(row,col)] = self.get_surrounding(row,col)

    def run_game(self):
        num_updated = 1
        round = 0
        while num_updated > 0:
            # print(round)
            num_updated = self.run_round()
            round += 1
        print('Number occupied:', np.sum(self.board=='#'))

    def run_round(self):
        occupy = []
        empty = []
        for i, row in enumerate(self.board):
            for j, seat in enumerate(row):
                if seat not in ('L','#'):
                    continue
                number_occupied = self.get_surrounding_cached(i,j)
                if seat == 'L' and number_occupied == 0:
                    occupy.append((i,j))
                if seat == '#' and number_occupied >= 5:
                    empty.append((i,j))
        number_to_update = len(occupy) + len(empty)
        self.update_board(occupy, empty)
        return number_to_update

    def get_surrounding_cached(self, row, col):
        surrounding_cells = self.surrounding[(row,col)]
        occupied = []
        for row, col in surrounding_cells:
            if self.board[row][col] == '#':
                occupied.append(1)
        number_occupied = len(occupied)
        return number_occupied

    def get_surrounding(self, row, col):
        surround = []
        cardinal = [(-1, -1), (-1, 0), (-1, 1),
                    (0, 1), (1, 1), (1, 0),
                    (1, -1), (0, -1)]
        for row_dir, col_dir in cardinal:
            i = row
            j = col
            on_board = True
            while on_board:
                i += row_dir
                j += col_dir
                if i < 0 or i >= len(self.board):
                    on_board = False
                elif j < 0 or j >= len(self.board[i]):
                    on_board = False
                elif self.board[i][j] in ('L','#'):
                    surround.append((i,j))
                    on_board = False
        return surround

# b = Board(test_data)
b = BoardTwo(input_data)
b.run_game()