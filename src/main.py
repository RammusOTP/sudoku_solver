from board import board, validate_board
from solver_functions import solve, print_board

def main():
    """
    Outputs the result of the sudoku
    :return:
    """
    if not validate_board(board):
        print("Invalid Sudoku board. The board is not a 9x9 square board.")
    else:
        print("Unsolved board:")
        print_board(board)
        if solve(board):
            print("Solved board:")
            print_board(board)
        else:
            print("No solution exists for the given Sudoku board.")


if __name__ == "__main__":
    main()