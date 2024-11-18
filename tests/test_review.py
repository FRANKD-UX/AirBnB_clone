#!/usr/bin/env python3

import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test cases for the Review class"""

    def test_instance(self):
        """Test that an instance of Review is created correctly"""
        review = Review()
        self.assertIsInstance(review, Review)
        self.assertIsInstance(review, BaseModel)

    def test_attributes(self):
        """Test that the Review class attributes are initialized correctly"""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_save(self):
        """Test that the save method works correctly"""
        review = Review()
        review.save()
        self.assertNotEqual(review.created_at, review.updated_at)


if __name__ == '__main__':
    unittest.main()
