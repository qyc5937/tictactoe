import tkinter as tk
from tkinter import messagebo
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
    assert check_winner([['O','O','O'],[' ',' ',' '],[' ',' ',' ']]) == True
    assert check_winner([['X','X','X'],[' ',' ',' '],[' ',' ',' ']]) == True
    assert check_winner([['X',' ',' '],['X',' ',' '],['X',' ',' ']]) == True
    assert check_winner([['O',' ',' '],['O',' ',' '],['O',' ',' ']]) == True
    assert check_winner([[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]) == True
    assert check_winner([['O',' ',' '],[' ','O',' '],[' ',' ','O']]) == True
    assert check_winner([['X',' ',' '],[' ','X',' '],[' ',' ','X']]) == True
    assert check_winner([['X',' ',' '],['O','X',' '],['X',' ','X']]) == True
    assert check_winner([['X','O','X'],['O','X','O'],['O','X','O']]) == False
    assert check_winner([['X','O','X'],['X','O','O'],['O','X','X']]) == False
    assert check_winner([['X','O','X'],['X','X','O'],['O','X','O']]) == False
    print("All test cases passed!")

def update_gui():
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text=board[i][j])

'''
complete the function on_click
function should
1. Update the board and synchronize with the same update as buttons
2. Check for winner and prompt if a winner is found 
3. Check for ties and proompt
4. Check that the move is valid.  i.e. the box is not already taken
'''
def on_click(row, col):
    if board[row][col]==' ':
        board[row][col] = player
        update_gui()
        if check_winner(board):
            reset_game()
            return
        if all(board[n][m] !=' ' for n in range(3) for m in range (3):
            reset_game()
            return
    else:
        

'''
complete the logic for reset_game()
this should allow a new game to be played
'''
def reset_game():
    for i in range(3):
        for j in range(3):
            board[i][j] = ' '
            buttons[i][j].config(text='')
        player='X'
 

def create_gui():
    global buttons
    root = tk.Tk()
    root.title("Tic Tac Toe")
    buttons = [[None]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            buttons[i][j] = tk.Button(root, text=' ', font=('Arial', 30), width=3, height=1, command=lambda row=i, col=j: on_click(row, col))
            buttons[i][j].grid(row=i, column=j)
    return root

        
            

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
