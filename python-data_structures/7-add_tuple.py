#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    default_tuple = (0, 0)
    if len(tuple_a) < 2:
        tuple_a = tuple_a + default_tuple
    if len(tuple_b) < 2:
        tuple_b = tuple_b + default_tuple
    valeur1 = tuple_a[0] + tuple_b[0]
    valeur2 = tuple_a[1] + tuple_b[1]
    add_tuple = (valeur1, valeur2)
    return add_tuple
