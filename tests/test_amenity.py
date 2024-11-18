#!/usr/bin/python3
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def test_instance(self):
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

    def test_to_dict(self):
        amenity = Amenity()
        dict_repr = amenity.to_dict()
        self.assertIn('id', dict_repr)
        self.assertIn('created_at', dict_repr)
        self.assertIn('updated_at', dict_repr)


if __name__ == '__main__':
    unittest.main()
