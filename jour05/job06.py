def can_place_checker(board, row, col):
    for i in range(len(board)):
        if board[row][i] == "X" or board[i][col] == "X":
            return False
    
    for i in range(len(board)):
        for j in range(len(board)):
            if i + j == row + col or i - j == row - col:
                if board[i][j] == "X":
                    return False
    
    return True


def place_checkers(board, n, row=0):
    if row == n:
        return True
    
    for col in range(n):
        if can_place_checker(board, row, col):
            board[row][col] = "X"
            if place_checkers(board, n, row + 1):
                return True
            board[row][col] = "O"
    
    return False


def print_board(board):
    for row in board:
        print(" ".join(row))


n = int(input("Enter the size of the board: "))
board = [["O" for _ in range(n)] for _ in range(n)]

if place_checkers(board, n):
    print_board(board)
else:
    print("No solution found.")
