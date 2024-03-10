#!/usr/bin/python3
"""Unittests for user.py"""

import unittest

from models.user import User


class TestUser_instantiation(unittest.TestCase):
    """Tests for instantiation"""
    def test_id(self):
        u1 = User()
        u2 = User()

        self.assertIsInstance(u1, User)
        self.assertTrue(hasattr(u1, "id"))
        self.assertNotEqual(u1.id, u2.id)
        self.assertIsInstance(u1.id, str)

    def test_email(self):
        u1 = User()

        self.assertIsInstance(u1, User)
        self.assertTrue(hasattr(u1, "email"))
        self.assertIsInstance(u1.email, str)

        my_email = "myemail@gmail.com"

        u1.email = my_email

        stored_email = u1.to_dict()['email']

        self.assertEqual(stored_email, my_email)

    def test_first_name(self):
        u1 = User()

        self.assertIsInstance(u1, User)
        self.assertTrue(hasattr(u1, "first_name"))
        self.assertIsInstance(u1.first_name, str)

        my_name = "John"
        u1.first_name = my_name

        u1_first_name = u1.to_dict()['first_name']

        self.assertEqual(u1_first_name, my_name)

    def test_last_name(self):
        """Tests the last_name public attribute"""
        u1 = User()

        self.assertIsInstance(u1, User)
        self.assertTrue(hasattr(u1, "last_name"))
        self.assertIsInstance(u1.last_name, str)

        my_name = "John"
        u1.last_name = my_name

        u1_last_name = u1.to_dict()['last_name']

        self.assertEqual(u1_last_name, my_name)

    def test_password(self):
        """Tests the password public attribute"""
        u1 = User()

        self.assertIsInstance(u1, User)
        self.assertTrue(hasattr(u1, "password"))
        self.assertIsInstance(u1.password, str)

        my_password = "Hq123U"
        u1.password = my_password

        u1_password = u1.to_dict()['password']

        self.assertEqual(u1_password, my_password)


class TestUser_to_dict(unittest.TestCase):
    """Test to_dict() method in Parent class"""

    def check_values(self):
        u1 = User()

        my_list = [
            "id",
            "password",
            "__class__",
            "updated_at",
            "created_at",
            "email",
            "password",
            "first_name",
            "last_name"
        ]
        my_dict = u1.to_dict()

        for key in my_list:
            if key == "updated_at" or key == "created_at":
                value = my_dict[key]
                self.assertIsInstance(value, str)
            self.assertIn(key, my_dict)

if __name__ == "__main__":
    unittest.main()
