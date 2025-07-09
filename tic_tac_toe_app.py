import streamlit as st

# Initialize session state
if "board" not in st.session_state:
    st.session_state.board = [["" for _ in range(3)] for _ in range(3)]
    st.session_state.current = "X"
    st.session_state.winner = None

st.title("🎮 Tic Tac Toe (Web Version)")

def check_winner(board, symbol):
    for i in range(3):
        if all(cell == symbol for cell in board[i]) or all(row[i] == symbol for row in board):
            return True
    if all(board[i][i] == symbol for i in range(3)) or all(board[i][2 - i] == symbol for i in range(3)):
        return True
    return False

def reset_game():
    st.session_state.board = [["" for _ in range(3)] for _ in range(3)]
    st.session_state.current = "X"
    st.session_state.winner = None

# Display the board
for i in range(3):
    cols = st.columns(3)
    for j in range(3):
        with cols[j]:
            if st.button(st.session_state.board[i][j] or " ", key=f"{i}-{j}"):
                if not st.session_state.board[i][j] and not st.session_state.winner:
                    st.session_state.board[i][j] = st.session_state.current
                    if check_winner(st.session_state.board, st.session_state.current):
                        st.session_state.winner = st.session_state.current
                    else:
                        st.session_state.current = "O" if st.session_state.current == "X" else "X"

# Show current status
if st.session_state.winner:
    st.success(f"Player {st.session_state.winner} wins!")
elif all(all(cell for cell in row) for row in st.session_state.board):
    st.warning("It's a draw!")
else:
    st.info(f"Current Turn: Player {st.session_state.current}")

# Reset Button
if st.button("Reset Game"):
    reset_game()