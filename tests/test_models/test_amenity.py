#!/usr/bin/python3
"""Unittest module for the Amenity Class."""

import unittest
import os
import re
import json
from datetime import datetime
from models.amenity import Amenity
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage


class TestAmenity(unittest.TestCase):
    """Test Cases for the Amenity class."""

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
        """Test instantiation of Amenity class."""
        amenity_instance = Amenity()
        self.assertEqual(str(type(amenity_instance)),
                         "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(amenity_instance, Amenity)
        self.assertTrue(issubclass(type(amenity_instance), BaseModel))

    def test_attributes(self):
        """Test the attributes of Amenity class."""
        amenity_instance = Amenity()
        attributes = storage.attributes()["Amenity"]
        for key, value in attributes.items():
            self.assertTrue(hasattr(amenity_instance, key))
            self.assertEqual(type(getattr(amenity_instance, key, None)), value)


if __name__ == "__main__":
    unittest.main()
