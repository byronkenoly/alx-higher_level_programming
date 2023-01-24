#!/usr/bin/python3
"""class Square module"""


class Square:
    """Class square"""

    def __init__(self, size=0):
        """__init__ method called after instance has been created.

           Args:
               size (int): square length
        """
        try:
            check = isinstance(size, int)

            if check is False:
                raise TypeError

            if size < 0:
                raise ValueError
        except TypeError:
            print("size must be an integer", end="")
            raise
        except ValueError:
            print("size must be >= 0", end="")
            raise
        else:
            self.__size = size
