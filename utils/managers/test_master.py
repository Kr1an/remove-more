"""Test Master Module.

Module is needed to run tests in different modes.

Example:
    test_master.run_tests()

Module is not finished and could be changed.

Todo:
    * Expand current functionality with different modes of test running.

"""
import os
from utils.managers import install_master


test_helper = {
    'is_already_installed': False
}


def run_tests():
    """Run Tests Function.

    Run unittest in default mode.

    """
    pre_test_processing()
    os.system("python -m unittest discover -v -s './tests'")
    post_test_processing()


def pre_test_processing():
    """Pre Test Processing

    Prepare System before tests

    """
    test_helper['is_already_installed'] = install_master.is_installed()
    install_master.remove()


def post_test_processing():
    """Post Test Processing

    Process after test to restore system

    """
    install_master.remove()
    if test_helper['is_already_installed']:
        install_master.install()
