#!/usr/bin/python3
"""
Unit tests for console.py
"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.user import User


class TestConsole(unittest.TestCase):
    """Test the AirBnB console commands"""

    def setUp(self):
        """Reset storage before each test"""
        storage._FileStorage__objects = {}

    def test_create_and_show(self):
        """Test create and show commands"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            model_id = f.getvalue().strip()
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd(f"show BaseModel {model_id}")
            output = f.getvalue().strip()
        self.assertIn(model_id, output)
        self.assertIn("BaseModel", output)

    def test_destroy(self):
        """Test destroy command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            model_id = f.getvalue().strip()
        HBNBCommand().onecmd(f"destroy BaseModel {model_id}")
        self.assertNotIn(f"BaseModel.{model_id}", storage.all())

    def test_all(self):
        """Test all command"""
        HBNBCommand().onecmd("create BaseModel")
        HBNBCommand().onecmd("create User")
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all")
            output = f.getvalue()
        self.assertIn("BaseModel", output)
        self.assertIn("User", output)

    def test_update(self):
        """Test update command"""
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            model_id = f.getvalue().strip()
        HBNBCommand().onecmd(f"update BaseModel {model_id} name TestName")
        obj = storage.all()[f"BaseModel.{model_id}"]
        self.assertEqual(obj.name, "TestName")


if __name__ == "__main__":
    unittest.main()

