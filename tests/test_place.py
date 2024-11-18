#!/usr/bin/env python3

import unittest
from models.place import Place


class TestPlace(unittest.TestCase):

    def test_save(self):
        """Test that the save method works correctly"""
        place = Place()
        prev_updated_at = place.updated_at
        place.save()
        self.assertNotEqual(prev_updated_at, place.updated_at)

    def test_invalid_attribute(self):
        """Test invalid attribute types"""
        place = Place()
        with self.assertRaises(TypeError):
            place.created_at = "invalid_type"  # Should raise TypeError
