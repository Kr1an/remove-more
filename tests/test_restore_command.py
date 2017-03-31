    #
""" Restore Command Unit Tests.

This module is a test case for module utils.commands.restore_command.
It test functionality of:
    * def restore().
    * def _move_from_bin().
    * def _get_restore_paths().

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
from utils.commands import restore_command, delete_command

TEST_FOLDER_PATH = \
    os.path.abspath(
        os.path.join(
            __file__,
            '..',
            'mock',
            'mock_folder_for_restore_command_test_case'
        )
    )

TEST_BIN_PATH = \
    os.path.abspath(
        os.path.join(
            TEST_FOLDER_PATH,
            'rrbin'
        )
    )


class RestoreCommandTestCase(unittest.TestCase):
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

    def test_restore_with_file(self):
        file_1 = os.path.join(self.test_folder_path, 'file_1')
        os.mknod(file_1)
        self.assertTrue(os.path.exists(file_1))
        delete_command.delete([file_1])
        self.assertFalse(os.path.exists(file_1))
        self.assertEqual(
            restore_command.restore(
                [os.path.join(
                    user_config_manager.get_property('bin_path'),
                    bin_config_manager.history_get('file_1')['bin_name']
                )]
            ),
            0
        )
        self.assertTrue(os.path.exists(file_1))
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
            0,
            msg="While restore, fail occupies."
        )

    def test_restore_with_folder(self):
        pass

    def test__move_from_bin(self):
        file_1 = os.path.join(self.test_folder_path, 'file_1')
        os.mknod(file_1)
        self.assertTrue(os.path.exists(file_1))
        delete_command.delete([file_1])
        self.assertFalse(os.path.exists(file_1))
        restore_command._move_from_bin([os.path.basename(file_1)])
        self.assertTrue(os.path.exists(file_1))
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
            0,
            msg="While restore, fail occupies."
        )

    def test__get_restore_paths(self):
        file_1 = os.path.join(self.test_folder_path, 'file_1')
        os.mknod(file_1)
        delete_command.delete([file_1])
        self.assertFalse(os.path.exists(file_1))
        self.assertTrue(os.path.exists(os.path.join(
            user_config_manager.get_property('bin_path'),
            os.path.basename(file_1)
        )))
        self.assertEqual(
            ['file_1'],
            restore_command._get_restore_paths([
                os.path.join(
                    user_config_manager.get_property('bin_path'),
                    'file_*'
                )
            ])
        )

    # def test_restore_with_file(self):
    #     file_1 = os.path.join(self.test_folder_path, 'file_1')
    #     os.mknod(file_1)
    #     restore_command.restore([file_1])
    #     self.assertEqual(
    #         restore_command.restore([file_1]),
    #         0,
    #         msg='Should return success code: 0.'
    #     )
    #     self.assertFalse(os.path.exists(file_1))
    #     self.assertTrue(
    #         os.path.exists(
    #             os.path.join(
    #                 user_config_manager.get_property('bin_path'),
    #                 'file_1'
    #             )
    #         )
    #     )
    #     self.assertEqual(
    #         bin_config_manager.history_get('file_1')['src_dir'],
    #         os.path.dirname(file_1)
    #     )


    # def test_restore_with_folder(self):
    #     pass
    #
    # def test__copy_to_bin(self):
    #     file_1 = os.path.join(self.test_folder_path, 'file_1')
    #     os.mknod(file_1)
    #     restore_command._copy_to_bin([file_1])
    #     self.assertTrue(
    #         os.path.exists(file_1),
    #         msg='Should not remove current file.'
    #     )
    #     self.assertEqual(
    #         bin_config_manager.history_get('file_1')['src_dir'],
    #         os.path.dirname(file_1),
    #         msg='Should copy file to bin.'
    #     )
    #     self.assertTrue(
    #         os.path.exists(os.path.join(user_config_manager.get_property('bin_path'), 'file_1')),
    #         msg='File should be coped to bin.'
    #     )
    #
    # def test__restore(self):
    #     file_1 = os.path.join(self.test_folder_path, 'file_1')
    #     os.mknod(file_1)
    #     restore_command._restore([file_1]),
    #     self.assertFalse(
    #         os.path.exists(file_1)
    #     )
    #
    # def test__get_del_paths(self):
    #     files = [os.path.join(self.test_folder_path, 'file_' + str(idx)) for idx in range(5)]
    #     for path in files:
    #         os.mknod(path)
    #     generated_list = sorted(restore_command._get_del_paths([os.path.join(self.test_folder_path, 'file_*')]))
    #     self.assertEqual(
    #         len(generated_list),
    #         5
    #     )
    #     for idx in range(5):
    #         self.assertEqual(
    #             generated_list[idx],
    #             files[idx]
    #         )
    #
    #
    # def move_bin(self):
    #     file_1 = os.path.join(self.test_folder_path, 'file_1')
    #     bin_move_path = os.path.join(self.test_folder_path, 'bin_move_path')
    #     os.mknod(file_1)
    #     bin_config_manager.history_add(file_1)
    #     clean_path.move(file_1, user_config_manager.get_property('bin_path'))
    #     self.assertEqual(
    #         1,
    #         0
    #     )
    #     self.assertFalse(
    #         os.path.exists(os.path.join(self.test_bin_path, 'file_1'))
    #     )
    #     self.assertTrue(
    #         os.path.exists(os.path.join(bin_move_path, 'file_1'))
    #     )
    #     self.assertEqual(
    #         user_config_manager.get_property('bin_path'),
    #         bin_move_path
    #     )
    #     self.assertEqual(
    #         len(bin_config_manager.get_property('history')),
    #         1
    #     )
