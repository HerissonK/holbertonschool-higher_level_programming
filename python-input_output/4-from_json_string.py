#!/usr/bin/python3
"""returns an object (Python data structure) represented by a JSON string"""


def from_json_string(my_str):
    """returns object from JSON"""
    import json
    return json.loads(my_str)
