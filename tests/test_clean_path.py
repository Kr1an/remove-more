"""Clean Path Unit Tests.

This module is a test case for module utils.helpers.clean_path.
It tests functionality of:
    * def move().
    * def delete().
    * def copy().

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

TEST_FOLDER_PATH = \
    os.path.abspath(
        os.path.join(
            __file__,
            '..',
            'mock',
            'mock_folder_for_clean_path_module_test'
        )
    )


class CleanPathTestCase(unittest.TestCase):
    def setUp(self):
        self.test_folder_path = TEST_FOLDER_PATH
        os.mkdir(self.test_folder_path)

    def tearDown(self):
        shutil.rmtree(self.test_folder_path)

    def test_delete_with_file(self):
        test_file_1 = os.path.join(self.test_folder_path, 'test_file_1')
        os.mknod(test_file_1)
        self.assertTrue(
            os.path.exists(test_file_1),
            msg="Function test_delete_with_file fails while preparation."
                "Test file does not exists."
        )
        self.assertEqual(
            clean_path.delete(test_file_1),
            0,
            msg="Function clean_path.delete returns fail code."
        )
        self.assertFalse(
            os.path.exists(test_file_1),
            msg="Function test_delete_with_file fails to delete file."
        )

    def test_delete_with_folder(self):
        test_dir_1 = os.path.join(self.test_folder_path, 'test_dir_1')
        test_file_1 = os.path.join(test_dir_1, 'test_file_1')
        os.mkdir(test_dir_1)
        os.mknod(test_file_1)
        self.assertTrue(
            os.path.exists(test_dir_1),
            msg="Function test_delete_with_folder fails while preparation."
                "Test folder does not exists."
        )
        self.assertTrue(
            os.path.exists(test_file_1),
            msg="Function test_delete_with_file fails while preparation."
                "Test file does not exists."
        )
        self.assertEqual(
            clean_path.delete(test_dir_1),
            0,
            msg="Function clean_path.delete returns fail code."
        )
        self.assertFalse(
            os.path.exists(test_dir_1),
            msg="Function test_delete_with_folder fails to delete folder."
        )
        self.assertFalse(
            os.path.exists(test_file_1),
            msg="Function test_delete_with_folder"
                " fails to delete file with in folder."
        )

    def test_copy_with_file(self):
        test_dir_dest = os.path.join(self.test_folder_path, 'test_dir_1')
        test_file_1 = os.path.join(self.test_folder_path, 'test_file_1')
        os.mkdir(test_dir_dest)
        os.mknod(test_file_1)

        self.assertEqual(
            clean_path.copy(test_file_1, test_dir_dest),
            0,
            "Copy function should return success code: 0."
        )
        self.assertTrue(
            os.path.exists(test_file_1),
            msg="Copy should not remove current location file."
        )
        self.assertTrue(
            os.path.exists(os.path.join(test_dir_dest, os.path.basename(test_file_1))),
            msg="Copy should create file in dest location."
        )

    def test_copy_with_folder(self):
        dest_dir = os.path.join(self.test_folder_path, 'dest_dir')
        os.mkdir(dest_dir)
        dir_1 = os.path.join(self.test_folder_path, 'dir_1')
        os.mkdir(dir_1)
        file_1 = os.path.join(dir_1, 'file_1')
        os.mknod(file_1)

        dir_1_after_copy = os.path.join(dest_dir, 'dir_1_after_copy')

        self.assertEqual(
            clean_path.copy(dir_1, dir_1_after_copy),
            0,
            "Copy function should return success code: 0."
        )
        self.assertTrue(
            os.path.exists(file_1),
            msg="Copy should not remove current location file."
        )
        self.assertTrue(
            os.path.exists(os.path.join(dir_1_after_copy, os.path.basename(file_1))),
            msg="Copy should create file in dest location."
        )

    def test_move_with_file(self):
        test_dir_dest = os.path.join(self.test_folder_path, 'test_dir_1')
        test_file_1 = os.path.join(self.test_folder_path, 'test_file_1')
        os.mkdir(test_dir_dest)
        os.mknod(test_file_1)

        self.assertEqual(
            clean_path.move(test_file_1, test_dir_dest),
            0,
            "Move function should return success code: 0."
        )
        self.assertFalse(
            os.path.exists(test_file_1),
            msg="Move should remove current location file."
        )
        self.assertTrue(
            os.path.exists(
                os.path.join(test_dir_dest, os.path.basename(test_file_1))),
            msg="Move should create file in dest location."
        )

    def test_move_with_folder(self):
        dest_dir = os.path.join(self.test_folder_path, 'dest_dir')
        os.mkdir(dest_dir)
        dir_1 = os.path.join(self.test_folder_path, 'dir_1')
        os.mkdir(dir_1)
        file_1 = os.path.join(dir_1, 'file_1')
        os.mknod(file_1)

        dir_1_after_move = os.path.join(dest_dir, 'dir_1_after_move')

        self.assertEqual(
            clean_path.move(dir_1, dir_1_after_move),
            0,
            "Move function should return success code: 0."
        )
        self.assertFalse(
            os.path.exists(file_1),
            msg="Move should remove current location file."
        )
        self.assertTrue(
            os.path.exists(
                os.path.join(dir_1_after_move, os.path.basename(file_1))),
            msg="Move should create file in dest location."
        )