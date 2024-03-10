#!/usr/bin/python3
"""Unittests for place.py"""

from datetime import datetime
import unittest

from models.place import Place


class TestPlace_instantiation(unittest.TestCase):
    """Test for instantation"""

    def test_id(self):
        """Tests the id"""
        p1 = Place()
        p2 = Place()

        self.assertIsInstance(p1, Place)
        self.assertTrue(hasattr(p1, "id"))
        self.assertNotEqual(p1.id, p2.id)
        self.assertIsInstance(p1.id, str)

    def test_created_at(self):
        """Tests created_at method"""
        p1 = Place()

        self.assertIsInstance(p1, Place)
        self.assertTrue(hasattr(p1, "created_at"))
        self.assertIsInstance(p1.created_at, datetime)

    def test_updated_at(self):
        """Tests updated_at attribute"""
        p1 = Place()

        self.assertIsInstance(p1, Place)
        self.assertTrue(hasattr(p1, "updated_at"))
        self.assertIsInstance(p1.created_at, datetime)

    def test_name(self):
        """Tests name attribute"""
        p1 = Place()

        self.assertIsInstance(p1, Place)
        self.assertTrue(hasattr(p1, "name"))
        self.assertIsInstance(p1.name, str)
        self.assertEqual(p1.name, "")

        p1.name = "Nairobi"

        self.assertEqual(p1.name, "Nairobi")

    def test_city_id(self):
        """Test public class attr city_id"""
        p1 = Place()

        self.assertIsInstance(p1, Place)
        self.assertTrue(hasattr(p1, "city_id"))
        self.assertIsInstance(p1.city_id, str)
        self.assertEqual(p1.city_id, "")

    def test_user_id(self):
        """Test public class attr user_id"""
        p1 = Place()

        self.assertIsInstance(p1, Place)
        self.assertTrue(hasattr(p1, "user_id"))
        self.assertIsInstance(p1.user_id, str)
        self.assertEqual(p1.user_id, "")

    def test_user_id(self):
        """Test public class attr user_id"""
        p1 = Place()

        self.assertIsInstance(p1, Place)
        self.assertTrue(hasattr(p1, "user_id"))
        self.assertIsInstance(p1.user_id, str)
        self.assertEqual(p1.user_id, "")

    def test_description(self):
        """Test public class attr description"""
        p1 = Place()

        self.assertIsInstance(p1, Place)
        self.assertTrue(hasattr(p1, "description"))
        self.assertIsInstance(p1.description, str)
        self.assertEqual(p1.description, "")

    def test_number_rooms(self):
        """Test public class attr number_rooms"""
        p1 = Place()

        self.assertIsInstance(p1, Place)
        self.assertTrue(hasattr(p1, "number_rooms"))
        self.assertIsInstance(p1.number_rooms, int)
        self.assertEqual(p1.number_rooms, 0)

    def test_number_bathrooms(self):
        """Test public class attr number_bathrooms"""
        p1 = Place()

        self.assertIsInstance(p1, Place)
        self.assertTrue(hasattr(p1, "number_bathrooms"))
        self.assertIsInstance(p1.number_bathrooms, int)
        self.assertEqual(p1.number_bathrooms, 0)

    def test_max_guest(self):
        """Test public class attr number_bathrooms"""
        p1 = Place()

        self.assertIsInstance(p1, Place)
        self.assertTrue(hasattr(p1, "max_guest"))
        self.assertIsInstance(p1.max_guest, int)
        self.assertEqual(p1.max_guest, 0)

    def test_price_by_night(self):
        """Test public class attr number_bathrooms"""
        p1 = Place()

        self.assertIsInstance(p1, Place)
        self.assertTrue(hasattr(p1, "price_by_night"))
        self.assertIsInstance(p1.price_by_night, int)
        self.assertEqual(p1.price_by_night, 0)

    def test_latitude(self):
        """Test public class attr number_bathrooms"""
        p1 = Place()

        self.assertIsInstance(p1, Place)
        self.assertTrue(hasattr(p1, "latitude"))
        self.assertIsInstance(p1.latitude, float)
        self.assertEqual(p1.latitude, 0.0)

    def test_longitude(self):
        """Test public class attr number_bathrooms"""
        p1 = Place()

        self.assertIsInstance(p1, Place)
        self.assertTrue(hasattr(p1, "longitude"))
        self.assertIsInstance(p1.longitude, float)
        self.assertEqual(p1.longitude, 0.0)

    def test_amenity_ids(self):
        """Test public class attr number_bathrooms"""
        p1 = Place()

        self.assertIsInstance(p1, Place)
        self.assertTrue(hasattr(p1, "amenity_ids"))
        self.assertIsInstance(p1.amenity_ids, list)
        self.assertEqual(p1.amenity_ids, [])


class TestPlace_to_dict(unittest.TestCase):
    """Test to_dict() method in Parent class"""

    def check_values(self):
        """Check the key value pair return by to_dict()"""
        c1 = Place()

        my_list = [
            "id",
            "__class__",
            "updated_at",
            "created_at",
            "name",
        ]

        my_dict = c1.to_dict()

        for key in my_list:
            if key == "updated_at" or key == "created_at":
                value = my_dict[key]
                self.assertIsInstance(value, str)
            self.assertIn(key, my_dict)


if __name__ == "__main__":
    unittest.main()
