#!/usr/bin/python3
def print_last_digit(number):
    last_digit = abs(number) % 10
    print(last_digit, end="")  # end="" évite le saut de ligne supplémentaire
    return last_digit
