#!/usr/bin/python3
"""a module for BaseModel that defines all common methods for other classes"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:

    """Bublic class defines all common methods for other classes"""

    def __init__(self, *args, **kwargs):
        """Initialization of Base instance"""

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Return a string representation of an instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary of __dict__ of the instance"""
        odict = self.__dict__.copy()
        odict['__class__'] = self.__class__.__name__
        odict['created_at'] = odict['created_at'].isoformat()
        odict['updated_at'] = odict['updated_at'].isoformat()
        return odict
