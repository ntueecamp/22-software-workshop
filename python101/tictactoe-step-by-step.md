## print()

``` python
print("Welcome to tic-tac-toe!")
```

## Variables input()

``` python
gameMode = input(
    "Do you want to play against the computer or another player? (c/p) "
)
print(gameMode)
```

## if statement

``` python
print("Welcome to tic-tac-toe!")

gameMode = input(
    "Do you want to play against the computer or another player? (c/p) "
)

if gameMode == "c":
    print("You are playing against the computer.")
elif gameMode == "p":
    print("You are playing against another player.")
else:
    print("Invalid input. Please try again.")
```

## while loop

``` python
print("Welcome to tic-tac-toe!")

while True:
    gameMode = input(
        "Do you want to play against the computer or another player? (c/p) "
    )
    if gameMode == "c":
        print("You are playing against the computer.")
        break
        print("You are playing against another player.")
        break
    elif gameMode == "p":
    else:
        print("Invalid input. Please try again.")
```

## list

``` python
board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
print(board)
board[0][0] = "X"
print(board)
```

## for loop

``` python
for i in range(3):
    print(board[i])
```

``` python
for i in range(3):
    for j in range(3):
        print(board[i][j] + ',', end=' ')
    print()
```

``` python
for i in range(3):
    for j in range(3):
        print(f" {board[i][j]} ", end="")
        if j < 2:
            print("|", end="")
    if i < 2:
        print("\n---|---|---")
```

## functions

``` python
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

showBoard(board)
```


## exercise 1

``` python
def getPlayerMove(player, board):
    print(f"Player {player}, please enter your move.")

    # TODO check if the move is valid: if the box is already taken, take another move until it is valid
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

    return (row - 1, col - 1)
```

### solution

``` python
def getPlayerMove(player, board):
    print(f"Player {player}, please enter your move.")
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
```

## exercise 1.5: check tie

### todo

``` python
def checkTie(board):
    # TODO check if the board is full
    return True
```

### solution

``` python
def checkTie(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                return False
    return True
```

## exercise 2: pvp mode

``` python
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
```

### todo

``` python
def pvpMode():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    showBoard(board)

    player = "O"
    while True:
        # TODO 1 get player move, play it on the board
        
        
        # TODO 2 check if the game is over
        # check if someone won
        # check if it's a tie
        # if yes, print the winner and break

        # TODO 3 switch player
        # switch player

        pass

    print("Thanks for playing!")
```

### solution

``` python
def pvpMode():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

    showBoard(board)

    player = "O"
    while True:
        print(f"Player {player}, please enter your move.")
        play(board, player, getPlayerMove(board))
        
        # check if the game is over
        if checkWin(board, player):
            showBoard(board)
            print(f"Player {player} wins!")
            break
        if checkTie(board):
            showBoard(board)
            print("Tie!")
            break
        
        # switch player
        if player == "O":
            player = "X"
        elif player == "X":
            player = "O"

    print("Thanks for playing!")
```

## import

``` python
import random

def getComputerMove(board):
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == " ":
            break
    return (row, col)
```

## exercise 3: final touch

``` python
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

```

### todo

``` python
print("Welcome to tic-tac-toe!")

# TODO finish the game

while True:
    gameMode = input(
        "Do you want to play against the computer or another player? (c/p) "
    )
    if gameMode == "c":
        print("You are playing against the computer.")
        break
    elif gameMode == "p":
        print("You are playing against another player.")
        break
    else:
        print("Invalid input. Please try again.")
```

### solution

``` python
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
```
