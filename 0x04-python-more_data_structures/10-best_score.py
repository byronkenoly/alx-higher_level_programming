#!/usr/bin/python3

def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    my_list = []
    for val in a_dictionary.values():
        my_list.append(val)

    big = my_list[0]
    for i in my_list:
        if i > big:
            big = i

    for key, val in a_dictionary.items():
        if val == big:
            return key
