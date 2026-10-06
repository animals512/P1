board = [" "] * 9

def display():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

def check_winner():
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in wins:
        if board[a] == board[b] == board[c] != " ":
            return board[a]

    if " " not in board:
        return "Draw"

    return None


player = "X"

while True:
    display()

    position = int(input(f"Player {player}, enter position (1-9): ")) - 1

    if position < 0 or position > 8 or board[position] != " ":
        print("Invalid move! Try again.")
        continue

    board[position] = player

    result = check_winner()

    if result:
        display()

        if result == "Draw":
            print("Game Draw!")
        else:
            print("Player", result, "wins!")

        break

    player = "O" if player == "X" else "X"