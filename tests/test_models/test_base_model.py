#!/usr/bin/python3
"""Unit test for BaseModel"""

import unittest
from models.base_model import BaseModel
from datetime import datetime
import time


class TestBaseModel(unittest.TestCase):
    """Tests for BaseModel"""

    def test_init(self):
        """Test initialization of BaseModel"""
        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)

    def test_to_dict(self):
        """Test to_dict method"""
        instance = BaseModel()
        instance_dict = instance.to_dict()
        self.assertEqual(instance_dict["__class__"], "BaseModel")
        self.assertIsInstance(instance_dict["created_at"], str)
        self.assertIsInstance(instance_dict["updated_at"], str)

    def test_str_representation(self):
        """Test string representation"""
        instance = BaseModel()
        string = str(instance)
        self.assertIn("[BaseModel]", string)
        self.assertIn(f"({instance.id})", string)
        self.assertIn(str(instance.__dict__), string)

    def test_updated_at_changes(self):
        """Test that updated_at updates on save"""
        instance = BaseModel()
        original_updated_at = instance.updated_at
        time.sleep(0.1)  # Ensure time difference
        instance.save()
        self.assertNotEqual(original_updated_at, instance.updated_at)
        self.assertGreater(instance.updated_at, original_updated_at)


if __name__ == "__main__":
    unittest.main()
