#!/usr/bin/python3

def uniq_add(my_list=[]):
    # converting given list to set
    new_set = set(my_list)

    summation = 0
    for i in new_set:
        summation += i

    return summation
