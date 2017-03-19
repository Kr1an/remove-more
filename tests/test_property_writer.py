""" Property Writer Unit Tests.

This module is a test case for module utils.helpers.property_writer.
It test functionality of:
    * def set_property().
    * def set_property_from_json().

Example:
    write 'python setup.py -t' in terminal.

Attributes:
    TEST_FILE_PATH: file with json 'some' mock date for tests.

Test Module is finished.
Find particular test class or test in is's name(title).

"""
import unittest

import os
from utils.helpers.property_writer import *
from utils.helpers.property_reader import *

TEST_FILE_PATH = \
    os.path.abspath(
        os.path.join(
            __file__,
            '..',
            'mock',
            'test_property_reader.json'
        )
    )


class PropertyWriterTestCase(unittest.TestCase):
    def setUp(self):
        try:
            with open(TEST_FILE_PATH, 'r') as json_file:
                self.obj_dict = json.load(json_file)
        except Exception as e:
            print(e)
        self.obj_json = json.dumps(self.obj_dict)

    def check_property_for_dict(self, value, search_query, sup='.'):
        self.obj_after_change = set_property(
            self.obj_dict,
            search_query,
            value,
            sup
        )

        return False if self.obj_after_change is None else get_property(
            self.obj_after_change,
            search_query,
            sup) is value

    def check_property_for_json(self, value, search_query, sup='.'):
        self.obj_after_change = set_property_from_json(
            self.obj_json,
            search_query,
            value,
            sup
        )

        return False if self.obj_after_change is None else get_property_from_json(
            self.obj_after_change,
            search_query,
            sup
        ) == value

    def test_check_if_json_data_exists(self):
        self.assertEqual(
            len(self.obj_json),
            586,
            msg="Test date is not valid."
        )

        self.assertEqual(
            len(self.obj_dict),
            6,
            msg="Test date is not valid"
        )

    def test_set_property_with_valid_parameters(self):

        self.assertTrue(
            self.check_property_for_dict('string test value', 'place_id'),
            msg="place_id != 'string test value'. query-height = 1."
        )
        self.assertTrue(
            self.check_property_for_dict(12, 'geometry.location.lat'),
            msg="geometry.location.lat.4!=12. query-height = 3."
        )

    def test_set_property_from_json_with_valid_parameters(self):
        self.assertTrue(
            self.check_property_for_json('string test value', 'place_id'),
            msg="place_id != 'string test value'. query-height = 1."
        )
        self.assertTrue(
            self.check_property_for_json(12, 'geometry.location.lat'),
            msg="geometry.location.lat.4!=12. query-height = 3."
        )

    def test_set_property_with_invalid_parameters(self):
        self.assertFalse(
            self.check_property_for_dict('string test value', 'place_pk'),
            msg="Should be false with invalid params. query-height = 1."
        )
        self.assertFalse(
            self.check_property_for_dict(12, 'geometry.location.lat.value'),
            msg="geometry.location.lat.4!=12. query-height = 4."
        )

    def test_set_property_from_json_with_invalid_parameters(self):
        self.assertFalse(
            self.check_property_for_json('string test value', 'place_pk'),
            msg="Should be false with invalid params. query-height = 1."
        )
        self.assertFalse(
            self.check_property_for_json(12, 'geometry.location.lat.value'),
            msg="geometry.location.lat.4!=12. query-height = 4."
        )

    def test_set_property_with_empty_parameters(self):
        self.assertFalse(
            self.check_property_for_dict(None, 'place_id'),
            msg="value->empty. should return 'None'"
        )
        self.assertFalse(
            self.check_property_for_dict('some value', None),
            msg="search_query->empty. should return 'None'"
        )
        self.assertTrue(
            self.check_property_for_dict(True, 'geometry bounds', None),
            msg="sup->empty. should use default sup=' '(Space) to sep s_query."
        )
        self.assertFalse(
            self.check_property_for_dict(True, 'geometry.bounds', None),
            msg="sup->empty. should use default sup=' '(Space) to sep s_query."
        )

        self.obj_dict = None
        self.assertFalse(
            self.check_property_for_dict(True, 'geometry.bounds', None),
            msg="sup->empty. should use default sup=' '(Space) to sep s_query."
        )

    def test_set_property_from_json_with_empty_parameters(self):
        self.assertFalse(
            self.check_property_for_json(None, 'place_id'),
            msg="value->empty. should return 'None'"
        )
        self.assertFalse(
            self.check_property_for_json('some value', None),
            msg="search_query->empty. should return 'None'"
        )
        self.assertTrue(
            self.check_property_for_json(True, 'geometry bounds', None),
            msg="sup->empty. should use default sup=' '(Space) to sep s_query."
        )
        self.assertFalse(
            self.check_property_for_json(True, 'geometry.bounds', None),
            msg="sup->empty. should use default sup=' '(Space) to sep s_query."
        )

        self.obj_json = None
        self.assertFalse(
            self.check_property_for_json(True, 'geometry.bounds', None),
            msg="sup->empty. should use default sup=' '(Space) to sep s_query."
        )

    def test_set_property_with_wrong_type_parameters(self):
        self.assertFalse(
            self.check_property_for_dict(-1, 'geometry.bounds', None),
            msg="sup->empty. should use default sup=' '(Space) to sep s_query."
        )
        self.assertFalse(
            self.check_property_for_dict(True, [], None),
            msg="Wrong type of 'search_query' parameter: search_query==[]"
        )
        self.assertFalse(
            self.check_property_for_dict(True, 'place_id', -1),
            msg="Wrong type of 'sup' parameter: sup==-1."
        )

    def test_set_property_from_json_with_wrong_type_parameters(self):
        self.assertFalse(
            self.check_property_for_json(-1, 'geometry.bounds', None),
            msg="sup->empty. should use default sup=' '(Space) to sep s_query."
        )
        self.assertFalse(
            self.check_property_for_json(True, [], None),
            msg="Wrong type of 'search_query' parameter: search_query==[]"
        )
        self.assertFalse(
            self.check_property_for_json(True, 'place_id', -1),
            msg="Wrong type of 'sup' parameter: sup==-1."
        )
