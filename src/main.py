from board import board
from solver_functions import solve, print_board

if __name__ == "__main__":
    print("Unsolved:")
    print_board(board)
    solve(board)
    print("Solved:")
    print_board(board)