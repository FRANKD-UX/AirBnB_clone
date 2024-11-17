#!/usr/bin/env python3

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    Unit tests for the BaseModel class.
    """

    def setUp(self):
        """
        Set up the test environment.
        Create an instance of BaseModel for testing.
        """
        self.model = BaseModel()

    def test_save_updates_updated_at(self):
        """
        Test the save method updates the updated_at attribute correctly.
        """
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(self.model.updated_at, old_updated_at)
        self.assertTrue(isinstance(self.model.updated_at, datetime))

    def test_to_dict_creates_dict_with_correct_keys(self):
        """
        Test that the to_dict method creates
        a dictionary with the correct keys.
        """
        dict_rep = self.model.to_dict()
        self.assertEqual(dict_rep['__class__'], 'BaseModel')
        self.assertTrue('id' in dict_rep)
        self.assertTrue('created_at' in dict_rep)
        self.assertTrue('updated_at' in dict_rep)

    def test_invalid_attribute(self):
        """
        Test assigning an invalid attribute type raises an error.
        """
        with self.assertRaises(TypeError):
            self.model.created_at = "invalid_type"


if __name__ == '__main__':
    unittest.main()
