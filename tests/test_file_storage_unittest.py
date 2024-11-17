#!/usr/bin/env python3
"""Unit tests for FileStorage class"""

import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class"""

    def setUp(self):
        """Set up resources before each test"""
        self.storage = FileStorage()
        self.file_path = "file.json"
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def tearDown(self):
        """Clean up resources after each test"""
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all_returns_dict(self):
        """Test that all() returns a dictionary"""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new_adds_object(self):
        """Test that new() adds an object to storage"""
        model = BaseModel()
        self.storage.new(model)
        key = f"{model.__class__.__name__}.{model.id}"
        self.assertIn(key, self.storage.all())

    def test_save_creates_file(self):
        """Test that save() creates a file"""
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))

    def test_reload_loads_objects(self):
        """Test that reload() loads objects from file"""
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        self.storage.reload()
        key = f"{model.__class__.__name__}.{model.id}"
        self.assertIn(key, self.storage.all())


if __name__ == "__main__":
    unittest.main()
