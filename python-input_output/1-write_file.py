#!/usr/bin/python3
"""function that writes a string to a text file (UTF8) and returns the number of characters written:"""



def write_file(filename="", text=""):
    """return the number of lines"""
    count = 0
    with open(filename) as file:
        while file.readline() is not "":
            count += 1
    return count
