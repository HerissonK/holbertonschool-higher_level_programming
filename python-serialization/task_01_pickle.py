#!/usr/bin/env python3
"""serialize and deserialize custom Python objects using the pickle module"""

import pickle
import os


class CustomObject:
    def __init__(self, name: str, age: int, is_student: bool):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the attributes"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename: str):
        """Serialize the object and save it to a file."""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except (OSError, pickle.PickleError) as e:
            print(f"Serialization error: {e}")
            return None

    @classmethod
    def deserialize(cls, filename: str):
        """Deserialize the object from the file and return it"""
        if not os.path.exists(filename):
            print("Error: File does not exist.")
            return None
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
            return obj
        except (OSError, pickle.PickleError, EOFError) as e:
            print(f"Deserialization error: {e}")
            return None
