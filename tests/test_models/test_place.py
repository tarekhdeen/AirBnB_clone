#!/usr/bin/python3
"""Unittest module for the Place Class."""

import unittest
import os
import re
import json
from datetime import datetime
from models.place import Place
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage


class TestPlace(unittest.TestCase):
    """Test Cases for the Place class."""

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
        """Test instantiation of Place class."""
        place_instance = Place()
        self.assertEqual(str(type(place_instance)),
                         "<class 'models.place.Place'>")
        self.assertIsInstance(place_instance, Place)
        self.assertTrue(issubclass(type(place_instance), BaseModel))

    def test_attributes(self):
        """Test the attributes of Place class."""
        place_instance = Place()
        attributes = storage.attributes()["Place"]
        for key, value in attributes.items():
            self.assertTrue(hasattr(place_instance, key))
            self.assertEqual(type(getattr(place_instance, key, None)), value)


if __name__ == "__main__":
    unittest.main()
