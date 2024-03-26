from test_solver_functions import *


def run_tests():
    test_functions = [
        test_validate_board_pass,
        test_validate_board_fail,
        test_print_board_pass
    ]

    passed_tests = 0
    total_tests = len(test_functions)

    for test_func in test_functions:
        try:
            test_func()
            print(f"\033[92m[Passed]\033[0m {test_func.__name__}")
            passed_tests += 1
        except AssertionError as e:
            print(f"\033[91m[Failed]\033[0m {test_func.__name__}: {e}")

    print(f"\n{passed_tests}/{total_tests} tests passed.")


if __name__ == "__main__":
    run_tests()
