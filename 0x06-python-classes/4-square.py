#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
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
        srq = self.__size ** 2
        return srq
