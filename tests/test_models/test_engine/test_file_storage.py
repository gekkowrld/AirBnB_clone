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

from models import storage
from models.base_model import BaseModel


class TestFileStorage_instantiation(unittest.TestCase):
    """Tests methods created in the FileStorage class"""

    def test_new(self):
        """Test whether an instance is added to objects dict"""
        bm1 = BaseModel()
        bm1_id = bm1.id

        my_dict = storage.all()
        self.assertIsInstance(my_dict, dict)

        obj = my_dict[f"{bm1.__class__.__name__}.{bm1_id}"]
        stored_id = obj.to_dict()["id"]

        self.assertEqual(stored_id, bm1_id)


class TestFileStorage_all(unittest.TestCase):
    """Test the all() method"""

    def test_key_value(self):
        """Test key value of all method"""
        bm1 = BaseModel()
        bm2 = BaseModel()

        my_dict = storage.all()

        for key, value in my_dict.items():
            my_list = key.split(".")
            self.assertEqual(my_list[0], value.__class__.__name__)
            obj_dict = value.to_dict()
            self.assertEqual(my_list[1], obj_dict["id"])


class TestFileStorage_save(unittest.TestCase):
    """Test the save method"""

    def test_file_creation(self):
        """Test for file creation"""
        bm1 = BaseModel()
        bm1_id = bm1.id

        bm1.save()

        my_objs = storage.all()
        obj = my_objs[f"{bm1.__class__.__name__}.{bm1_id}"]
        self.assertIsInstance(obj, BaseModel)

        self.assertEqual(obj.to_dict()["id"], bm1_id)

        bm1.age = 62
        my_objs = storage.all()
        obj = my_objs[f"{bm1.__class__.__name__}.{bm1_id}"]

        self.assertTrue(hasattr(obj, "age"))

    def test_new_obj(self):
        """Test creation of a new object"""

        bm1 = BaseModel()

        obj = storage.all()[f"{bm1.__class__.__name__}.{bm1.id}"]

        values = obj.to_dict()

        bm2 = BaseModel(**values)

        self.assertFalse(bm1 is bm2)
        self.assertEqual(bm1.id, bm2.id)


if __name__ == "__main__":
    unittest.main()
