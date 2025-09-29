#!/usr/bin/python3
"""Function that write a string and returns the number of characters written"""


def write_file(filename="", text=""):
    """Write text to a file and return the number of characters written"""
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
