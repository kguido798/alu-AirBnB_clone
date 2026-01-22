#!/usr/bin/python3
"""
Unittest for BaseModel class
"""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Tests for BaseModel"""

    def test_id_and_datetime(self):
        bm = BaseModel()
        self.assertIsInstance(bm.id, str)
        self.assertIsInstance(bm.created_at, datetime)
        self.assertIsInstance(bm.updated_at, datetime)

    def test_str_method(self):
        bm = BaseModel()
        s = str(bm)
        self.assertIn("[BaseModel]", s)
        self.assertIn(bm.id, s)

    def test_save_updates_time(self):
        bm = BaseModel()
        old_time = bm.updated_at
        bm.save()
        self.assertNotEqual(old_time, bm.updated_at)

    def test_to_dict_contains_all_keys(self):
        bm = BaseModel()
        d = bm.to_dict()
        self.assertEqual(d["__class__"], "BaseModel")
        self.assertEqual(d["id"], bm.id)
        self.assertIn("created_at", d)
        self.assertIn("updated_at", d)


if __name__ == "__main__":
    unittest.main()

