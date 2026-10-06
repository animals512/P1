def solve_n_queens(n):
    board = [-1] * n

    def safe(row, col):
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == abs(i - row):
                return False
        return True

    def solve(row):
        if row == n:
            return True

        for col in range(n):
            if safe(row, col):
                board[row] = col

                if solve(row + 1):
                    return True

                board[row] = -1

        return False

    solve(0)

    for row in range(n):
        for col in range(n):
            if board[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


# 4 x 4
print("4-Queens Solution:")
solve_n_queens(4)

# 8 x 8
#print("\n8-Queens Solution:")
#solve_n_queens(8)
