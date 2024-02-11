#!/usr/bin/python3
"""Unittest module for the User Class."""

import unittest
import os
import re
import json
from datetime import datetime
from models.user import User
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage


class TestUser(unittest.TestCase):
    """Test Cases for the User class."""

    def setUp(self):
        """Set up test methods."""
        pass

    def tearDown(self):
        """Tear down test methods."""
        self._reset_storage()
        pass

    def _reset_storage(self):
        """Reset FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.isfile(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_instantiation(self):
        """Test instantiation of User class."""
        user_instance = User()
        self.assertEqual(str(type(user_instance)),
                         "<class 'models.user.User'>")
        self.assertIsInstance(user_instance, User)
        self.assertTrue(issubclass(type(user_instance), BaseModel))

    def test_attributes(self):
        """Test the attributes of User class."""
        user_instance = User()
        attributes = storage.attributes()["User"]
        for key, value in attributes.items():
            self.assertTrue(hasattr(user_instance, key))
            self.assertEqual(type(getattr(user_instance, key, None)), value)


if __name__ == "__main__":
    unittest.main()
