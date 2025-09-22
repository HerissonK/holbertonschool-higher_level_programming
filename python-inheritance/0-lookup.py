#!/usr/bin/python3
"""Definition d'un objet attribut lookup function"""


def lookup(obj):
    """Retourne la liste des attributs et mehodes disponibles pour un objet"""
    return dir(obj)
