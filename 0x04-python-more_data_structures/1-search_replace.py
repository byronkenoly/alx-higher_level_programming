#!/usr/bin/python3

def search_replace(my_list, search, replace):
    copy = my_list[:]
    x = 0

    for i in my_list:
        if i == search:
            copy[x] = replace
        x += 1

    return copy
