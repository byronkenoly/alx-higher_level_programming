#!/usr/bin/python3
"""
function that prints a square with the character #
"""


def print_square(size):
    """
        print_square - prints square with character #

        Args:
            size: length of square
    """
    if isinstance(size, float) is True and size < 0:
        size = int(size)

    check = isinstance(size, int)

    try:
        if check is False:
            raise TypeError

        if size < 0:
            raise ValueError
    except TypeError:
        print("size must be an integer")
    except ValueError:
        print("size must be >= 0")
    else:
        count = 0
        for i in range(0, size):
            for j in range(0, size):
                if count == size - 1:
                    print("#")
                    continue
                print("#", end="")
                count += 1
            count = 0
