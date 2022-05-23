#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_l = []
    divv = 0
    for i in range(list_length):
        try:
            divv = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            divv = 0
        except ZeroDivisionError:
            print("division by 0")
            divv = 0
        except IndexError:
            print("out of range")
            divv = 0
        finally:
            new_l.append(divv)
    return new_l
