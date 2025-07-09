from board import Board
from player import Player

class Game:
    def __init__(self):
        self.board = Board()
        self.players = [Player("Player 1", "X"), Player("Player 2", "O")]
        self.current_player_index = 0

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index

    def play(self):
        print("Welcome to Tic Tac Toe!")
        self.board.print_board()

        while True:
            player = self.players[self.current_player_index]
            print(f"{player.name}'s turn ({player.symbol}):")

            try:
                row = int(input("Enter row (0-2): "))
                col = int(input("Enter column (0-2): "))
            except ValueError:
                print("Invalid input. Try again.")
                continue

            if not self.board.is_valid_move(row, col):
                print("Invalid move. Cell already taken or out of range.")
                continue

            self.board.place_move(row, col, player.symbol)
            self.board.print_board()

            if self.board.check_winner(player.symbol):
                print(f"{player.name} wins!")
                break

            if self.board.is_full():
                print("It's a draw!")
                break

            self.switch_player()