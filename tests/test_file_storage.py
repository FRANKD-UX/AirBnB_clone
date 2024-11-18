#!/usr/bin/python3
import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def test_save_and_reload(self):
        storage = FileStorage()
        obj = SomeObject()  # Replace with an actual object
        storage.new(obj)
        storage.save()

        # Assuming FileStorage reloads objects from the file
        storage.reload()

        # Check if the object is correctly reloaded
        all_objects = storage.all()
        self.assertIn(obj.id, all_objects)


if __name__ == '__main__':
    unittest.main()
