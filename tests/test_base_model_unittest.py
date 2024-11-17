#!/usr/bin/env python3
"""Unit tests for BaseModel class"""

import unittest
from models.base_model import BaseModel
import time
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class"""

    def setUp(self):
        """Set up resources before each test"""
        self.model = BaseModel()

    def tearDown(self):
        """Clean up resources after each test"""
        del self.model

    def test_id_is_unique(self):
        """Test that id is unique for each instance"""
        model2 = BaseModel()
        self.assertNotEqual(self.model.id, model2.id)

    def test_created_at_is_datetime(self):
        """Test that created_at is a datetime object"""
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """Test that updated_at is a datetime object"""
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_save_updates_updated_at(self):
        """Test that save() updates the updated_at timestamp"""
        old_updated_at = self.model.updated_at
        time.sleep(0.1)  # Ensure timestamps differ
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)
        self.assertGreater(self.model.updated_at, old_updated_at)

    def test_to_dict_contains_correct_keys(self):
        """Test that to_dict() contains all expected keys"""
        model_dict = self.model.to_dict()
        expected_keys = ['id', 'created_at', 'updated_at', '__class__']
        for key in expected_keys:
            self.assertIn(key, model_dict)

    def test_to_dict_contains_correct_values(self):
        """Test that to_dict() contains correct values"""
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertEqual(
            model_dict['created_at'],
            self.model.created_at.isoformat()
        )
        self.assertEqual(
            model_dict['updated_at'],
            self.model.updated_at.isoformat()
        )


if __name__ == "__main__":
    unittest.main()
