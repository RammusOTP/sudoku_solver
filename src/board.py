#Input board here, a blank board is at the bottom to copy and paste to replace the old board

board = [
    [8, 0, 2, 9, 0, 0, 6, 0, 0],
    [0, 9, 0, 1, 3, 8, 0, 0, 0],
    [5, 0, 0, 2, 0, 0, 9, 8, 0],
    [0, 0, 7, 8, 2, 0, 0, 0, 0],
    [9, 0, 0, 0, 1, 0, 0, 7, 8],
    [1, 0, 8, 0, 6, 7, 4, 0, 0],
    [0, 6, 0, 0, 5, 0, 0, 3, 0],
    [7, 3, 0, 0, 8, 0, 1, 0, 6],
    [2, 0, 0, 6, 0, 3, 7, 4, 5]
]


def validate_board(board):
    """
    Validates the Sudoku board.
    :param board: 2D list representing the Sudoku board
    :return: True if the board is valid, False otherwise
    """
    if len(board) != 9:
        return False  # Incorrect number of rows

    for row in board:
        if len(row) != 9:
            return False  # Incorrect number of columns

        for cell in row:
            if not isinstance(cell, int) or not (0 <= cell <= 9):
                return False  # Invalid cell value

    return True

fresh_board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]