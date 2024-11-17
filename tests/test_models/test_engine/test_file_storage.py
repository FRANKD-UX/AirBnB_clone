#!/usr/bin/python3
"""Unit test for FileStorage"""

import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()
        self.model = BaseModel()

    def test_all_returns_dict(self):
        self.assertIsInstance(self.storage.all(), dict)

    def test_new_adds_instance(self):
        self.storage.new(self.model)
        key = f"BaseModel.{self.model.id}"
        self.assertIn(key, self.storage.all())

    def test_save_creates_file(self):
        self.storage.new(self.model)
        self.storage.save()
        with open(self.storage._FileStorage__file_path, 'r') as f:
            content = f.read()
            self.assertIn(self.model.id, content)


if __name__ == '__main__':
    unittest.main()
