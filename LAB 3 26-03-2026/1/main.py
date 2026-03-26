# Program 1: 8-Queens - All Solutions with Board Visualization

def print_board(board):
    for row in board:
        print(" ".join("Q" if x == 1 else "." for x in row))
    print()


def is_safe(board, row, col, n):
    # Column check
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve(board, row, n, solutions):
    if row == n:
        solutions.append([r[:] for r in board])
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve(board, row + 1, n, solutions)
            board[row][col] = 0


def main():
    n = 8
    board = [[0]*n for _ in range(n)]
    solutions = []

    solve(board, 0, n, solutions)

    print("Total solutions:", len(solutions))
    print()

    for i, sol in enumerate(solutions, 1):
    # for i, sol in enumerate(solutions[:]):
        print(f"Solution {i}:")
        print_board(sol)


if __name__ == "__main__":
    main()