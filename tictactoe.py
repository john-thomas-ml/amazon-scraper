import random

def printboard(board):
    for i in range(3):
        print('|'.join([' ' if x == -1 else 'X' if x == 1 else 'O' for x in board[i*3:(i+1)*3]]))

def checkwin(board):
    for i in range(0,9,3):
        if board[i] == board [i+1] == board[i+2] and board[i] != -1:
            return True
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] and board[i] != -1:
            return True
    if board[0] == board[4] == board[8] and board[0] != -1:
        return True
    if board[2] == board[4] == board[6] and board[2] != -1:
        return True
    return False 

def play(board,chance):
    while True:
        try:
            position = int(input("Enter a location(0-8): "))
            if position  > 8 or position < 0:
                raise ValueError("Position Invalid! Try again.")
            if board[position] != -1:
                raise ValueError("Position already picked! Try another spot.")
            break
        except ValueError as e:
            print(e)
    board[position] = chance

if __name__ == "__main__":
    current = random.choice(['x','o'])
    chance = 1 if current == 'x' else 0
    board = [-1 for i in range(9)]
    for i in range(3):
        print('|'.join([str(x) for x in range(i*3,(i+1)*3)]))
    while True:
        print(f"Its {current.upper()}'s turn: ")
        printboard(board)
        play(board,chance)
        if checkwin(board):
            print(f"{current.upper()} wins!")
            printboard(board)
            break
        if -1 not in board:
            print("Its a draw!!")
            printboard(board)
            break
        chance = (chance + 1)%2
        current = 'x' if chance == 1 else 'o'