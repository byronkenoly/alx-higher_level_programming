#!/usr/bin/python3

def safe_print_integer(value):
    try:
        boolean = isinstance(value, int)
	
        if boolean == False:
            raise TypeError

        print("{:d}".format(value))
        return True
    except TypeError:
        return False
