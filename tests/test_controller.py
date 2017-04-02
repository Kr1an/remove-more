""" Controller Unit Tests.

It is close to e2e tests because it tests functionality via
terminal scripts, as real user would do.

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

from utils.managers import user_config_manager, app_config_manager, bin_config_manager

TEST_FOLDER_PATH = os.path.abspath(
    os.path.join(
        __file__,
        '..',
        'mock',
        'mock_folder_for_controller_test_case'
    )
)

TEST_BIN_PATH = os.path.abspath(
    os.path.join(
        TEST_FOLDER_PATH,
        'bin'
    )
)

CONTROLLER_PATH = os.path.abspath(
    'controller.py'
)


class ControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.test_folder_path = TEST_FOLDER_PATH
        self.test_bin_path = TEST_BIN_PATH
        self.real_bin_path = user_config_manager.get_property('bin_path')
        self.real_bin_history = bin_config_manager.get_property('history')
        user_config_manager.set_property('bin_path', self.test_bin_path)
        bin_config_manager.set_property('history', [])
        os.mkdir(self.test_folder_path)
        os.mkdir(self.test_bin_path)

        self.real_location = os.getcwd()
        os.chdir(self.test_folder_path)

    def tearDown(self):

        shutil.rmtree(self.test_folder_path)
        user_config_manager.set_property('bin_path', self.real_bin_path)
        bin_config_manager.set_property('history', self.real_bin_history)
        os.chdir(self.real_location)

    def get_script(self, arguments):
        return 'python %s %s' % (
            CONTROLLER_PATH,
            arguments
        )

    def test_controller_scenario_with_deleting_file(self):
        file_1 = os.path.join(self.test_folder_path, 'file_1')
        os.mknod(file_1)

        self.assertEqual(os.system(self.get_script('%s' % os.path.basename(file_1))), 0)
        self.assertFalse(os.path.exists(file_1))
        self.assertTrue(os.path.exists(
            os.path.join(
                user_config_manager.get_property('bin_path'),
                os.path.basename(file_1)
            )
        ))

    def test_controller_scenario_with_binempty(self):
        file_1 = os.path.join(self.test_folder_path, 'file_1')
        os.mknod(file_1)

        self.assertEqual(os.system(self.get_script('%s' % os.path.basename(file_1))), 0)
        self.assertEqual(os.system(self.get_script('--binempty')), 0)
        self.assertEqual(len(bin_config_manager.get_property('history')), 0)
        self.assertFalse(os.path.exists(file_1))
        self.assertFalse(os.path.exists(
            os.path.join(
                user_config_manager.get_property('bin_path'),
                os.path.basename(file_1)
            )
        ))

    def test_controller_scenario_with_restoring_file(self):
        file_1 = os.path.join(self.test_folder_path, 'file_1')
        os.mknod(file_1)

        self.assertEqual(os.system(self.get_script('%s' % os.path.basename(file_1))), 0)
        self.assertEqual(len(bin_config_manager.get_property('history')), 1)
        os.chdir(os.path.basename(self.test_bin_path))
        self.assertFalse(os.path.exists(file_1))
        self.assertEqual(os.system(self.get_script('%s --restore' % os.path.basename(file_1))), 0)
        self.assertEqual(len(bin_config_manager.get_property('history')), 0)

        self.assertTrue(os.path.exists(file_1))
        self.assertFalse(os.path.exists(
            os.path.join(
                user_config_manager.get_property('bin_path'),
                os.path.basename(file_1)
            )
        ))

    def test_controller_scenario_with_restoring_file(self):
        file_1 = os.path.join(self.test_folder_path, 'file_1')
        os.mknod(file_1)

        self.assertEqual(os.system(self.get_script('%s' % os.path.basename(file_1))), 0)
        self.assertEqual(len(bin_config_manager.get_property('history')), 1)
        os.chdir(os.path.basename(self.test_bin_path))
        self.assertFalse(os.path.exists(file_1))
        self.assertEqual(os.system(self.get_script('%s --restore' % os.path.basename(file_1))), 0)
        self.assertEqual(len(bin_config_manager.get_property('history')), 0)

        self.assertTrue(os.path.exists(file_1))
        self.assertFalse(os.path.exists(
            os.path.join(
                user_config_manager.get_property('bin_path'),
                os.path.basename(file_1)
            )
        ))