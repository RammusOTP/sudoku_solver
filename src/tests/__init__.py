from src.board import validate_board
from src.solver_functions import print_board

def test_validate_board():
    test_board = [
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

    result = validate_board(test_board)

    assert result is True
    assert len(test_board) == 9
    for row in test_board:
        assert len(row) == 9

from io import StringIO
import sys

def test_print_board(capsys):
    expected_output = '''1 0 1 | 0 1 0 | 1 0 1
0 1 0 | 1 0 1 | 0 1 0
1 0 1 | 0 1 0 | 1 0 1
- - - + - - - + - - -
0 1 0 | 1 0 1 | 0 1 0
1 0 1 | 0 1 0 | 1 0 1
0 1 0 | 1 0 1 | 0 1 0
- - - + - - - + - - -
1 0 1 | 0 1 0 | 1 0 1
0 1 0 | 1 0 1 | 0 1 0
1 0 1 | 0 1 0 | 1 0 1
'''

    expected_board = [
        [1, 0, 1, 0, 1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0, 1, 0, 1, 0],
        [1, 0, 1, 0, 1, 0, 1, 0, 1]
    ]

    # Redirect stdout to capture printed output
    sys.stdout = StringIO()

    # Call the function
    print_board(expected_board)

    # Get printed output
    captured = sys.stdout.getvalue()

    # Reset redirect
    sys.stdout = sys.__stdout__

    # Assert printed output matches expected
    assert captured == expected_output
