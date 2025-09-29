#!/usr/bin/python3
"""function that returns the number of characters written:"""


def write_file(filename="", text=""):
    """return the number of character"""
    count = 0
    with open(filename) as file:
        while file.read is not "":
            count += 1
    return count
