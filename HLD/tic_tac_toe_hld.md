# High-Level Design for Tic Tac Toe

## Functional Requirements
- Allow two players to play the game on 3x3 board
- Players take turn placing X or O in the specific spot on the board
- Game end:
  - When a specific player wins the game by placing X or O, three in a row
  - The board is full(draw match)
- Player should be given a option to reset the game.

## Non-functional Requirements
- Simple terminal or web interface
- Lightweight and fast
- Clean and modular code

## Main Components
- Game
- Board
- Player
- UI Layer

## Component Interaction Flow
- Game controls turn-based flow. 
- Board manages grid. 
- Players make moves.

## Data Flow
- Input : Player enters move by choosing row and column
- Game : Validates the move
- Board : Updates grid and checks winner 
- Game : Switches turn or ends the game
- Output : Show updated board, messages