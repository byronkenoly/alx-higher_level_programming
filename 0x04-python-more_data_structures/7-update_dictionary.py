#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    change = {key: value}
    a_dictionary.update(change)

    return a_dictionary
