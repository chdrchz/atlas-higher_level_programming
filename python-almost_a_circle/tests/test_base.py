#!/usr/bin/python3
import unittest
import os
from models.base import Base
from unittest.mock import patch
from io import StringIO


class TestBaseMethods(unittest.TestCase):

    def test_init(self):
        obj1 = Base()
        self.assertEqual(obj1.id, 1)

        obj2 = Base()
        self.assertEqual(obj2.id, 2)

        obj3 = Base(100)
        self.assertEqual(obj3.id, 100)

    def test_to_json_string(self):
        obj = Base(1)
        obj_dict = obj.to_dictionary()
        json_string = Base.to_json_string([obj_dict])
        self.assertEqual(json_string, '[{"id": 1}]')

    def test_save_to_file(self):
        obj1 = Base(1)
        obj2 = Base(2)
        Base.save_to_file([obj1, obj2])

        with open("Base.json", "r") as file:
            content = file.read()
            self.assertEqual(content, '[{"id": 1}, {"id": 2}]')

        # Clean up
        os.remove("Base.json")

    def test_from_json_string(self):
        json_string = '[{"id": 1}, {"id": 2}]'
        obj_list = Base.from_json_string(json_string)
        self.assertEqual(len(obj_list), 2)
        self.assertEqual(obj_list[0].id, 1)
        self.assertEqual(obj_list[1].id, 2)

    def test_create(self):
        obj_dict = {"id": 1}
        obj = Base.create(**obj_dict)
        self.assertEqual(obj.id, 1)

    def test_load_from_file(self):
        obj1 = Base(1)
        obj2 = Base(2)
        Base.save_to_file([obj1, obj2])

        loaded_objs = Base.load_from_file()
        self.assertEqual(len(loaded_objs), 2)
        self.assertEqual(loaded_objs[0].id, 1)
        self.assertEqual(loaded_objs[1].id, 2)

        # Clean up
        os.remove("Base.json")

    def test_load_from_file_missing_file(self):
        loaded_objs = Base.load_from_file()
        self.assertEqual(len(loaded_objs), 0)

if __name__ == '__main__':
    unittest.main()