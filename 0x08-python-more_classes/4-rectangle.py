#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """Class rectangle"""

    def __init__(self, width=0, height=0):
        """__init__ method called after instance has been created

            Args:
                width (int): width of rectangle
                height (int): height of rectangle
        """
        self.__width = width
        self.__height = height

    def __str__(self):
        """__str__ displays string represenation of object"""
        if self.__width == 0 or self.__height == 0:
            return ""

        display = []
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                display.append("#")
            if i != self.__height - 1:
                display.append("\n")

        return "".join(display)

    def __repr__(self):
        """__repr__ official string representation of object"""
        return "Rectangle(%s, %s)" % (self.__width, self.__height)

    @property
    def width(self):
        """return width of rectangle

        Returns:
            width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """sets width of rectangle

        Args:
            value (int): rectangle width
        """
        try:
            if isinstance(value, int) is False:
                raise TypeError

            if value < 0:
                raise ValueError
        except TypeError:
            print("width must be an integer")
            raise
        except ValueError:
            print("width must be >= 0")
            raise
        else:
            self.__width = value

    @property
    def height(self):
        """return height of rectangle

        Returns:
            height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """sets height of rectangle

        Args:
            value (int): rectangle height
        """
        try:
            if isinstance(value, int) is False:
                raise TypeError

            if value < 0:
                raise ValueError
        except TypeError:
            print("height must be an integer")
            raise
        except ValueError:
            print("height must be >= 0")
            raise
        else:
            self.__height = value

    def area(self):
        """area method computes rectangle area

        Returns:
            area of rectangle
        """
        sqr = self.__width * self.__height
        return sqr

    def perimeter(self):
        """perimeter method computes rectangle perimeter

        Returns:
            perimeter of rectangle
        """
        prmt = (self.__width * 2) + (self.__height * 2)
        return prmt
