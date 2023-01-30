#!/usr/bin/python3
"""
function that divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
        matrix_divided - divides all elements of a matrix

        Args:
            matrix (list of lists): matrix to be divided
            div (int or float): divisor

        Returns:
            new matrix
    """
    try:
        for ls in matrix:
            for i in ls:
                check_int = isinstance(i, int)
                check_float = isinstance(i, float)

                if check_int is False and check_float is False:
                    raise TypeError
        
        elements = len(matrix[0])

        for ls in matrix:
            count = 0
            for i in ls:
                count += 1
            if count != elements:
                raise TypeError

        if isinstance(div, int) is False and isinstance(div, float) is False:
            raise TypeError

        if div == 0:
            raise ZeroDivisionError
    except TypeError:
        if check_int is False and check_float is False:
            return "matrix must be a matrix (list of lists) of integers/floats"
        elif isinstance(div, int) is False and isinstance(div, float) is False:
            return "div must be a number"
        else:
            return "Each row of the matrix must have the same size"
    except ZeroDivisionError:
        return "division by zero"
    else:
        # copying nested list that wont interfere with original
        # found solution on stack overflow
        copy = [x[:] for x in matrix]

        x = 0
        for ls in copy:
            y = 0
            for i in ls:
                copy[x][y] =  round(i / div, 2)
                y += 1
            x += 1

        return copy
