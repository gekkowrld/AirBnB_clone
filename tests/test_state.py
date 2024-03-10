#!/usr/bin/python3
"""Unittests for state.py"""

import unittest
from datetime import datetime

from models.state import State


class TestState_instantiation(unittest.TestCase):
    """Tests for instantiation"""

    def test_id(self):
        """Test if id value is correct"""
        s1 = State()
        s2 = State()

        self.assertIsInstance(s1, State)
        self.assertTrue(hasattr(s1, "id"))
        self.assertNotEqual(s1.id, s2.id)
        self.assertIsInstance(s1.id, str)

    def test_created_at(self):
        """Tests created_at method"""
        s1 = State()

        self.assertIsInstance(s1, State)
        self.assertTrue(hasattr(s1, "created_at"))
        self.assertIsInstance(s1.created_at, datetime)

    def test_updated_at(self):
        """Tests updated_at attribute"""
        s1 = State()

        self.assertIsInstance(s1, State)
        self.assertTrue(hasattr(s1, "updated_at"))
        self.assertIsInstance(s1.created_at, datetime)

    def test_name(self):
        """Tests name attribute"""
        s1 = State()

        self.assertIsInstance(s1, State)
        self.assertTrue(hasattr(s1, "name"))

        state_name = "Alaska"
        s1.name = state_name

        stored_state_name = s1.__dict__["name"]

        self.assertEqual(state_name, stored_state_name)


class TestState_to_dict(unittest.TestCase):
    """Test to_dict() method in Parent class"""

    def check_values(self):
        """Check the values returned"""
        s1 = State()

        my_list = [
            "id",
            "__class__",
            "updated_at",
            "created_at",
            "name",
        ]

        my_dict = s1.to_dict()

        for key in my_list:
            if key in {"updated_at", "created_at"}:
                value = my_dict[key]
                self.assertIsInstance(value, str)
            self.assertIn(key, my_dict)


if __name__ == "__main__":
    unittest.main()
