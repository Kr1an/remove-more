""" Setup Unit Tests.

This module is a test case for module utils.helpers.property_writer.
It test functionality of:
    * def test().
    * def setup().
    * def install().
    * def remove().

Example:
    write 'python setup.py -t' in terminal.

Test Module is not finished finished.

"""
import unittest
import os
import setup


class SetupTestCase(unittest.TestCase):
    def setUp(self):
        self.scripts = {
            'is_installed': 'cat ~/.bashrc | grep remove-more/utils/controller >> /dev/null',
            'install':
                'echo "alias .../remove-more/utils/controller.py" >> ~/.bashrc'
        }

    def test_install_function(self):
        setup.remove()
        self.assertEqual(
            os.system(self.scripts['is_installed']),
            256,
            msg="Preparing script does not work as expected."
        )
        setup.install()
        self.assertEqual(
            os.system(self.scripts['is_installed']),
            0,
            msg="Script should be in file already."
        )
        setup.remove()

    def test_remove_function(self):
        if os.system(self.scripts['is_installed']) is 256:
            os.system(self.scripts['install'])
        self.assertEqual(
            os.system(self.scripts['is_installed']),
            0,
            msg="Preparing script does not work as expected."
        )

        setup.remove()

        self.assertEqual(
            os.system(self.scripts['is_installed']),
            256,
            msg="Script should be removed now"
        )
