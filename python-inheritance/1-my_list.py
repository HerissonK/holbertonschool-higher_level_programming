#!/usr/bin/python3
"""contient la classe MyList"""


class MyList(list):
    """une sous-classe de list"""

    def print_sorted(self):
        """affiche la liste triée sans modifier la liste originale"""
        print(sorted(self))
