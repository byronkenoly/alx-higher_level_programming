#!/usr/bin/python3

def add_integer(a, b=98):
    """ add_integer returns sum of two integers

        Args:
            a (int): first operand
            b (int): second operand
       
        Returns:
            sum of the two operands
    """
    try:
        if isinstance(a, float) is True:
            a = int(a)

        if isinstance(b, float) is True:
            b = int(b)

        check_a = isinstance(a, int)
        check_b = isinstance(b, int)

        if check_a is False:
            raise TypeError

        if check_b is False:
            raise TypeError
    except TypeError:
        if check_a is False:
            return "a must be an integer"
        if check_b is False:
            return "b must be an integer"
    else:
        return a + b
