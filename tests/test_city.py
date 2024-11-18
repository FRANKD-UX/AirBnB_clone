#!/usr/bin/env python3

from models.amenity import Amenity
import unittest


class TestAmenity(unittest.TestCase):

    def test_save(self):
        """Test that the save method works correctly"""
        amenity = Amenity()
        prev_updated_at = amenity.updated_at
        amenity.save()
        self.assertNotEqual(prev_updated_at, amenity.updated_at)

    def test_invalid_attribute(self):
        """Test invalid attribute types"""
        amenity = Amenity()
        with self.assertRaises(TypeError):
            amenity.created_at = "invalid_type"  # Should raise TypeError
