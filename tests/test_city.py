#!/usr/bin/env python3

import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test cases for the City class"""

    def test_instance(self):
        """Test that an instance of City is created correctly"""
        city = City()
        self.assertIsInstance(city, City)
        self.assertIsInstance(city, BaseModel)

    def test_attributes(self):
        """Test that the city_id and name attributes are initialized"""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_save(self):
        """Test that the save method works correctly"""
        city = City()
        city.save()
        self.assertNotEqual(city.created_at, city.updated_at)


if __name__ == '__main__':
    unittest.main()
