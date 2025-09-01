#!/usr/bin/python3
def uppercase(str):
    strlen = len(str)
    i = 0
    while i < strlen:
        char = ord(str[i])
        if 97 <= char <= 122:
            char -= 32
        print("{}".format(chr(char)), end="")
        i += 1
    print()
