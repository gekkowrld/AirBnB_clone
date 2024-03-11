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

from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class TestFileStorage_instantiation(unittest.TestCase):
    """Tests methods created in the FileStorage class"""

    def test_file_path_if_private(self):
        """Checks whether the __file_path attr is private"""
        f1 = FileStorage()

        self.assertIsInstance(f1, FileStorage)
        self.assertFalse(hasattr(f1, "__file_path"))

    def test_file_path(self):
        """Test the class attr __file_path"""
        f1 = FileStorage()

        f1._FileStorage__file_path = "my_file.json"

        self.assertIsInstance(f1, FileStorage)
        self.assertIsNotNone(f1._FileStorage__file_path)
        self.assertIsInstance(f1._FileStorage__file_path, str)
        self.assertEqual(f1._FileStorage__file_path, "my_file.json")

    def test_objects_if_private(self):
        """Checks whether the __objects attr is private"""
        f1 = FileStorage()

        self.assertIsInstance(f1, FileStorage)
        self.assertFalse(hasattr(f1, "__objects"))

        f1._FileStorage__objects = None
        self.assertEqual(f1._FileStorage__objects, None)

    def test_object(self):
        """Test the class attr __objects"""
        import os

        f1 = FileStorage()

        if os.path.exists(f1._FileStorage__file_path):
            os.remove(f1._FileStorage__file_path)

        self.assertIsInstance(f1, FileStorage)
        self.assertIsInstance(f1._FileStorage__objects, dict)
        self.assertEqual(f1._FileStorage__objects, {})

        b1 = BaseModel()

        f1.new(b1)

        self.assertNotEqual(f1._FileStorage__objects, {})
        self.assertIsInstance(f1._FileStorage__objects, dict)


class TestFileStorage_all(unittest.TestCase):
    """Test the method all()"""

    def test_empty_objects(self):
        """Tests case when no self.__objects is empty"""
        import os

        f1 = FileStorage()

        if os.path.exists(f1._FileStorage__file_path):
            os.remove(f1._FileStorage__file_path)

        my_dict = f1.all()

        self.assertIsInstance(f1, FileStorage)
        self.assertIsInstance(my_dict, dict)
        self.assertEqual(my_dict, {})

    def test_non_empty_objects(self):
        """Tests case when self.__objects is not empty"""
        f1 = FileStorage()

        b1 = BaseModel()

        b1_key = f"{b1.__class__.__name__}.{b1.id}"

        f1.new(b1)

        my_dict = f1.all()

        self.assertNotEqual(my_dict, {})
        self.assertIn(b1_key, my_dict)
        self.assertEqual(b1, my_dict[b1_key])


class TestFileStorage_new(unittest.TestCase):
    """Test the new method"""

    def test_BaseModel(self):
        """Test whether an obj is added"""
        f1 = FileStorage()

        b1 = BaseModel()

        b1_key = f"{b1.__class__.__name__}.{b1.id}"

        f1.new(b1)

        my_dict = f1.all()

        self.assertNotEqual(my_dict, {})
        self.assertIn(b1_key, my_dict)
        self.assertEqual(b1, my_dict[b1_key])

    def test_Amenity(self):
        """Test whether an Amenity instance is added"""
        f1 = FileStorage()

        a1 = Amenity()

        a1_key = f"{a1.__class__.__name__}.{a1.id}"

        f1.new(a1)

        my_dict = f1.all()

        self.assertNotEqual(my_dict, {})
        self.assertIn(a1_key, my_dict)
        self.assertEqual(a1, my_dict[a1_key])

    def test_State(self):
        """Test whether an obj is added"""
        f1 = FileStorage()

        s1 = State()

        s1_key = f"{s1.__class__.__name__}.{s1.id}"

        f1.new(s1)

        my_dict = f1.all()

        self.assertNotEqual(my_dict, {})
        self.assertIn(s1_key, my_dict)
        self.assertEqual(s1, my_dict[s1_key])

    def test_User(self):
        """Test whether a User instance is added"""
        f1 = FileStorage()

        u1 = User()

        u1_key = f"{u1.__class__.__name__}.{u1.id}"

        f1.new(u1)

        my_dict = f1.all()

        self.assertNotEqual(my_dict, {})
        self.assertIn(u1_key, my_dict)
        self.assertEqual(u1, my_dict[u1_key])

    def test_City(self):
        """Test whether City Instance is added"""
        f1 = FileStorage()
        c1 = City()

        c1_key = f"{c1.__class__.__name__}.{c1.id}"

        f1.new(c1)

        my_dict = f1.all()

        self.assertNotEqual(my_dict, {})
        self.assertIn(c1_key, my_dict)
        self.assertEqual(c1, my_dict[c1_key])

    def test_Review(self):
        """Test whether City Instance is added"""
        f1 = FileStorage()
        r1 = Review()

        r1_key = f"{r1.__class__.__name__}.{r1.id}"

        f1.new(r1)

        my_dict = f1.all()

        self.assertNotEqual(my_dict, {})
        self.assertIn(r1_key, my_dict)
        self.assertEqual(r1, my_dict[r1_key])

    def test_Place(self):
        """Test whether Place Instance is added"""
        f1 = FileStorage()
        p1 = Place()

        p1_key = f"{p1.__class__.__name__}.{p1.id}"

        f1.new(p1)

        my_dict = f1.all()

        self.assertNotEqual(my_dict, {})
        self.assertIn(p1_key, my_dict)
        self.assertEqual(p1, my_dict[p1_key])


class TestFileStorage_save(unittest.TestCase):
    """Tests the save method"""

    def test_file_content(self):
        """Tests the content of our file"""
        import json
        import os

        f1 = FileStorage()

        if os.path.exists(f1._FileStorage__file_path):
            os.remove(f1._FileStorage__file_path)

        b1 = BaseModel()
        u1 = User()

        f1.new(b1)
        f1.new(u1)

        f1.save()

        with open(f1._FileStorage__file_path, "r", encoding="UTF-8") as fo:
            content = fo.read()

        self.assertIsInstance(content, str)

        obj_dict = json.loads(content)

        self.assertIsInstance(obj_dict, dict)

        b1_key = f"{b1.__class__.__name__}.{b1.id}"
        u1_key = f"{u1.__class__.__name__}.{u1.id}"

        self.assertIn(b1_key, obj_dict)
        self.assertIn(u1_key, obj_dict)


class TestFileStorage_reload(unittest.TestCase):
    """Tests the reload method"""

    def test_reload_file_exists(self):
        """Test if obj is created from file when file exists"""
        import os

        f1 = FileStorage()

        if os.path.exists(FileStorage()._FileStorage__file_path):
            os.remove(FileStorage()._FileStorage__file_path)

        content = (
            '{"BaseModel.15495279-5c36-40ee-b8a5-1a7bf333e8d8": '
            '{"id": "15495279-5c36-40ee-b8a5-1a7bf333e8d8", "created_at": "2024-03-11T18:08:11.572045", '
            '"updated_at": "2024-03-11T18:08:11.572045", "__class__": "BaseModel"} '
        )
        key = "BaseModel.15495279-5c36-40ee-b8a5-1a7bf333e8d8"

        with open(
            FileStorage()._FileStorage__file_path, "w", encoding="UTF-8"
        ) as fo:
            fo.write(content)



        print(f1.all())


if __name__ == "__main__":
    unittest.main()
