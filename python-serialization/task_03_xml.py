#!/usr/bin/env python3
"""
This module provides functions to serialize a Python dictionary
into XML and deserialize XML back into a Python dictionary.
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary: dict, filename: str) -> bool:
    """Serialize a Python dictionary into an XML file"""
    try:
        root = ET.Element("data")

        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)

        return True

    except Exception as e:
        print(f"Serialization error: {e}")
        return False


def deserialize_from_xml(filename: str) -> dict:
    """Deserialize an XML file into a Python dictionary"""
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}
        for child in root:
            result[child.tag] = child.text

        return result

    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
        return {}
    except ET.ParseError as e:
        print(f"XML Parse error: {e}")
        return {}
    except Exception as e:
        print(f"Unexpected error: {e}")
        return {}
