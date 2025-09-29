#!/usr/bin/python3
"""function that returns the JSON representation of an object (string):"""


def to_json_string(my_obj):
    """returns JSON representation of an object"""
    import json
    return json.dumps(my_obj, ensure_ascii=False)
