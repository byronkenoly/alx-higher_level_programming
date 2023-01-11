#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()

    mul = lambda x: x * 2

    for key, val in new_dict.items():
        change = {key: mul(val)}
        new_dict.update(change)

    return new_dict
