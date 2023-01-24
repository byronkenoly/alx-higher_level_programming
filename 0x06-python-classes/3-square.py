#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
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

    def area(self):
        srq = self.__size ** 2
        return srq
