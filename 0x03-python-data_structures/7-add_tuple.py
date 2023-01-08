#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    size1 = len(tuple_a)
    size2 = len(tuple_b)

    if size1 >= 2 and size2 >= 2:
        a, b = tuple_a
        c, d = tuple_b
        new_tuple = (a + c, b + d)
        return new_tuple

    # convert tuple to list using list()
    # convert list to tuple using tuple()
    if size1 < 2:
        list_a = list(tuple_a)
        while len(list_a) < 2:
            list_a.append(0)
        tuple_a = tuple(list_a)

    if size2 < 2:
        list_b = list(tuple_b)
        while len(list_b) < 2:
            list_b.append(0)
        tuple_b = tuple(list_b)

    w, x = tuple_a
    y, z = tuple_b

    new_tuple = (w + y, x + z)
    return new_tuple
