#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    square = lambda x: x * x

    x = 0
    y = 0

    # list comprehension to create copy of list without altering original
    copy = [x[:] for x in matrix]

    for lst in copy:
        for i in lst:
            new_val = square(i)
            copy[x][y] = new_val
            y += 1
        x += 1
        y = 0

    return copy
