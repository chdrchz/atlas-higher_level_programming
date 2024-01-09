#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for item in range(x):
            try:
                value = my_list[item]
                print("{:d}".format(int(value)), end="")
                count += 1
            except (ValueError, TypeError):
                pass
    except IndexError:
        pass
    print()
    return count
