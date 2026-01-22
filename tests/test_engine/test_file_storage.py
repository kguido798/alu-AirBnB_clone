#!/usr/bin/python3
"""
Unittest for FileStorage class
"""

import unittest
import os
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User


class TestFileStorage(unittest.TestCase):
    """Tests for FileStorage class"""

    def setUp(self):
        """Remove file.json if exists before each test"""
        self.fs = FileStorage()
        if os.path.exists("file.json"):
            os.remove("file.json")
        self.fs._FileStorage__objects = {}

    def test_all_and_new(self):
        bm = BaseModel()
        self.fs.new(bm)
        self.assertIn(f"BaseModel.{bm.id}", self.fs.all())

    def test_save_creates_file(self):
        bm = BaseModel()
        self.fs.new(bm)
        self.fs.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload_restores_objects(self):
        bm = BaseModel()
        self.fs.new(bm)
        self.fs.save()
        self.fs._FileStorage__objects = {}
        self.fs.reload()
        key = f"BaseModel.{bm.id}"
        self.assertIn(key, self.fs.all())
        self.assertEqual(self.fs.all()[key].id, bm.id)

    def test_reload_no_file(self):
        self.fs._FileStorage__objects = {}
        try:
            self.fs.reload()
        except Exception as e:
            self.fail(f"reload() raised {type(e).__name__} unexpectedly!")


if __name__ == "__main__":
    unittest.main()

