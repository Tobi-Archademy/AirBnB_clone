#!/usr/bin/python3
"""Defines the `FileStorage class` that serializes instances to
JSON file and deserializes JSON file to instances
"""
import json
from models.base_model import BaseModel

class FileStorage:
    """Serializes instances to a JSON file and
    deserializes JSON file to instances.

    Attributes:
        __file_path (str): Path to a JSON file (to deserialize)
        __objects (dict): Empty but will store all objects by
        `<class name>.id`
            Ex: to store a `BaseModel` object with `id=12121212`,
            the key will be `BaseModel.12121212`.
    """
   __file_path = "file.json"
   __objects = {}

    def all(self):
        """Retuns the dictionary `__objects`
        """
        return (self.__class__.__name__.__objects)

    def new(self, obj):
        """Sets in `__objects` the supplied `obj` with the key
        <obj class name>.id
        """
        key = obj.__class__.__name__ + '.' + obj.id
        return (self.__class__.__name__.__objects[key] = obj)

    def save(self):
        """Serializes `__objects` to the JSON file path `__file_path`
        """
        copy_instance = self.__class__.__name__.__objects
        obj_dicts = {obj: copy_instance[obj]
                for obj in copy_instance.keys()}
        with open(self.__class__.__name__.__file_path, "w") as f:
            json.dump(copy_instance, f)

    def reload(self):
        """Deserializes the JSON file to `__objects` if it exists
        or do nothing, if `__file_path` doesn't exist
        """
        try:
            with open(self.__class__.__name__.__file_path) as f:
                objs = json.load(f)
                for obj in objs.values():
                    name = obj['__class__']
                    del obj['__class__']
                    self.new(eval(name)(**obj))
        except FileNotFoundError:
            return
