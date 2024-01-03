#!/usr/bin/python3

from sys import argv

for i in range(len(argv)):
    for j in range(len(argv)):
        print("{:d}: {:s}".format(i, argv[j]))
