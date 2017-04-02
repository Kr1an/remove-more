""" Execution Manager Test Case.

This module is a test case for module utils.managers.execution_manager.
It test functionality of:
    * execute_command().

Example:
    write 'python setup.py -t' in terminal.

Attributes:
    TEST_FOLDER_PATH: file with json 'some' mock date for tests.

Test Module is not finished.
Find particular test class or test in is's name(title).

"""

import unittest

import os
import shutil

from utils.helpers import clean_path
from utils.managers import user_config_manager, app_config_manager, bin_config_manager
from utils.managers import execution_manager
from utils.commands import delete_command

TEST_FOLDER_PATH = \
    os.path.abspath(
        os.path.join(
            __file__,
            '..',
            'mock',
            'mock_folder_for_execution_manager_test_case'
        )
    )

TEST_BIN_PATH = \
    os.path.abspath(
        os.path.join(
            TEST_FOLDER_PATH,
            'bin'
        )
    )


class ExecutionManagerTestCase(unittest.TestCase):
    def setUp(self):
        self.options = {}
        self.paths = {}
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

    def test_execution_manager_with_create_bin(self):
        new_bin_location = os.path.join(
            self.test_folder_path,
            'new_bin'
        )

        self.options.update({'mods': ['create_bin'], 'path': new_bin_location})
        self.assertEqual(
            execution_manager.execute_command(self.paths, self.options),
            0, msg="Execute command should return success code: 0."
        )
        self.assertEqual(
            user_config_manager.get_property('bin_path'),
            new_bin_location
        )
        self.assertEqual(
            len(bin_config_manager.get_property('history')),
            0
        )

    def test_execution_manager_with_copy_bin(self):
        file_1 = os.path.join(self.test_folder_path, 'file_1')
        os.mknod(file_1)
        delete_command.delete([file_1])
        copy_bin_location = os.path.join(self.test_folder_path, 'copy_bin')
        self.options.update({'mods': ['copy_bin'], 'path': copy_bin_location})
        self.assertEqual(
            execution_manager.execute_command(self.paths, self.options),
            0, msg="Execute command should return success code: 0."
        )
        self.assertTrue(os.path.exists(os.path.join(self.test_bin_path, os.path.basename(file_1))))
        self.assertTrue(os.path.exists(os.path.join(copy_bin_location, os.path.basename(file_1))))
        self.assertEqual(
            user_config_manager.get_property('bin_path'),
            self.test_bin_path
        )


    def test_execution_manager_with_move_bin(self):
        file_1 = os.path.join(self.test_folder_path, 'file_1')
        os.mknod(file_1)
        delete_command.delete([file_1])
        new_bin_location = os.path.join(self.test_folder_path, 'new_bin')

        self.options.update({'mods': ['move_bin'], 'path': new_bin_location})
        self.assertEqual(
            execution_manager.execute_command(self.paths, self.options),
            0, msg="Execute command should return success code: 0."
        )
        self.assertEqual(
            user_config_manager.get_property('bin_path'),
            new_bin_location
        )
        self.assertTrue(
            os.path.exists(
                os.path.join(new_bin_location, os.path.basename(file_1))
            )
        )
        self.assertEqual(
            bin_config_manager.history_get(os.path.basename(file_1))['src_dir'],
            os.path.dirname(file_1)
        )


    def test_execution_manager_with_empty_bin(self):
        file_1 = os.path.join(self.test_folder_path, 'file_1')
        os.mknod(file_1)
        delete_command.delete([file_1])
        self.options.update({'mods': ['empty_bin']})
        self.assertEqual(
            execution_manager.execute_command(self.paths, self.options),
            0, msg="Execute command should return success code: 0."
        )
        self.assertEqual(
            len(bin_config_manager.get_property('history')),
            0
        )
        self.assertFalse(
            os.path.exists(file_1)
        )
        self.assertFalse(
            os.path.exists(
                os.path.join(
                    user_config_manager.get_property('bin_path'),
                    os.path.basename(file_1)
                )
            )
        )

    def test_execution_manager_with_empty_bin_with_second_key_format(self):
        file_1 = os.path.join(self.test_folder_path, 'file_1')
        os.mknod(file_1)
        delete_command.delete([file_1])
        self.options.update({'mods': ['binempty']})
        self.assertEqual(
            execution_manager.execute_command(self.paths, self.options),
            0, msg="Execute command should return success code: 0."
        )
        self.assertEqual(
            len(bin_config_manager.get_property('history')),
            0
        )
        self.assertFalse(
            os.path.exists(file_1)
        )
        self.assertFalse(
            os.path.exists(
                os.path.join(
                    user_config_manager.get_property('bin_path'),
                    os.path.basename(file_1)
                )
            )
        )

    def test_execution_manager_with_delete(self):
        file_1 = os.path.join(self.test_folder_path, 'file_1')
        os.mknod(file_1)
        self.assertTrue(
            os.path.exists(
                file_1
            )
        )
        self.options.update({'mods': ['remove']})
        self.paths = [file_1]
        self.assertEqual(
            execution_manager.execute_command(self.paths, self.options),
            0, msg="Execute command should return success code: 0."
        )
        self.assertFalse(
            os.path.exists(
                file_1
            )
        )
        self.assertEqual(
            len(bin_config_manager.get_property('history')),
            1
        )
        self.assertEqual(
            bin_config_manager.history_get(os.path.basename(file_1))['src_dir'],
            os.path.dirname(file_1)
        )

    def test_execution_manager_with_restore(self):
        file_1 = os.path.join(self.test_folder_path, 'file_1')
        os.mknod(file_1)

        self.assertEqual(
            delete_command.delete([file_1]),
            0, msg="Execute command should return success code: 0."
        )

        self.paths = [
            os.path.join(
                user_config_manager.get_property('bin_path'),
                os.path.basename(file_1)
            )
        ]

        self.options.update({'mods': ['restore']})

        self.assertEqual(
            execution_manager.execute_command(self.paths, self.options),
            0, msg="Execute command should return success code: 0."
        )

        self.assertFalse(
            os.path.exists(
                os.path.join(
                    user_config_manager.get_property('bin_path'),
                    os.path.basename(file_1)
                )
            )
        )
        self.assertEqual(
            len(bin_config_manager.get_property('history')),
            0
        )



