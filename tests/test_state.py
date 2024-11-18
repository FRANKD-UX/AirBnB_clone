#!/usr/bin/env python3

from models.state import State
mport unittest


class TestState(unittest.TestCase):

    def test_save(self):
        """Test that the save method works correctly"""
        state = State()
        prev_updated_at = state.updated_at
        state.save()
        self.assertNotEqual(prev_updated_at, state.updated_at)

    def test_invalid_attribute(self):
        """Test invalid attribute types"""
        state = State()
        with self.assertRaises(TypeError):
            state.created_at = "invalid_type"  # Should raise TypeError
