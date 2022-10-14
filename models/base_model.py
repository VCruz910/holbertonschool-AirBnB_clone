#!/usr/bin/python3
"""
BaseModel

Parent Class that defines all
common attributes/methods
for other classes.
"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """
    Defines the attributes/
    methods for the other
    classes.

    Attributes:
    ==================================
    Public Instance Attributes:
        - id
        - created_at
        - updated_at

    Methods:
    ==================================
    Public Instance Method:
        - save(self)
        - to_dict(self)

    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the attributes.
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
        else:
            ISOform = "%Y-%m-%dT%H:%M:%S.%f"
            for KEY, VALUE in kwargs.items():
                if KEY == 'created_at' or KEY == 'updated_at':
                    VALUE = datetime.strptime(kwargs[KEY], ISOform)
                if KEY != '__class__':
                    setattr(self, KEY, VALUE)

    def __str__(self):
        """
        Returns an instance in a dictionary
        representation:
        """
        NameCLASS = "[" + self.__class__.__name__ + "]"
        DICT = {K: V for (K, V) in self.__dict__.items() if (not V) is False}
        return (NameCLASS + "(" + self.id + ")" + str(DICT))

    def save(self):
        """
        Updates the last update time.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Creates a new dictionary instance, adds a key,
        and returns datetimes converted into strings.
        """

        NDICT = {}

        for KEY, VALUES in self.__dict__.items():
            if KEY == "created_at" or KEY == "updated_at":
                NDICT[KEY] = VALUES.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                if not VALUES:
                    pass
                else:
                    NDICT[KEY] = VALUES
        NDICT['__class__'] = self.__class__.__name__
        return (NDICT)
