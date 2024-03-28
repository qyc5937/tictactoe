def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 8)


def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return True

    # Check columns
    for col in range(len(board[0])):
        if all(board[row][col] == board[0][col] and board[0][col] != ' ' for row in range(len(board))):
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return True

    return False



def test_check_winner():
    player = 'X'
    err=0
    # case 1, rows
    for r in range(3):
        board = [[' ' for _ in range(3)] for _ in range(3)]
        board[r][0]=player
        board[r][1]=player
        board[r][2]=player
        if check_winner(board)==False:
            print('Error: winner not detected')
            print_board(board)
            err = 1
        
    # case 2, cols  
    for r in range(3):
        board = [[' ' for _ in range(3)] for _ in range(3)]
        board[0][r]=player
        board[1][r]=player
        board[2][r]=player
        if check_winner(board)==False:
            print('Error: winner not detected')
            print_board(board)
            err = 1
    
    # case 3, diagonal
        board = [[' ' for _ in range(3)] for _ in range(3)]
        board[0][0]=player
        board[1][1]=player
        board[2][2]=player
        if check_winner(board)==False:
            print('Error: winner not detected')
            print_board(board)
            err = 1
    # case 4, diagonal
        board = [[' ' for _ in range(3)] for _ in range(3)]
        board[0][2]=player
        board[1][1]=player
        board[2][0]=player

        if check_winner(board)==False:
            print('Error: winner not detected')
            print_board(board)
            err = 1
    # case 5, tie
        board = [[' ' for _ in range(3)] for _ in range(3)]
        board[0][0]='X'
        board[0][1]='O'
        board[0][2]='X'
        board[1][1]='O'
        board[1][0]='X'
        board[1][2]='O'
        board[2][2]='X'
        board[2][1]='X'
        board[2][0]='O'

        if check_winner(board)==True:
            print('Oops:looks like you got a tie!')
            print_board(board)
            err=1

    '''
    Check for all possible win conditions and make sure that our check_winner function is correctly 
    declaring that a win condition is achieved.   Also test that if given a draw condition, the code
    correctly recognizes that there's no winner.
    '''
    if err==0:
        print("All test cases passed!")


def tic_tac_toe():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'
    while True:
        print_board(board)

        while True:
            row = int(input(f"Player {player}, choose row (1-3): ")) - 1
            if row >=0 and row <= 2:
                break

        while True:
            col = int(input(f"Player {player}, choose column (1-3): ")) - 1
            if col >=0 and col <=2:
                break


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
