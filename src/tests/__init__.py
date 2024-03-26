from src.board import validate_board
from src.solver_functions import print_board
from io import StringIO
import sys

def test_validate_board_pass():
    """
    Test the validate_board function, tests to see that the board shape is a 9x9
    :return: PASS
    """
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

def test_validate_board_fail():
    """
    Test the validate_board function, tests to see that the board shape is a 9x9
    :return: FAIL
    """
    test_board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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


def test_print_board_pass():
    """
    Tests the print_board function to ensure that the function prints as it intended
    :return: PASS
    """
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

    sys.stdout = StringIO()
    print_board(expected_board)
    captured = sys.stdout.getvalue()
    sys.stdout = sys.__stdout__
    assert captured == expected_output
