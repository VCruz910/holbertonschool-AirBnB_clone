#!/usr/bin/python3
"""
FileStorage.

Class that serializes instances
to a JSON file and deserializes
JSON file to instances.
"""

import json
import os


class FileStorage:
    """
    Handles the storage of the
    classes, and json files.

    Attributes:
    ================================

    Private Class Attributes:
    ================================
        - __file_path:
            * A string.
            * Path to JSON file.

        - __objects:
            * A dictionary.
            * Empty, but stores
            all objects by
            <class name>.id.

    Public Instance Methods:
    =================================
        - all(self):
        - new(self, obj):
        - save(self):
        - reload(self):
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary '__objects'.
        """
        return (FileStorage.__objects())

    def new(self, obj):
        """
        Sets in '__objects' the 'obj'
        with key '<obj class name>.id'.
        """
        KEY = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[KEY] = obj

    def save(self):
        """
        Serializes '__objects' to the
        JSON file(path: __file_path).
        """

        dictionary = {}

        for KEY, VALUE in FileStorage.__objects.items():
            dictionary[KEY] = VALUE.to_dict()
        with open(FileStorage.__file_path, 'w') as F:
            json.dump(dictionary, F)

    def reload(self):
        """
        Deserializes the JSON file to
        '__objects' (only if the JSON
        file (__file_path) exists;
        otherwise, do nothing. If the
        file doesn’t exist, no exception
        should be raised).
        """
        from models.base_model import BaseModel
        from models.user import User
        from models.amenity import Amenity
        from models.place import Place
        from models.city import City
        from models.state import State
        from models.review import Review

        DICT = {
                'BaseModel': BaseModel,
                'User': User,
                'Amenity': Amenity,
                'Place': Place,
                'City': City,
                'State': State,
                'Review': Review
                }
        if os.path.exists(FileStorage.__file_path) is True:
            with open(FileStorage.__file_path, 'r') as F:
                for KEY, VALUE in json.load(F).items():
                    self.new(DICT[VALUE['__class__']](**VALUE))
