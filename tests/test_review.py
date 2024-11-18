#!/usr/bin/env python3

from models.review import Review
mport unittest


class TestReview(unittest.TestCase):

    def test_save(self):
        """Test that the save method works correctly"""
        review = Review()
        prev_updated_at = review.updated_at
        review.save()
        self.assertNotEqual(prev_updated_at, review.updated_at)

    def test_invalid_attribute(self):
        """Test invalid attribute types"""
        review = Review()
        with self.assertRaises(TypeError):
            review.created_at = "invalid_type"  # Should raise TypeError
