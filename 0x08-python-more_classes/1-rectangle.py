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
