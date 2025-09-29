#!/usr/bin/python3
"""function that reads a text file (UTF8) and prints it to stdout:"""


def read_file(filename=""):
    """read text file and prints to stdout"""
    with open(filename) as file:
        print(file.read(), end="")
