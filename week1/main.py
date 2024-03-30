'''
This is a simple console based tic-tac-toe game.  To run the game run

python main.py


week 1 code was generated using chatgpt using the chat sequence below
https://chat.openai.com/share/ae6d5f14-9218-426f-bbd7-9a24b8c34945
'''

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


# complete the logic to find the winner
def check_winner(board):
    X_rows=[0,0,0]
    X_cols=[0,0,0]
    O_rows=[0,0,0]
    O_cols=[0,0,0]
    for r in range (3):
        for c in range (3):
            if board[r][c]=='X':
                X_rows[r] = X_rows[r] + 1
                X_cols[c] = X_cols[c] + 1
            elif board[r][c]=='O':
                O_rows[r] = O_rows[r] + 1
                O_cols[c] = O_cols[c] + 1
    if (3 in X_rows) or (3 in X_cols) or (3 in O_rows) or (3 in O_cols):
        return True 
    else:
        return False


# TODO:  Demonstrate in meeting how to make sense of this function in chatgpt.
def get_move(player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): "))
            if 1 <= move <= 9:
                return move
            else:
                print("Invalid move! Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input! Please enter a number.")


def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'
    while True:
        print_board(board)
        move = get_move(player)
        row = (move - 1) // 3
        col = (move - 1) % 3

        if board[row][col] == ' ':
            board[row][col] = player
            if check_winner(board):
                print_board(board)
                print(f"Player {player} wins!")
                break
            if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
                print_board(board)
                print("It's a tie!")
                break
            player = 'O' if player == 'X' else 'X'
        else:
            print("That spot is already taken!")


if __name__ == "__main__":
    tic_tac_toe()
