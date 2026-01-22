#!/usr/bin/python3
"""
Unittest for User class
"""

import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Tests for User class"""

    def test_inheritance(self):
        u = User()
        self.assertTrue(hasattr(u, "id"))
        self.assertTrue(hasattr(u, "created_at"))
        self.assertTrue(hasattr(u, "updated_at"))

    def test_attributes(self):
        u = User()
        u.email = "test@example.com"
        u.first_name = "John"
        u.last_name = "Doe"
        u.password = "pass123"
        self.assertEqual(u.email, "test@example.com")
        self.assertEqual(u.first_name, "John")
        self.assertEqual(u.last_name, "Doe")
        self.assertEqual(u.password, "pass123")


if __name__ == "__main__":
    unittest.main()

