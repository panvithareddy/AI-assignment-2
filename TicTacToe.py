import random

board = [" " for i in range(9)]

def print_board():
    print()
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        if i < 6:
            print("--+---+--")
    print()

def check_winner(player):
    win_positions = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]

    for a,b,c in win_positions:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def board_full():
    return " " not in board

def human_move():
    pos = int(input("Enter position (1-9): ")) - 1
    if board[pos] == " ":
        board[pos] = "X"
    else:
        print("Position already taken!")
        human_move()

def ai_move():
    empty = [i for i in range(9) if board[i] == " "]
    move = random.choice(empty)
    board[move] = "O"
    print("AI placed O at position", move+1)

print("TIC TAC TOE (Human vs AI)")
print("Positions are numbered 1 to 9")

while True:

    print_board()
    human_move()

    if check_winner("X"):
        print_board()
        print("You Win!")
        break

    if board_full():
        print_board()
        print("Game Draw!")
        break

    ai_move()

    if check_winner("O"):
        print_board()
        print("AI Wins!")
        break

    if board_full():
        print_board()
        print("Game Draw!")
        break