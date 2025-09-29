#!/usr/bin/python3
"""append string at the end of a file and returns the number of characters"""


def append_write(filename="", text=""):
    """appends string to text file"""
    with open(filename, 'a') as f:
        return f.write(text)
