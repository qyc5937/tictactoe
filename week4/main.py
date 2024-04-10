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
    update_gui()
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
            update_gui()
            game_ended = has_game_ended('O')
    else:
        messagebox.showwarning("Invalid Move", "That spot is already taken!")

'''
complete ai_move function.   

a naive implementation, will check if there's a winning move for the human player and block it
if a winning move does not exists, take the first empty spot.

this can be further improved by using minmax algorithm. https://en.wikipedia.org/wiki/Minimax
'''
def ai_move(human_player):
    if winning_move():
        return
    elif prevent_losing():
        return
    elif block_win(): 
        return
    else: 
        play_random()
        return

def block_win():
    global board
    rowX = [0, 0, 0]
    colX = [0, 0, 0]
    diagX = [0, 0]
    for i in range(3):
        for j in range(3):  
            if board[i][j] == 'X':
                rowX[i] += 1  
                colX[j] += 1 
            if i == j: 
                if board[i][j] == 'X':
                    diagX[0] += 1
            if i + j == 2: 
                if board[i][j] == 'X':
                    diagX[1] += 1
    for i in range(3):
        if rowX[i]==2:
            for j in range(3): 
                if board[i][j]==' ':
                    board[i][j]='O'
                    return True
    for i in range(3):
        if colX[i]==2:
            for j in range(3): 
                if board[j][i]==' ':
                    board[j][i]='O'
                    return True
    if diagX[0]==2:
        for i in range(3):
            if board[i][i]==' ':
                board[i][i]='O'
                return True
    if diagX[1]==2:
        for i in range(3):
            if board[i][2-i]==' ':
                board[i][2-i]='O'
                return True
    return False

def play_random():
    import random
    while True:        
        # pick random i,j
        i = random.randint(0,2)
        j = random.randint(0,2)
        if board[i][j]==' ':
            board[i][j]='O'
            return True
    return False

def prevent_losing():
    global board
    count=0
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                count += 1
    if count==8:
        if 'X' == board[1][0] or 'X' == board[0][1] or 'X' == board[2][2] or 'X' == board[2][1]:
                board[1][1] = 'O'
                return True
    return False

def winning_move():
    global board
    rowX = [0, 0, 0]
    colX = [0, 0, 0]
    diagX = [0, 0]
    for i in range(3): 
        for j in range(3):  
            if board[i][j] == 'O':
                rowX[i] += 1  
                colX[j] += 1  
            if i == j:  
                if board[i][j] == 'O':
                    diagX[0] += 1
            if i + j == 2:
                if board[i][j] == 'O':
                    diagX[1] += 1   
    for i in range(3):
        if rowX[i]==2:
            for j in range(3): 
                if board[i][j]==' ':
                    board[i][j]='O'
                    return True
    for i in range(3):
        if colX[i]==2:
            for j in range(3): 
                if board[j][i]==' ':
                    board[j][i]='O'
                    return True
    if diagX[0]==2:
        for i in range(3):
            if board[i][i]==' ':
                board[i][i]='O'
                return True
    if diagX[1]==2:
        for i in range(3):
            if board[i][2-i]==' ':
                board[i][2-i]='O'
                return True
    return False
def reset_game():
    global board, player
    for i in range(3):
        for j in range(3):
            board[i][j] = ' '
            buttons[i][j].config(text=' ')
    player = 'X'

def create_gui():
    global buttons
    root = tk.Tk()
    root.title("𐬹Tic𐬹Tac𐬹Toe𐬹")
    buttons = [[None]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            buttons[i][j] = tk.Button(root, text=' ', font=('Arial', 30), width=3, height=1, command=lambda row=i, col=j: on_click(row, col))
            buttons[i][j].grid(row=i, column=j)
    return root


def test_check_winner():
    # Test rows
    assert check_winner([['X', 'X', 'X'], [' ', ' ', ' '], [' ', ' ', ' ']]) == True
    assert check_winner([[' ', ' ', ' '], ['X', 'X', 'X'], [' ', ' ', ' ']])== True
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