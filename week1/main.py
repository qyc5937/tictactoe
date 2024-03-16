'''
This is a simple console based tic-tac-toe game.  To run the game run

python main.py


week 1 code was generated using chatgpt using the chat sequence below
https://chat.openai.com/share/ae6d5f14-9218-426f-bbd7-9a24b8c34945
'''

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


# complete the logic to find the winner
def check_winner(board):
    if board[0][0] == 'X' and board[0][1] == 'X' and board[0][2] == 'X':
        return True
    if board[1][0] == 'X' and board[1][1] == 'X' and board[1][2] == 'X':
        return True
    if board[2][0] == 'X' and board[2][1] == 'X' and board[2][2] == 'X':
        return True
    if board[0][0] == 'X' and board[1][0] == 'X' and board[2][0] == 'X':
        return True
    if board[0][1] == 'X' and board[1][1] == 'X' and board[2][1] == 'X':
        return True
    if board[0][2] == 'X' and board[1][2] == 'X' and board[2][2] == 'X':
        return True
    if board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
        return True
    if board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
        return True
    
    if board[0][0] == 'O' and board[0][1] == 'O' and board[0][2] == 'O':
        return True
    if board[1][0] == 'O' and board[1][1] == 'O' and board[1][2] == 'O':
        return True
    if board[2][0] == 'O' and board[2][1] == 'O' and board[2][2] == 'O':
        return True
    if board[0][0] == 'O' and board[1][0] == 'O' and board[2][0] == 'O':
        return True
    if board[0][1] == 'O' and board[1][1] == 'O' and board[2][1] == 'O':
        return True
    if board[0][2] == 'O' and board[1][2] == 'O' and board[2][2] == 'O':
        return True
    if board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
        return True
    if board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O':
        return True
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
