""" Property Reader Unit Tests.

This module is a test case for module utils.helpers.property_reader.
It test functionality of:
    * def history_add().
    * def history_del().
    * def history_empty().
    * def history_get().

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
from utils.managers import user_config_manager, bin_config_manager, app_config_manager

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


class BinConfigManagerTestCase(unittest.TestCase):
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
        self.assertTrue(os.path.exists(self.test_bin_path), "Initial Structure Exception.")
        self.assertEqual(
            user_config_manager.get_property('bin_path'),
            self.test_bin_path,
            msg="Test bin does not exists."
        )
        self.assertEqual(
            len(bin_config_manager.get_property('history')),
            0,
            msg="Initial Exception: len should equal to 0."
        )

    def test_history_add(self):
        file_1 = os.path.join(self.test_bin_path, 'file_1')
        bin_config_manager.history_add(file_1)
        self.assertEqual(
            len(bin_config_manager.get_property('history')),
            1,
            msg="History len should be 1 after adding element."
        )
        self.assertEqual(
            bin_config_manager.get_property('history')[0]['bin_name'],
            os.path.basename(file_1),
            msg="Wrong history item name."
        )
        self.assertEqual(
            bin_config_manager.get_property('history')[0]['src_dir'],
            os.path.dirname(file_1),
            msg="Wrong history item src_dir."
        )

    def test_history_delete(self):
        file_1 = os.path.join(self.test_bin_path, 'file_1')
        bin_config_manager.history_add(file_1)
        bin_config_manager.history_del(os.path.basename(file_1))
        self.assertEqual(
            len(bin_config_manager.get_property('history')),
            0,
            msg="History len should be 0 after removing element."
        )

    def test_history_empty(self):
        files = [os.path.join(self.test_bin_path, str(idx)) for idx in range(5)]
        for file in files:
            bin_config_manager.history_add(file)

        self.assertEqual(
            len(bin_config_manager.get_property('history')),
            5,
            msg="History should be equal to 5 after adding 5 different elements to it."
        )
        history = bin_config_manager.get_property('history')
        [
            self.assertEqual(
                os.path.join(
                    history[i]['src_dir'],
                    history[i]['bin_name']
                ),
                files[i]
            ) for i in range(5)
        ]
        bin_config_manager.history_empty()
        self.assertEqual(
            len(bin_config_manager.get_property('history')),
            0,
            msg="History should be len 0 after history_empty."
        )

    def test_history_get(self):
        file_1 = os.path.join(self.test_bin_path, 'file_1')
        file_1_name = os.path.basename(file_1)
        bin_config_manager.history_add(file_1)
        self.assertEqual(
            bin_config_manager.history_get(file_1_name)['src_dir'],
            os.path.dirname(file_1)
        )
        self.assertEqual(
            bin_config_manager.history_get(file_1_name)['bin_name'],
            os.path.basename(file_1)
        )
