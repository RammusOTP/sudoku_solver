def print_board(board):
    """
    Iterates over all cells in the board and print them to output the board. Uses - and | and + to show the boxes visually.
    :param board:
    :return:
    """
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print('- - - + - - - + - - -')
        for j in range(len(board)):
            if j % 3 == 0 and j != 0:
                print('|', end=' ')
            if j == 8:
                print(board[i][j])
            else:
                print(f"{str(board[i][j])} ", end="")

def find_empty_cell(board):
    """
    Finds the first empty cell in the board. In this case empty cells are 0.
    :param board: 
    :return: tuple with the row, col as values in it.
    """
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)

def valid(board, number, position):
    """
    Iterates through 1 to 9 and finds the lowest possible number that fits the cell.
    :param board:
    :param number:
    :param position:
    :return: True if number is valid, False otherwise
    """
    for i in range(len(board[0])):
        if board[position[0]][i] == number and position[1] != i:
            return False

    for i in range(len(board)):
        if board[i][position[1]] == number and position[0] != i:
            return False

    x = position[1] // 3
    y = position[0] // 3

    for i in range(y * 3, y * 3 + 3):
        for j in range(x * 3, x * 3 + 3):
            if board[i][j] == number and position != (i, j):
                return False

    return True
def solve(board):
    """
    Uses find_empty_cell to find the first empty cell and fills it using valid, then iterates over the whole board
    till it is solved
    :param board:
    :return: True if the board is valid, False otherwise
    """
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        return True
    else:
        row, col = empty_cell

    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False
