#!/usr/bin/env python3
"""Unit tests for README.md"""

import os
import unittest


class TestReadme(unittest.TestCase):
    """Test cases for README.md"""

    def test_readme_exists(self):
        """Test that README.md file exists"""
        self.assertTrue(os.path.exists("README.md"))

    def test_readme_not_empty(self):
        """Test that README.md file is not empty"""
        with open("README.md", "r") as file:
            content = file.read()
            self.assertGreater(len(content), 0)


if __name__ == "__main__":
    unittest.main()
