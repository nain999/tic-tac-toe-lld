class Board:
    def __init__(self, size: int = 3):
        self.size = size
        self.grid = [[" " for _ in range(size)] for _ in range(size)]

    def print_board(self):
        for row in self.grid:
            print("|".join(row))
            print("-" * (2 * self.size - 1))

    def is_valid_move(self, row, col):
        return 0 <= row < self.size and 0 <= col < self.size and self.grid[row][col] == " "

    def place_move(self, row, col, symbol):
        self.grid[row][col] = symbol

    def check_winner(self, symbol):
        for i in range(self.size):
            if all(self.grid[i][j] == symbol for j in range(self.size)) or \
               all(self.grid[j][i] == symbol for j in range(self.size)):
                return True
        if all(self.grid[i][i] == symbol for i in range(self.size)) or \
           all(self.grid[i][self.size - i - 1] == symbol for i in range(self.size)):
            return True
        return False

    def is_full(self):
        return all(self.grid[i][j] != " " for i in range(self.size) for j in range(self.size))
