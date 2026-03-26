# Program 4: 8-Queens with Pre-Placed Queen at (0,3)

def print_board(board):
    for row in board:
        print(" ".join("Q" if x == 1 else "." for x in row))
    print()


def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False

    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve(board, row, n, count):
    if row == n:
        count[0] += 1
        return

    if row == 0:  # Skip since row since here queen is fixed
        solve(board, row + 1, n, count)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve(board, row + 1, n, count)
            board[row][col] = 0


def main():
    n = 8
    board = [[0]*n for _ in range(n)]

    # Pre-place queen at (0,3)
    board[0][3] = 1

    count = [0]
    solve(board, 0, n, count)

    print("Solutions with queen at (0,3):", count[0])
    print()
    print("One such solution is: ", print_board(board))


if __name__ == "__main__":
    main()