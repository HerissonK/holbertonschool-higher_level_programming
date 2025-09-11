#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    convert = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    value = 0
    for i in range(len(roman_string)):
        if (
            i < len(roman_string) - 1
            and convert[roman_string[i]] < convert[roman_string[i + 1]]
        ):
            value -= convert[roman_string[i]]
        else:
            value += convert[roman_string[i]]
    return value
