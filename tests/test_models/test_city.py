#!/usr/bin/python3
"""Unittest module for the City Class."""

import unittest
import os
import re
import json
from datetime import datetime
from models.city import City
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage


class TestCity(unittest.TestCase):
    """Test Cases for the City class."""

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
        """Test instantiation of City class."""
        city_instance = City()
        self.assertEqual(str(type(city_instance)),
                         "<class 'models.city.City'>")
        self.assertIsInstance(city_instance, City)
        self.assertTrue(issubclass(type(city_instance), BaseModel))

    def test_attributes(self):
        """Test the attributes of City class."""
        city_instance = City()
        attributes = storage.attributes()["City"]
        for key, value in attributes.items():
            self.assertTrue(hasattr(city_instance, key))
            self.assertEqual(type(getattr(city_instance, key, None)), value)


if __name__ == "__main__":
    unittest.main()
