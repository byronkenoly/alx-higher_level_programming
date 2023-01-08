#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list

    count = -1
    for i in my_list:
        count += 1

    if idx > count:
        return my_list

    # slice operation returning a shallow copy of the list
    copy = my_list[:]

    copy[idx] = element

    return copy
