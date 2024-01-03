#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        last_num = -(abs(number) % 10)
    else:
        last_num = abs(number) % 10
    return last_num
