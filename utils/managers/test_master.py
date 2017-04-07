"""Test Master Module.

Module is needed to run tests in different modes.

Example:
    test_master.run_tests()

Module is not finished and could be changed.

Todo:
    * Expand current functionality with different modes of test running.

"""
import os
from utils.managers import install_master, user_config_manager
from utils.managers import app_config_manager, bin_config_manager



test_helper = {
    'is_already_installed': False,
    'bin_config': {},
    'user_config': {},
    'app_config': {}
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
    os.system('gulp backup')
    test_helper['user_config'] = user_config_manager._get_config()
    test_helper['app_config'] = app_config_manager._get_config()
    test_helper['bin_config'] = bin_config_manager._get_config()
    test_helper['is_already_installed'] = install_master.is_installed()

    install_master.remove()


def post_test_processing():
    """Post Test Processing

    Process after test to restore system

    """
    install_master.remove()
    if test_helper['is_already_installed']:
        install_master.install()
    app_config_manager._set_config(test_helper['app_config'])
    user_config_manager._set_config(test_helper['user_config'])
    bin_config_manager._set_config(test_helper['bin_config'])
