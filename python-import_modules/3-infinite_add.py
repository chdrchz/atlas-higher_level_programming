#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    sums = 0
    sums = sum(int(arg) for arg in argv[1:] if arg.isdigit())
    print(sums)
