import random

# done
def showBoard(board):
    print("\n")
    for i in range(3):
        for j in range(3):
            print(f" {board[i][j]} ", end="")
            if j < 2:
                print("|", end="")
        if i < 2:
            print("\n---|---|---")
    print("\n")


# done
def getPlayerMove(board):
    while True:
        while True:
            row = int(input("Enter row (1-3): "))
            if row < 1 or row > 3:
                print("\nInvalid input. Please try again.")
                continue
            break

        while True:
            col = int(input("Enter column (1-3): "))
            if col < 1 or col > 3:
                print("\nInvalid input. Please try again.")
                continue
            break

        if board[row - 1][col - 1] == " ":
            break
        else:
            print("\nInvalid input. Please try again.")

    return (row - 1, col - 1)


def getComputerMove(board):
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == " ":
            break
    return (row, col)


def play(board, player, move):
    row, col = move
    board[row][col] = player
    showBoard(board)


def checkWin(board, player):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False


def checkTie(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False
    return True


def pvpMode():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    showBoard(board)

    player = "O"
    while True:
        print(f"Player {player}, please enter your move.")
        play(board, player, getPlayerMove(board))
        
        # check if the game is over
        if checkWin(board, player):
            print(f"Player {player} wins!")
            break
        if checkTie(board):
            print("Tie!")
            break
        
        # switch player
        if player == "O":
            player = "X"
        elif player == "X":
            player = "O"

    print("Thanks for playing!")


def computerMode():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    showBoard(board)

    player = "O"
    while True:
        if player == "O":
            print(f"Player {player}, please enter your move.")
            play(board, player, getPlayerMove(board))
        elif player == "X":
            play(board, player, getComputerMove(board))

        if checkWin(board, player):
            print(f"Player {player} wins!")
            break
        if checkTie(board):
            print("Tie!")
            break

        if player == "O":
            player = "X"
        elif player == "X":
            player = "O"

    print("Thanks for playing!")


# done
def main():
    print("Welcome to tic-tac-toe!")

    while True:
        gameMode = input(
            "Do you want to play against the computer or another player? (c/p) "
        )
        if gameMode == "c":
            print("You are playing against the computer.")
            computerMode()
            break
        elif gameMode == "p":
            print("You are playing against another player.")
            pvpMode()
            break
        else:
            print("Invalid input. Please try again.")


if __name__ == "__main__":
    main()
