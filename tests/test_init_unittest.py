#!/usr/bin/env python3
"""Unit tests for models/__init__.py"""

import unittest
from models import storage
from models.engine.file_storage import FileStorage


class TestModelsInit(unittest.TestCase):
    """Test cases for models/__init__.py"""

    def test_storage_instance(self):
        """Test that storage is an instance of FileStorage"""
        self.assertIsInstance(storage, FileStorage)


if __name__ == "__main__":
    unittest.main()
