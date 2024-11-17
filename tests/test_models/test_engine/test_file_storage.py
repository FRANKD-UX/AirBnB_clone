#!/usr/bin/python3
"""Unit test for FileStorage"""

import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Tests for FileStorage"""

    def setUp(self):
        """Set up test environment"""
        self.storage = FileStorage()
        self.obj = BaseModel()
        self.storage.new(self.obj)

    def tearDown(self):
        """Clean up test environment"""
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all(self):
        """Test all method returns the correct objects dictionary"""
        all_objects = self.storage.all()
        key = (
            f"BaseModel.{self.obj.id}"
        )  # Ensures the line does not exceed 79 characters
        self.assertIn(key, all_objects)
        self.assertEqual(all_objects[key], self.obj)

    def test_new(self):
        """Test new method sets the correct key-value pair"""
        key = (
            f"BaseModel.{self.obj.id}"
        )  # Ensures the line does not exceed 79 characters
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key], self.obj)

    def test_save_and_reload(self):
        """Test save and reload methods"""
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))

        # Create a new FileStorage instance to ensure objects are reloaded
        new_storage = FileStorage()
        new_storage.reload()
        key = (
            f"BaseModel.{self.obj.id}"
        )  # Ensures the line does not exceed 79 characters
        self.assertIn(key, new_storage.all())
        self.assertEqual(new_storage.all()[key].to_dict(), self.obj.to_dict())


if __name__ == "__main__":
    unittest.main()
