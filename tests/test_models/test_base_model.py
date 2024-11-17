#!/usr/bin/env python3

import unittest
from models.base_model import BaseModel
import datetime
import time


class TestBaseModel(unittest.TestCase):
    """Unit tests for the BaseModel class"""

    def setUp(self):
        """Set up a fresh instance for testing"""
        self.model = BaseModel()

    def test_id_is_string(self):
        """Test that id is a string"""
        self.assertIsInstance(self.model.id, str)

    def test_created_at_is_datetime(self):
        """Test that created_at is a datetime object"""
        self.assertIsInstance(self.model.created_at, datetime.datetime)

    def test_updated_at_is_datetime(self):
        """Test that updated_at is a datetime object"""
        self.assertIsInstance(self.model.updated_at, datetime.datetime)

    def test_to_dict_creates_dict(self):
        """Test the to_dict method generates a dictionary
        with correct fields"""
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

        # Check for all keys
        expected_keys = {'id', 'created_at', 'updated_at', '__class__'}
        self.assertTrue(expected_keys.issubset(model_dict.keys()))

    def test_save_updates_updated_at(self):
        """Test the save method updates updated_at"""
        old_updated_at = self.model.updated_at
        time.sleep(0.01)  # Ensure time difference for comparison
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)
        self.assertGreater(self.model.updated_at, old_updated_at)

    def test_invalid_attribute(self):
        """Test assigning an invalid attribute type raises an error"""
        with self.assertRaises(TypeError):
            self.model.created_at = "invalid_type"


if __name__ == '__main__':
    unittest.main()
