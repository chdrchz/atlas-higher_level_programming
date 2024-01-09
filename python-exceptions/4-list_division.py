#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result_list = []
    try:
        for item in range(list_length):
            try:
                element_1 = my_list_1[item]
                element_2 = my_list_2[item]
                if not (isinstance(element_1, (int, float)) and isinstance(element_2, (int, float))):
                    raise TypeError("wrong type")
                if element_2 == 0:
                    raise ZeroDivisionError("division by 0")
                result_list.append(element_1 / element_2)
            except (TypeError, ZeroDivisionError) as e:
                print("{}".format(e))
                result_list.append(0)
    except IndexError:
        print("out of range")
    finally:
        return result_list
