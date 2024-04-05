import tkinter as tk
from tkinter import messagebox

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 10)

def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != ' ':
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[2][col]!= ' ':
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return True

    return False

def update_gui():
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text=board[i][j])

def has_game_ended(player):
    if check_winner(board):
        messagebox.showinfo("Winner", f"Player {player} wins!")
        reset_game()
        return True
    if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
        messagebox.showinfo("Tie", "It's a tie!")
        reset_game()
        return True
    return False

def on_click(row, col):
    global player
    if board[row][col] == ' ':
        board[row][col] = player
        update_gui()
        game_ended = has_game_ended(player)
        if game_ended != True:
            ai_move(player)

    else:
        messagebox.showwarning("Invalid Move", "That spot is already taken!")

'''
complete ai_move function.   

a naive implementation, will check if there's a winning move for the human player and block it
if a winning move does not exists, take the first empty spot.

this can be further improved by using minmax algorithm. https://en.wikipedia.org/wiki/Minimax
'''
def ai_move(human_player):
    bot = 'X' if human ='O'
    for i in range(3):
        for j in range(3):
            if board[i][j]==' ':
                
    pass

def reset_game():
    global board, player
    for i in range(3):
        for j in range(3):
            board[i][j] = ' '
            buttons[i][j].config(text=' ')
    player = 'X'
    
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)
print(factorial(n))

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
    global board, player
    board = [[' ' for _ in range(3)] for _ in range(3)]
    player = 'X'
    root = create_gui()
    root.mainloop()

if __name__ == "__main__":
    test_check_winner()
    tic_tac_toe()
