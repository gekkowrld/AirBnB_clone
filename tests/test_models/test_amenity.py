#!/usr/bin/python3
"""Unittests for amenity.py"""

from datetime import datetime
import unittest

from models.amenity import Amenity


class TestAmenity_instantiation(unittest.TestCase):
    """Test for instantation"""

    def test_id(self):
        """Tests for attr id"""
        a1 = Amenity()
        a2 = Amenity()

        self.assertIsInstance(a1, Amenity)
        self.assertTrue(hasattr(a1, "id"))
        self.assertNotEqual(a1.id, a2.id)
        self.assertIsInstance(a1.id, str)

    def test_created_at(self):
        """Tests created_at method"""
        a1 = Amenity()

        self.assertIsInstance(a1, Amenity)
        self.assertTrue(hasattr(a1, "created_at"))
        self.assertIsInstance(a1.created_at, datetime)

    def test_updated_at(self):
        """Tests updated_at attribute"""
        a1 = Amenity()

        self.assertIsInstance(a1, Amenity)
        self.assertTrue(hasattr(a1, "updated_at"))
        self.assertIsInstance(a1.created_at, datetime)

    def test_name(self):
        """Tests name attribute"""
        a1 = Amenity()

        self.assertIsInstance(a1, Amenity)
        self.assertTrue(hasattr(a1, "name"))
        self.assertIsInstance(a1.name, str)
        self.assertEqual(a1.name, "")

        a1.name = "Nairobi"

        self.assertEqual(a1.name, "Nairobi")


class TestAmenity_to_dict(unittest.TestCase):
    """Test to_dict() method in Parent class"""

    def check_values(self):
        """Checks the key, value pair of dict returned by to_dict()"""
        c1 = Amenity()

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
