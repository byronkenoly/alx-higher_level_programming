#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()

    for key, val in new_dict.items():
        change = {key: val * 2}
        new_dict.update(change)

    return new_dict
