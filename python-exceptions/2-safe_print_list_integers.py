#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for item in range(x):
            value = my_list[item]
            print("{:d}".format(value), end="")
            if isinstance(value, int):
                count += 1
    except (ValueError, IndexError):
        pass
    print()
    return count
