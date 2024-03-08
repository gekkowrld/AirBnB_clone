#!/usr/bin/python3
"""
Unittest for models.base_model module
Unittest classes:
    TestBaseModel_instantiation - line 18
    TestBaseModel_str - line 67
    TestBaseModel_save - line 82
    TestBaseModel_to_dict - line 95
"""

import unittest
import uuid
from datetime import datetime

from models.base_model import BaseModel


class TestBaseModel_instantiation(unittest.TestCase):
    """class to test the BaseModel"""

    def test_uuid(self):
        """Test the id of an instance"""
        bm1 = BaseModel()
        bm2 = BaseModel()

        self.assertIsInstance(bm1, BaseModel)
        self.assertTrue(hasattr(bm1, "id"))
        self.assertNotEqual(bm1.id, bm2.id)
        self.assertIsInstance(bm1.id, str)

    def test_my_number(self):
        """Test my_number attribute"""
        bm1 = BaseModel()
        bm1.my_number = 69

        self.assertTrue(hasattr(bm1, "my_number"))
        self.assertEqual(bm1.my_number, 69)
        self.assertIsInstance(bm1.my_number, int)

    def test_name(self):
        """Test for name attribute"""
        bm1 = BaseModel()

        bm1.name = "Python"
        self.assertTrue(hasattr(bm1, "name"))
        self.assertIsInstance(bm1.name, str)

    def test_created_at(self):
        """Test the created_at attribute"""
        bm1 = BaseModel()

        self.assertTrue(hasattr(bm1, "created_at"))
        self.assertIsInstance(bm1.created_at, datetime)
        self.assertEqual(bm1.created_at, bm1.updated_at)

    def test_updated_at(self):
        """Test the updated_at attribute"""
        bm1 = BaseModel()

        self.assertTrue(hasattr(bm1, "updated_at"))
        self.assertIsInstance(bm1.updated_at, datetime)
        self.assertEqual(bm1.created_at, bm1.updated_at)

        bm1.save()

        self.assertNotEqual(bm1.updated_at, bm1.created_at)


class TestBaseModel_str(unittest.TestCase):
    """Unittest for the __str__() method"""

    def test_str(self):
        """Compare the result of __str__() method with instance attributes"""
        bm1 = BaseModel()

        self.assertIsInstance(bm1.__str__(), str)

        test_str = "[{}] ({}) {}".format(
            bm1.__class__.__name__, bm1.id, bm1.__dict__
        )
        self.assertEqual(bm1.__str__(), test_str)


class TestBaseModel_save(unittest.TestCase):
    """Unittest for save() method of BaseModel"""

    def test_save(self):
        """Tests whether updated_at works as expected"""
        bm1 = BaseModel()

        curr_update_time = bm1.updated_at
        bm1.save()

        self.assertNotEqual(bm1.updated_at, curr_update_time)


class TestBaseModel_to_dict(unittest.TestCase):
    """Unittest for the to_dict() method"""

    def test_to_dict_instance(self):
        """Test the to_dict method"""
        bm1 = BaseModel()

        self.assertIsInstance(bm1.__dict__, dict)

    def test_to_dict_values(self):
        """Test if all the keys are in the dict"""
        bm1 = BaseModel()
        bm1.name = "Python"
        bm1.my_number = 69

        my_list = [
            "id",
            "my_number",
            "__class__",
            "updated_at",
            "created_at",
            "name",
        ]
        my_dict = bm1.to_dict()

        for key in my_list:
            if key == "updated_at" or key == "created_at":
                value = my_dict[key]
                self.assertIsInstance(value, str)
            self.assertIn(key, my_dict)


if __name__ == "__main__":
    unittest.main()
