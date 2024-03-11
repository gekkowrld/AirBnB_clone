#!/usr/bin/python3
"""Unittests for review.py"""

import unittest
from datetime import datetime

from models.review import Review


class TestReview_instantiation(unittest.TestCase):
    """Test for instantation"""

    def test_id(self):
        r1 = Review()
        r2 = Review()

        self.assertIsInstance(r1, Review)
        self.assertTrue(hasattr(r1, "id"))
        self.assertNotEqual(r1.id, r2.id)
        self.assertIsInstance(r1.id, str)

    def test_created_at(self):
        """Tests created_at method"""
        r1 = Review()

        self.assertIsInstance(r1, Review)
        self.assertTrue(hasattr(r1, "created_at"))
        self.assertIsInstance(r1.created_at, datetime)

    def test_updated_at(self):
        """Tests updated_at attribute"""
        r1 = Review()

        self.assertIsInstance(r1, Review)
        self.assertTrue(hasattr(r1, "updated_at"))
        self.assertIsInstance(r1.created_at, datetime)

    def test_place_id(self):
        """Tests place_id attribute"""
        r1 = Review()

        self.assertIsInstance(r1, Review)
        self.assertTrue(hasattr(r1, "place_id"))
        self.assertIsInstance(r1.place_id, str)
        self.assertEqual(r1.place_id, "")

    def test_user_id(self):
        """Tests user_id attribute"""
        r1 = Review()

        self.assertIsInstance(r1, Review)
        self.assertTrue(hasattr(r1, "user_id"))
        self.assertIsInstance(r1.user_id, str)
        self.assertEqual(r1.user_id, "")

    def test_user_id(self):
        """Tests user_id attribute"""
        r1 = Review()

        self.assertIsInstance(r1, Review)
        self.assertTrue(hasattr(r1, "text"))
        self.assertIsInstance(r1.text, str)
        self.assertEqual(r1.text, "")


class TestReview_to_dict(unittest.TestCase):
    """Test to_dict() method in Parent class"""

    def check_values(self):
        """Checks the key, value pair of dict returned by to_dict()"""
        c1 = Review()

        my_list = [
            "id",
            "__class__",
            "updated_at",
            "created_at",
        ]

        my_dict = c1.to_dict()

        for key in my_list:
            if key == "updated_at" or key == "created_at":
                value = my_dict[key]
                self.assertIsInstance(value, str)
            self.assertIn(key, my_dict)


if __name__ == "__main__":
    unittest.main()
