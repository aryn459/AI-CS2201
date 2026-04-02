N = 9

def is_consistent(board, row, col, num):
    for j in range(N):
        if board[row][j] == num:
            return False

    for i in range(N):
        if board[i][col] == num:
            return False

    start_row = 3 * (row // 3)
    start_col = 3 * (col // 3)

    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True


def select_unassigned_variable(board):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                return i, j
    return None


def backtrack(board):
    var = select_unassigned_variable(board)
    if not var:
        return True

    row, col = var

    for num in range(1, 10):
        if is_consistent(board, row, col, num):
            board[row][col] = num  # assign

            if backtrack(board):
                return True

            board[row][col] = 0  # unassign (backtrack)

    return False


def print_board(board):
    for row in board:
        print(" ".join(str(x) for x in row))


board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],

    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],

    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


if backtrack(board):
    print("Solved Sudoku:\n")
    print_board(board)
else:
    print("No solution exists.")