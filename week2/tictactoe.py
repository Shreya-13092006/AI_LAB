board = [" "] * 9

def show():
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])

def check():
    wins = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for a, b, c in wins:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return board[a]

    if " " not in board:
        return "draw"

    return None

def minimax(turn):
    result = check()

    if result == "O":
        return 1
    if result == "X":
        return -1
    if result == "draw":
        return 0

    if turn == "O":
        best = -10

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax("X")
                board[i] = " "

                if score > best:
                    best = score

        return best

    else:
        best = 10

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax("O")
                board[i] = " "

                if score < best:
                    best = score

        return best

def computer():
    best = -10
    move = 0

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax("X")
            board[i] = " "

            if score > best:
                best = score
                move = i

    board[move] = "O"

while True:
    show()

    move = int(input("Enter position (1-9): ")) - 1

    if move < 0 or move > 8 or board[move] != " ":
        print("Invalid move")
        continue

    board[move] = "X"

    result = check()
    if result:
        show()
        print("Result:", result)
        break

    computer()

    result = check()
    if result:
        show()
        print("Result:", result)
        break
