""" Bin Command Unit Tests.

This module is a test case for module utils.commands.bin_command.
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
import sys

from utils.helpers import clean_path
from utils.managers import user_config_manager, app_config_manager, bin_config_manager
from utils.commands import bin_command

from contextlib import contextmanager
from StringIO import StringIO

from setting.DEFAULT_CONFIGS import ERROR_MESSAGES

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



# @contextmanager
# def captured_output():
#     new_out, new_err = StringIO(), StringIO()
#     old_out, old_err = sys.stdout, sys.stderr
#     try:
#         sys.stdout, sys.stderr = new_out, new_err
#         yield sys.stdout, sys.stderr
#     finally:
#         sys.stdout, sys.stderr = old_out, old_err


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

    def test_move_bin(self):
        file_1 = os.path.join(self.test_folder_path, 'file_1')
        bin_move_path = os.path.join(self.test_folder_path, 'bin_move_path')
        os.mknod(file_1)
        bin_config_manager.history_add(file_1)
        clean_path.move(file_1, user_config_manager.get_property('bin_path'))
        self.assertEqual(
            bin_command.move_bin(bin_move_path),
            0
        )
        self.assertFalse(
            os.path.exists(os.path.join(self.test_bin_path, 'file_1'))
        )
        self.assertTrue(
            os.path.exists(os.path.join(bin_move_path, 'file_1'))
        )
        self.assertEqual(
            user_config_manager.get_property('bin_path'),
            bin_move_path
        )
        self.assertEqual(
            len(bin_config_manager.get_property('history')),
            1
        )

    def test_move_bin_with_relative_path(self):
        file_1 = os.path.join(self.test_folder_path, 'file_1')
        bin_move_rel_path = os.path.relpath(
                os.path.join(
                    self.test_folder_path,
                    'bin_move_path'
                ),
                os.getcwd()
            )
        os.mknod(file_1)
        bin_config_manager.history_add(file_1)
        clean_path.move(file_1, user_config_manager.get_property('bin_path'))
        self.assertEqual(
            bin_command.move_bin(bin_move_rel_path),
            0
        )
        self.assertFalse(
            os.path.exists(os.path.join(self.test_bin_path, 'file_1'))
        )
        self.assertTrue(
            os.path.exists(
                os.path.join(
                    user_config_manager.get_property('bin_path'),
                    'file_1'
                )
            )
        )
        self.assertEqual(
            user_config_manager.get_property('bin_path'),
            os.path.abspath(bin_move_rel_path)
        )
        self.assertEqual(
            len(bin_config_manager.get_property('history')),
            1
        )

    def test_copy_bin(self):
        file_1 = os.path.join(self.test_folder_path, 'file_1')
        bin_copy_path = os.path.join(self.test_folder_path, 'bin_copy_path')
        os.mknod(file_1)
        bin_config_manager.history_add(file_1)
        clean_path.move(file_1, user_config_manager.get_property('bin_path'))
        self.assertEqual(
            bin_command.copy_bin(bin_copy_path),
            0,
            msg="Should return success code: 0."
        )
        self.assertEqual(
            len(bin_config_manager.get_property('history')),
            1,
        )
        self.assertTrue(
            os.path.exists(os.path.join(bin_copy_path, 'file_1')),
            msg="Should copy innear files too"
        )
        self.assertEqual(
            user_config_manager.get_property('bin_path'),
            self.test_bin_path
        )

    def test_copy_bin_with_rel_path(self):
        file_1 = os.path.join(self.test_folder_path, 'file_1')
        bin_copy_rel_path = os.path.relpath(
            os.path.join(
                self.test_folder_path,
                'bin_copy_path'
            ),
            os.getcwd()
        )

        os.mknod(file_1)
        bin_config_manager.history_add(file_1)
        clean_path.move(file_1, user_config_manager.get_property('bin_path'))
        self.assertEqual(
            bin_command.copy_bin(bin_copy_rel_path),
            0,
            msg="Should return success code: 0."
        )
        self.assertEqual(
            len(bin_config_manager.get_property('history')),
            1,
        )
        self.assertTrue(
            os.path.exists(os.path.join(user_config_manager.get_property('bin_path'), 'file_1')),
            msg="Should copy innear files too"
        )
        self.assertEqual(
            user_config_manager.get_property('bin_path'),
            os.path.abspath(self.test_bin_path)
        )

    def test_empty_bin(self):
        file_1 = os.path.join(self.test_folder_path, 'file_1')
        os.mknod(file_1)
        bin_config_manager.history_add(file_1)
        clean_path.move(file_1, user_config_manager.get_property('bin_path'))
        self.assertTrue(
            os.path.exists(
                os.path.join(
                    user_config_manager.get_property('bin_path'),
                    'file_1'
                )
            )
        )
        self.assertFalse(os.path.exists(file_1), msg="File should be in bin.")
        self.assertEqual(
            bin_config_manager.history_get('file_1')['src_dir'],
            os.path.dirname(file_1),
            msg="Initial preparations fails."
        )
        self.assertEqual(
            bin_command.empty_bin(),
            0,
            msg='Bin command should return success code: 0.'
        )
        self.assertFalse(
            os.path.exists(
                os.path.join(
                    user_config_manager.get_property('bin_path'),
                    'file_1'
                )
            )
        )
        self.assertEqual(
            len(bin_config_manager.get_property('history')),
            0
        )

    def test_create_bin(self):
        file_1 = os.path.join(self.test_folder_path, 'file_1')
        os.mknod(file_1)
        clean_path.move(file_1, user_config_manager.get_property('bin_path'))
        bin_config_manager.history_add(file_1)
        new_bin_location = os.path.join(self.test_folder_path, 'new_bin_location')
        self.assertEqual(
            bin_command.create_bin(new_bin_location),
            0,
            msg='Bin command should return success code: 0.'
        )
        self.assertEqual(
            len(bin_config_manager.get_property('history')),
            0,
            msg="New bin should be empty."
        )
        self.assertEqual(
            user_config_manager.get_property('bin_path'),
            new_bin_location,
            msg="New path should be writen to user config file"
        )

    def test_create_bin_with_rel_path(self):
        file_1 = os.path.join(self.test_folder_path, 'file_1')
        os.mknod(file_1)
        clean_path.move(file_1, user_config_manager.get_property('bin_path'))
        bin_config_manager.history_add(file_1)
        new_bin_rel_path = os.path.relpath(
            os.path.join(
                self.test_folder_path,
                'new_bin_rel_path'
            ),
            os.getcwd()
        )
        self.assertEqual(
            bin_command.create_bin(new_bin_rel_path),
            0, msg='Bin command should return success code: 0.'
        )
        self.assertEqual(
            len(bin_config_manager.get_property('history')),
            0, msg="New bin should be empty."
        )
        self.assertEqual(
            user_config_manager.get_property('bin_path'),
            os.path.abspath(new_bin_rel_path),
            msg="New path should be writen to user config file"
        )

    # def test_get_bin_path_success(self):
    #     with captured_output() as (out, err):
    #         self.assertFalse(
    #             bin_command.get_bin_path()
    #         )
    #
    #     output = out.getvalue().strip()
    #     self.assertEqual(
    #         user_config_manager.get_property('bin_path'),
    #         output
    #     )
    #
    # def test_get_bin_path_not_exists(self):
    #     user_config_manager.set_property('bin_path', '')
    #     with captured_output() as (out, err):
    #         self.assertFalse(
    #             bin_command.get_bin_path()
    #         )
    #
    #     output = out.getvalue().strip()
    #     self.assertEqual(
    #         ERROR_MESSAGES['bin_not_exists'],
    #         output
    #     )
