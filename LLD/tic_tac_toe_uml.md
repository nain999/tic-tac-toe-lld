# Low-Level Design for Tic Tac Toe

## Classes

### Player
- name: str
- symbol: str

### Board
- grid: 2D list
- methods: place_move(), check_winner(), is_valid_move()

### Game
- Controls game loop
- Manages players