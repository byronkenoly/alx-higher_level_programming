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

    def my_print(self):
        if self.__size == 0:
            print("")
        for i in range(0, self.__size):
            for j in range(0, self.__size - 1):
                print("#", end="")
            print("#")
