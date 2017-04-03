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
import sys

from utils.managers import user_config_manager, app_config_manager, bin_config_manager
from utils.commands import bin_command

from contextlib import contextmanager
from StringIO import StringIO

from setting.DEFAULT_CONFIGS import ERROR_MESSAGES


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



@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err



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

    def test_controller_scenario_with_deleting_folder(self):
        dir_1 = os.path.join(self.test_folder_path, 'dir_1')
        file_1 = os.path.join(dir_1, 'file_1')
        os.mkdir(dir_1)
        os.mknod(file_1)

        self.assertEqual(os.system(self.get_script('%s' % os.path.basename(dir_1))), 0)
        self.assertFalse(os.path.exists(file_1))
        self.assertFalse(os.path.exists(dir_1))
        self.assertTrue(os.path.exists(
            os.path.join(
                user_config_manager.get_property('bin_path'),
                os.path.basename(dir_1)
            )
        ))
        self.assertEqual(
            bin_config_manager.history_get(os.path.basename(dir_1))['src_dir'],
            os.path.dirname(dir_1)
        )

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

    def test_controller_scenario_with_restoring_folder(self):
        dir_1 = os.path.join(self.test_folder_path, 'dir_1')
        file_1 = os.path.join(dir_1, 'file_1')
        os.mkdir(dir_1)
        os.mknod(file_1)

        self.assertEqual(os.system(self.get_script('%s' % os.path.basename(dir_1))), 0)
        self.assertEqual(len(bin_config_manager.get_property('history')), 1)
        os.chdir(os.path.basename(self.test_bin_path))
        self.assertFalse(os.path.exists(file_1))
        self.assertFalse(os.path.exists(dir_1))
        self.assertTrue(os.path.exists(
            os.path.join(
                user_config_manager.get_property('bin_path'),
                bin_config_manager.history_get(os.path.basename(dir_1))['bin_name']
            )
        ))
        self.assertTrue(os.path.exists(
            os.path.join(
                user_config_manager.get_property('bin_path'),
                bin_config_manager.history_get(os.path.basename(dir_1))['bin_name'],
                os.path.basename(file_1)
            )
        ))

        self.assertEqual(os.system(self.get_script('%s --restore' % os.path.basename(dir_1))), 0)
        self.assertEqual(len(bin_config_manager.get_property('history')), 0)

        self.assertTrue(os.path.exists(file_1))
        self.assertTrue(os.path.exists(dir_1))
        self.assertFalse(os.path.exists(
            os.path.join(
                user_config_manager.get_property('bin_path'), os.path.basename(dir_1)
            )
        ))
        self.assertFalse(os.path.exists(
            os.path.join(
                user_config_manager.get_property('bin_path'),
                os.path.basename(dir_1),
                os.path.basename(file_1)
            )
        ))

    def test_controller_scenario_with_moving_bin(self):
        file_1 = os.path.join(self.test_folder_path, 'file_1')
        new_rel_bin_path = 'bin/../new_bin'
        os.mknod(file_1)
        self.assertEqual(os.system(self.get_script('%s' % os.path.basename(file_1))), 0)
        self.assertEqual(os.system(self.get_script('--binmove=%s' % new_rel_bin_path)), 0)

        self.assertEqual(len(bin_config_manager.get_property('history')), 1)
        self.assertEqual(
            os.path.abspath(new_rel_bin_path),
            user_config_manager.get_property('bin_path')
        )
        self.assertEqual(
            bin_config_manager.history_get(os.path.basename(file_1))['src_dir'],
            os.path.dirname(file_1)
        )
        self.assertTrue(os.path.exists(
            os.path.join(
                user_config_manager.get_property('bin_path'),
                os.path.basename(file_1)
            )
        ))

    def test_controller_scenario_with_copy_bin(self):
        file_1 = os.path.join(self.test_folder_path, 'file_1')
        copy_rel_bin_path = 'bin/../bin_copy_1'
        os.mknod(file_1)
        self.assertEqual(os.system(self.get_script('%s' % os.path.basename(file_1))), 0)
        self.assertEqual(os.system(self.get_script('--bincopy=%s' % copy_rel_bin_path)), 0)

        self.assertEqual(len(bin_config_manager.get_property('history')), 1)
        self.assertEqual(
            os.path.abspath(self.test_bin_path),
            user_config_manager.get_property('bin_path')
        )
        self.assertEqual(
            bin_config_manager.history_get(os.path.basename(file_1))['src_dir'],
            os.path.dirname(file_1)
        )
        self.assertTrue(os.path.exists(
            os.path.join(
                user_config_manager.get_property('bin_path'),
                os.path.basename(file_1)
            )
        ))

    def test_controller_scenario_with_creating_bin(self):
        file_1 = os.path.join(self.test_folder_path, 'file_1')
        new_rel_bin_path = 'bin/../new_bin'
        os.mknod(file_1)
        self.assertEqual(os.system(self.get_script('%s' % os.path.basename(file_1))), 0)
        self.assertEqual(os.system(self.get_script('--bincreate=%s' % new_rel_bin_path)), 0)

        self.assertEqual(len(bin_config_manager.get_property('history')), 0)
        self.assertEqual(
            os.path.abspath(new_rel_bin_path),
            user_config_manager.get_property('bin_path')
        )
        self.assertFalse(os.path.exists(
            os.path.join(
                user_config_manager.get_property('bin_path'),
                os.path.basename(file_1)
            )
        ))

    def test_controller_scenario_with_regex_delete_file(self):
        file_1 = os.path.join(self.test_folder_path, 'file_1')
        file_3 = os.path.join(self.test_folder_path, 'file_3')
        file_2 = os.path.join(self.test_folder_path, 'file_2')
        os.mknod(file_1)
        os.mknod(file_2)
        os.mknod(file_3)
        self.assertEqual(os.system(self.get_script('--regex=./file_*')), 0)

        self.assertEqual(len(bin_config_manager.get_property('history')), 3)
        self.assertFalse(os.path.exists(file_1) or os.path.exists(file_2) or os.path.exists(file_3))
        self.assertTrue(os.path.isfile(os.path.join(
            user_config_manager.get_property('bin_path'),
            os.path.basename(file_3)
        )))

    def test_controller_scenario_with_regex_delete_file_within_folder(self):
        dir_1 = os.path.join(self.test_folder_path, 'dir_1')
        file_1 = os.path.join(dir_1, 'file_1')
        file_3 = os.path.join(dir_1, 'file_3')
        file_2 = os.path.join(dir_1, 'file_2')

        os.mkdir(dir_1)
        os.mknod(file_1)
        os.mknod(file_2)
        os.mknod(file_3)

        self.assertEqual(os.system(self.get_script('--regex=dir_1/file_*')), 0)

        self.assertEqual(len(bin_config_manager.get_property('history')), 3)
        self.assertFalse(os.path.exists(file_1) or os.path.exists(file_2) or os.path.exists(file_3))
        self.assertEqual(
            bin_config_manager.history_get(os.path.basename(file_1))['src_dir'],
            os.path.dirname(file_1)
        )
        self.assertEqual(
            bin_config_manager.history_get(os.path.basename(file_2))[
                'src_dir'],
            os.path.dirname(file_2)
        )
        self.assertEqual(
            bin_config_manager.history_get(os.path.basename(file_3))[
                'src_dir'],
            os.path.dirname(file_3)
        )

    def test_controller_scenario_with_regex_delete_folders(self):
        dir_1 = os.path.join(self.test_folder_path, 'dir_1')
        dir_3 = os.path.join(self.test_folder_path, 'dir_3')
        dir_2 = os.path.join(self.test_folder_path, 'dir_2')
        os.mkdir(dir_1)
        os.mkdir(dir_2)
        os.mkdir(dir_3)
        self.assertEqual(os.system(self.get_script('--regex=./dir_*')), 0)

        self.assertEqual(len(bin_config_manager.get_property('history')), 3)
        self.assertFalse(os.path.exists(dir_1) or os.path.exists(dir_2) or os.path.exists(dir_3))
        self.assertTrue(os.path.isdir(os.path.join(
            user_config_manager.get_property('bin_path'),
            os.path.basename(dir_1)
        )))
        self.assertTrue(os.path.isdir(os.path.join(
            user_config_manager.get_property('bin_path'),
            os.path.basename(dir_2)
        )))
        self.assertTrue(os.path.isdir(os.path.join(
            user_config_manager.get_property('bin_path'),
            os.path.basename(dir_3)
        )))

    def test_controller_scenario_with_regex_delete_folders(self):
        dir_1 = os.path.join(self.test_folder_path, 'dir_1')
        dir_2 = os.path.join(dir_1, 'dir_2')
        dir_3 = os.path.join(dir_2, 'dir_3')
        file_1 = os.path.join(dir_1, 'file_1')
        file_2 = os.path.join(dir_2, 'file_2')
        file_3 = os.path.join(dir_3, 'file_3')
        os.mkdir(dir_1)
        os.mkdir(dir_2)
        os.mkdir(dir_3)
        os.mknod(file_1)
        os.mknod(file_2)
        os.mknod(file_3)
        self.assertEqual(os.system(self.get_script('--regex=./dir_1/**/file_*')), 0)

        self.assertEqual(len(bin_config_manager.get_property('history')), 3)
        self.assertTrue(os.path.exists(dir_1) and os.path.exists(dir_2) and os.path.exists(dir_3))
        self.assertTrue(os.path.isfile(os.path.join(
            user_config_manager.get_property('bin_path'),
            os.path.basename(file_1)
        )))
        self.assertTrue(os.path.isfile(os.path.join(
            user_config_manager.get_property('bin_path'),
            os.path.basename(file_2)
        )))
        self.assertTrue(os.path.isfile(os.path.join(
            user_config_manager.get_property('bin_path'),
            os.path.basename(file_3)
        )))

    def test_controller_with_binprint_option(self):
        file_1 = os.path.join(self.test_folder_path, 'file_1')
        file_3 = os.path.join(self.test_folder_path, 'file_3')
        file_2 = os.path.join(self.test_folder_path, 'file_2')
        os.mknod(file_1)
        os.mknod(file_2)
        os.mknod(file_3)
        self.assertEqual(os.system(self.get_script('--regex=./file_*')), 0)

        with captured_output() as (out, err):
            self.assertEqual(bin_command.print_bin(None), 0)

        output = out.getvalue().strip()

        history_list = bin_config_manager.get_property('history')
        for history_item in history_list:
            self.assertTrue(
                history_item['bin_name'] in output,
                msg="Does not print all file info."
            )
