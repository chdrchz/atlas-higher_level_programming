#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":

    sums = sum(int(arg) for arg in argv[1:] if arg.isdigit())
    print(sums)
