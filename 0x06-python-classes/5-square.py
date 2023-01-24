#!/usr/bin/python3
"""class Square module"""

class Square:
    """Class square"""

    def __init__(self, size=0):
        """__init__ method called after instance has been created.
           
           Args:
               size (int): square length
        """
        self.size = size

    @property
    def size(self):
        """returns length of square.
           
           Returns:
               length of square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """sets length of square.
           
           Args:
               value (int): square length
        """
        try:
            check = isinstance(value, int)

            if check is False:
                raise TypeError

            if value < 0:
                raise ValueError
        except TypeError:
            print("size must be an integer", end="")
            raise
        except ValueError:
            print("size must be >= 0", end="")
            raise
        else:
            self.__size = value

    def area(self):
        """area method computes area of square.
           
           Returns:
               area of square
        """
        srq = self.__size ** 2

    def my_print(self):
        """prints square - putchar(35)/#"""
        if self.__size == 0:
            print("")
        for i in range(0, self.__size):
            for j in range(0, self.__size - 1):
                print("#", end="")
            print("#")
