# Low-Level Design for Tic Tac Toe

## Classes

### Player - Stores player-specific data
- name: str
- symbol: str

### Board - Manages board state and validation and contains logic for win/draw conditions
- grid: List[List[str]] # 3x3 grid
- methods: print_board(), is_valid_move(row, col), place_move(row, col, symbol), check_winner(symbol), is_full()

### Game - Handles game loop, Controls game loop, Manages players
- board : Board()
- players : List[Player]
- current_player_index: int
- methods : switch_player(), play()

# Game Sequence
Player clicks -> Game.play()
    -> Board.is_valid_move()
    -> Board.place_move()
    -> Board.check_winner()
Game.switch_player()