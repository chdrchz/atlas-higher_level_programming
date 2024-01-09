#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for item in my_list[:x]:
            value = my_list[item]
            print("{:d}".format(value), end="")
            if isinstance(value, int):
                count += 1
    except IndexError:
        pass
    print()
    return count
