board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

current_player = "X"
winner = None
gameRunning = True

def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def playerBoard(board):
    user_input = int(input("Enter a number 1-9: "))
    if 1 <= user_input <= 9 and board[user_input - 1] == "-":
        board[user_input - 1] = current_player

    else:
        print("That spot is already taken or does not exist.")
        switchPlayer()

def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[4] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True


def checkVertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True


def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[2] and board[6] != "-":
        winner = board[2]
        return True


def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("It's a tie.")
        gameRunning = False


def checkForWin():
    global gameRunning
    if checkDiagonal(board) or checkHorizontal(board) or checkVertical(board):
        print(f"The winner is {winner}")
        gameRunning = False


def switchPlayer():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

print("Welcome to Tic Tac Toe!\nHere, Player X starts.\nThe first line is 1-3, then 4-6, then 7-9.\n")
while gameRunning:
    printBoard(board)
    playerBoard(board)
    checkForWin()
    checkTie(board)
    switchPlayer()