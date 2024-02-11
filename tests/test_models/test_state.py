#!/usr/bin/python3
"""Unittest module for the State Class."""
import unittest
import os
import re
import json
from datetime import datetime
from models.state import State
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage


class TestState(unittest.TestCase):
    """Test Cases for the State class."""

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
        """Test instantiation of State class."""
        state_instance = State()
        self.assertEqual(str(type(state_instance)),
                         "<class 'models.state.State'>")
        self.assertIsInstance(state_instance, State)
        self.assertTrue(issubclass(type(state_instance), BaseModel))

    def test_attributes(self):
        """Test the attributes of State class."""
        state_instance = State()
        attributes = storage.attributes()["State"]
        for key, value in attributes.items():
            self.assertTrue(hasattr(state_instance, key))
            self.assertEqual(type(getattr(state_instance, key, None)), value)


if __name__ == "__main__":
    unittest.main()
