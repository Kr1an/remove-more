""" Property Reader Unit Tests.

This module is a test case for module utils.helpers.property_reader.
It test functionality of:
    * def move_bin().
    * def copy_bin().
    * def empty_bin().
    * def create_bin().

Example:
    write 'python setup.py -t' in terminal.

Attributes:
    TEST_FOLDER_PATH: file with json 'some' mock date for tests.

Test Module is finished.
Find particular test class or test in is's name(title).

"""

import unittest

import os
import shutil

from utils.helpers import clean_path
from utils.managers import user_config_manager, app_config_manager, bin_config_manager

TEST_FOLDER_PATH = \
    os.path.abspath(
        os.path.join(
            __file__,
            '..',
            'mock',
            'mock_folder_for_bin_config_manager'
        )
    )

TEST_BIN_PATH = \
    os.path.abspath(
        os.path.join(
            __file__,
            '..',
            'mock',
            'mock_folder_for_bin_config_manager',
            'bin'
        )
    )


class BinCommandTestCase(unittest.TestCase):
    def setUp(self):
        self.test_folder_path = TEST_FOLDER_PATH
        self.test_bin_path = TEST_BIN_PATH
        self.real_bin_path = user_config_manager.get_property('bin_path')
        self.real_bin_history = bin_config_manager.get_property('history')
        user_config_manager.set_property('bin_path', self.test_bin_path)
        bin_config_manager.set_property('history', [])
        os.mkdir(self.test_folder_path)
        os.mkdir(self.test_bin_path)

    def tearDown(self):
        shutil.rmtree(self.test_folder_path)
        user_config_manager.set_property('bin_path', self.real_bin_path)
        bin_config_manager.set_property('history', self.real_bin_history)

    def test_initial_structure(self):
        pass

    def test_move_bin(self):
        pass

    def test_copy_bin(self):
        pass

    def test_empty_bin(self):
        pass

    def test_create_bin(self):
        pass
