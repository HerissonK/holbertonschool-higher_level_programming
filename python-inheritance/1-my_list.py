#!/usr/bin/python3
"""contient la class MyList"""


class MyList(list):
    """une liste de sousclasse"""

    def print_sorted(self):
        print(sorted(self))
