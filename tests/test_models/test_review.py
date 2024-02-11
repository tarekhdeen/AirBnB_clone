#!/usr/bin/python3
"""Unittest module for the Review Class."""

import unittest
import os
import re
import json
from datetime import datetime
from models.review import Review
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage


class TestReview(unittest.TestCase):
    """Test Cases for the Review class."""

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
        """Test instantiation of Review class."""
        review_instance = Review()
        self.assertEqual(str(type(review_instance)),
                         "<class 'models.review.Review'>")
        self.assertIsInstance(review_instance, Review)
        self.assertTrue(issubclass(type(review_instance), BaseModel))

    def test_attributes(self):
        """Test the attributes of Review class."""
        review_instance = Review()
        attributes = storage.attributes()["Review"]
        for key, value in attributes.items():
            self.assertTrue(hasattr(review_instance, key))
            self.assertEqual(type(getattr(review_instance, key, None)), value)


if __name__ == "__main__":
    unittest.main()
