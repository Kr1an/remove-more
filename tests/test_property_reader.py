import unittest

import os
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


class PropertyReaderTestCase(unittest.TestCase):
    def setUp(self):
        try:
            with open(TEST_FILE_PATH, 'r') as json_file:
                self.obj_dict = json.load(json_file)
        except Exception as e:
            print(e)
        self.obj_json = json.dumps(self.obj_dict)

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

    def test_get_property_with_valid_parameters(self):
        self.assertEqual(
            len(get_property(self.obj_dict, 'address_components')),
            1,
            msg="Should return valid value. Query height = 1. Result != 1"
        )
        self.assertAlmostEqual(
            get_property(self.obj_dict, 'geometry.bounds.northeast.lat'),
            17,
            delta=0.5,
            msg="Should return valid value. Query height = 4 . Result != 1"
        )

    def test_get_property_from_json_with_valid_parameters(self):
        self.assertEqual(
            len(get_property_from_json(self.obj_json, 'address_components')),
            1,
            msg="Should return valid value. Query height = 1. Result != 1"
        )
        self.assertAlmostEqual(
            get_property_from_json(
                self.obj_json,
                'geometry.bounds.northeast.lat'
            ),
            17,
            delta=0.5,
            msg="Should return valid value. Query height = 4 . Result != 1"
        )

    def test_get_property_with_invalid_parameters(self):
        self.assertEqual(
            get_property(self.obj_dict, 'partial_place'),
            None,
            msg="Query height = 1. Should return <None> if prop doesn't exist."
        )
        self.assertEqual(
            get_property(self.obj_dict, 'location_type.type1'),
            None,
            msg="Query height > 1. Should return <None> if prop doesn't exist."
        )

    def test_get_property_from_json_with_invalid_parameters(self):
        self.assertEqual(
            get_property_from_json(self.obj_json, 'partial_place'),
            None,
            msg="Query height = 1. Should return <None> if prop doesn't exist."
        )
        self.assertEqual(
            get_property_from_json(self.obj_json, 'location_type.type1'),
            None,
            msg="Query height > 1. Should return <None> if prop doesn't exist."
        )

    def test_get_property_with_empty_parameters(self):
        self.assertEqual(
            get_property(None, 'some_param'),
            None,
            msg="With invalid params should return <None>. obj!=None."
        )
        self.assertEqual(
            get_property(self.obj_dict, ''),
            None,
            msg="With empty search query should return <None>. obj!=None."
        )
        self.assertEqual(
            get_property(self.obj_dict, None),
            None,
            msg="With <None> in search query should return <None>. obj!=None."
        )
        self.assertEqual(
            get_property(self.obj_dict, 'formatted_address', None),
            'Honduras',
            msg="Should work if sep == <None>. Use value: ' '(Space)."
        )

    def test_get_property_from_json_with_empty_parameters(self):
        self.assertEqual(
            get_property_from_json(None, 'some_param'),
            None,
            msg="With invalid params should return <None>. obj!=None."
        )
        self.assertEqual(
            get_property_from_json(self.obj_json, ''),
            None,
            msg="With empty search query should return <None>. obj!=None."
        )
        self.assertEqual(
            get_property_from_json(self.obj_json, None),
            None,
            msg="With <None> in search query should return <None>. obj!=None."
        )
        self.assertEqual(
            get_property_from_json(self.obj_json, 'formatted_address', None),
            'Honduras',
            msg="Should work if sep == <None>. Use value: ' '(Space)."
        )

    def test_get_property_with_wrong_type_parameters(self):
        self.assertEqual(
            get_property(-1, 'formatted_address'),
            None,
            msg="Should return <None> if some parameter is wrong type."
        )
        self.assertEqual(
            get_property({}, True),
            None,
            msg="Should return <None> if some parameter is wrong type."
        )
        self.assertEqual(
            get_property({}, '', 34.23),
            None,
            msg="Should return <None> if some parameter is wrong type."
        )

    def test_get_property_from_json_with_wrong_type_parameters(self):
        self.assertEqual(
            get_property_from_json(-1, 'formatted_address'),
            None,
            msg="Should return <None> if some parameter is wrong type."
        )
        self.assertEqual(
            get_property_from_json(None, True),
            None,
            msg="Should return <None> if some parameter is wrong type."
        )
        self.assertEqual(
            get_property_from_json([], '', 34.23),
            None,
            msg="Should return <None> if some parameter is wrong type."
        )
