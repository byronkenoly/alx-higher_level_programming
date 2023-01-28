#!/usr/bin/python3
"""
function that prints: My name is <first name> <last name>
"""


def say_my_name(first_name, last_name=""):
    """
        say_my_name - prints name to stdout

        Args:
            first_name (string): first name
            last_name (string): last name
    """
    try:
        check_first = isinstance(first_name, str)
        check_last = isinstance(last_name, str)

        if check_first is False:
            raise TypeError

        if check_last is False:
            raise TypeError
    except TypeError:
        if check_first is False:
            print("first_name must be a string")
        if check_last is False:
            print("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
