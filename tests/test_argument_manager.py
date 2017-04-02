"""Argument Manager Test Case.

This module is a test case for module utils.managers.argument_manager.
Should be tested:
* def parse_arguments()
* def add_optional_arguments()
* def add_positional_arguments()
* def get_options()

Example:
    write 'python setup.py -t' in terminal.

Test Module is not finished.

"""
import unittest
import os
import setup
import shutil
import sys

from utils.managers import user_config_manager, app_config_manager, bin_config_manager
from utils.managers import argument_manager
from utils.commands import delete_command


class Args(object):
    def __init__(self, binmove, bincopy, bincreate, binempty, restore):
        self.binmove = binmove
        self.bincopy = bincopy
        self.bincreate = bincreate
        self.binempty = binempty
        self.restore = restore


class ArgumentManagerTestCase(unittest.TestCase):
    def setUp(self):
        self.real_argv = sys.argv
        sys.argv = [os.path.basename(__file__)]

    def tearDown(self):
        sys.argv = self.real_argv

    def test_parse_arguments_with_binempty(self):
        sys.argv += ['--binempty']
        self.assertEqual(
            argument_manager.parse_arguments(),
            [[], {'mods': ['binempty']}]
        )

    def test_parse_arguments_with_bincreate(self):
        sys.argv += ['--bincreate=.']
        self.assertEqual(
            argument_manager.parse_arguments(),
            [[], {'mods': ['bincreate'], 'path': '.'}]
        )

    def test_parse_arguments_with_empty_argv(self):
        files_path = '../path_to_files/..'
        sys.argv += [files_path]
        self.assertEqual(
            argument_manager.parse_arguments(),
            [[files_path], {'mods': ['remove']}]
        )

    def test_get_options_with_bincopy(self):
        copy_path = '.'
        arguments = Args(False, copy_path, False, False, False)
        options = argument_manager._get_options(arguments)
        self.assertEqual(options['mods'][0], 'bincopy')
        self.assertEqual(options['path'], copy_path)

    def test_get_options_with_restore(self):
        copy_path = '.'
        arguments = Args(False, False, False, False, True)
        options = argument_manager._get_options(arguments)
        self.assertEqual(options['mods'][0], 'restore')
        self.assertEqual(len(options['mods']), 1)

    def test_get_options_with_several_mods(self):
        copy_path = '.'
        arguments = Args('/move_path', '/copy_path', '/create_path', True, True)
        options = argument_manager._get_options(arguments)
        self.assertEqual(options['mods'][0], 'binmove')
        self.assertEqual(options['path'], '/move_path')
        self.assertEqual(len(options['mods']), 1)

    def test_get_options_with_empty_arguments(self):
        arguments = Args(None, None, None, None, None)
        self.assertEqual(
            argument_manager._get_options(arguments),
            {'mods': ['remove']}
        )
