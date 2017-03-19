"""Test Master Module.

Module is needed to run tests in different modes.

Example:
    test_master.run_tests()

Module is not finished and could be changed.

Todo:
    * Expand current functionality with different modes of test running.

"""
import os


def run_tests():
    """Tests runner function"""
    os.system("python -m unittest discover -v -s './tests'")
