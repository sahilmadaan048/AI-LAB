# Program 3: Generalized N-Queens Problem

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


def count_solutions(n):
    board = [[0]*n for _ in range(n)]
    count = [0]

    def solve(row):
        if row == n:
            count[0] += 1
            return

        for col in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 1
                solve(row + 1)
                board[row][col] = 0

    solve(0)
    return count[0]


def main():
    values = [4, 6, 8, 10, 12]

    print("N\tNumber of Solutions")
    print("--------------------------")

    for n in values:
        result = count_solutions(n)
        print(f"{n}\t{result}")


if __name__ == "__main__":
    main()