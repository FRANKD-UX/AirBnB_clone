#!/usr/bin/env python3

import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test cases for the State class"""

    def test_instance(self):
        """Test that an instance of State is created correctly"""
        state = State()
        self.assertIsInstance(state, State)
        self.assertIsInstance(state, BaseModel)

    def test_attribute(self):
        """Test that the name attribute is initialized as an empty string"""
        state = State()
        self.assertEqual(state.name, "")

    def test_save(self):
        """Test that the save method works correctly"""
        state = State()
        state.save()
        self.assertNotEqual(state.created_at, state.updated_at)


if __name__ == '__main__':
    unittest.main()
