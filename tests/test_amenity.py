#!/usr/bin/env python3

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class"""

    def test_instance(self):
        """Test that an instance of Amenity is created correctly"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)
        self.assertIsInstance(amenity, BaseModel)

    def test_attribute(self):
        """Test that the name attribute is initialized as an empty string"""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_save(self):
        """Test that the save method works correctly"""
        amenity = Amenity()
        amenity.save()
        self.assertNotEqual(amenity.created_at, amenity.updated_at)


if __name__ == '__main__':
    unittest.main()
