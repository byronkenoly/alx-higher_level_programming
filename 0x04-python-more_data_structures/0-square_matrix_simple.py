#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    x = 0
    y = 0

    # list comprehension to create copy of list without altering original
    copy = [x[:] for x in matrix]

    for lst in copy:
        for i in lst:
            new_val = i ** 2
            copy[x][y] = new_val
            y += 1
        x += 1
        y = 0

    return copy
