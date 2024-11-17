#!/usr/bin/python3
"""Unit test for BaseModel"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Tests for BaseModel"""

    def test_init(self):
        """Test initialization of BaseModel"""
        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime)

    def test_to_dict(self):
        """Test to_dict method"""
        instance = BaseModel()
        instance_dict = instance.to_dict()
        self.assertEqual(instance_dict["__class__"], "BaseModel")
        self.assertIsInstance(instance_dict["created_at"], str)
        self.assertIsInstance(instance_dict["updated_at"], str)


if __name__ == "__main__":
    unittest.main()
