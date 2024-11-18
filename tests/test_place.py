#!/usr/bin/env python3

import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Test cases for the Place class"""

    def test_instance(self):
        """Test that an instance of Place is created correctly"""
        place = Place()
        self.assertIsInstance(place, Place)
        self.assertIsInstance(place, BaseModel)

    def test_attributes(self):
        """Test that the Place class attributes are initialized correctly"""
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_save(self):
        """Test that the save method works correctly"""
        place = Place()
        place.save()
        self.assertNotEqual(place.created_at, place.updated_at)


if __name__ == '__main__':
    unittest.main()
