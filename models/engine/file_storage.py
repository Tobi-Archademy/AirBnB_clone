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
        return FileStorage.__objects

    def new(self, obj):
        """Sets in `__objects` the supplied `obj` with the key
        <obj class name>.id
        """
        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes `__objects` to the JSON file path `__file_path`
        """
        a_copy = FileStorage.__objects
        obj_dict = {obj: a_copy[obj].to_dict() for obj in a_copy.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to `__objects` if it exists
        or do nothing, if `__file_path` doesn't exist
        """
        try:
            with open(FileStorage.__file_path) as f:
                objs = json.load(f)
                for obj in objs.values():
                    name = obj['__class__']
                    del obj['__class__']
                    self.new(eval(name)(**obj))
        except FileNotFoundError:
            return
