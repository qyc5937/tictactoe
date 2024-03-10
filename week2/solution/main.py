def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)


def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return True

    # Check columns
    for col in range(len(board[0])):
        if all(board[row][col] == board[0][col] and board[col][0] != ' ' for row in range(len(board))):
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return True

    return False


def test_check_winner():
    # Test rows
    assert check_winner([['X', 'X', 'X'], [' ', ' ', ' '], [' ', ' ', ' ']]) == True
    assert check_winner([['O', 'O', 'O'], [' ', ' ', ' '], [' ', ' ', ' ']]) == True

    # Test columns
    assert check_winner([['X', ' ', ' '], ['X', ' ', ' '], ['X', ' ', ' ']]) == True
    assert check_winner([['O', ' ', ' '], ['O', ' ', ' '], ['O', ' ', ' ']]) == True

    # Test diagonals
    assert check_winner([['X', ' ', ' '], [' ', 'X', ' '], [' ', ' ', 'X']]) == True
    assert check_winner([['O', ' ', ' '], [' ', 'O', ' '], [' ', ' ', 'O']]) == True

    assert check_winner([['X', ' ', 'O'], [' ', 'O', ' '], ['O', ' ', 'X']]) == True
    assert check_winner([['X', 'O', 'X'], [' ', 'X', ' '], ['O', ' ', 'X']]) == True

    # Test no winner
    assert check_winner([['X', 'O', 'X'], ['O', 'X', 'O'], ['O', 'X', 'O']]) == False
    assert check_winner([['X', 'O', 'X'], ['X', 'X', 'O'], ['O', 'X', 'O']]) == False
    assert check_winner([['X', 'O', 'X'], ['X', 'O', 'O'], ['O', 'X', 'X']]) == False
    assert check_winner([['X', 'O', 'X'], ['O', 'X', 'O'], ['O', 'X', 'O']]) == False

    print("All test cases passed!")


def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'
    while True:
        print_board(board)
        row = int(input(f"Player {player}, choose row (1-3): ")) - 1
        col = int(input(f"Player {player}, choose column (1-3): ")) - 1

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
    test_check_winner()
    tic_tac_toe()
