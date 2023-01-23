#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for i in my_list:
            count += 1
        if count < x:
            raise IndexError

        count = 0
        for item in my_list:
            if count == x:
                break
            if count <= x - 2:
                print(item, end="")
            else:
                print(item)
            count += 1
        return x
    except IndexError:
        a = 0
        for y in my_list:
            if a <= count - 2:
                print(y, end="")
            else:
                print(y)
            a += 1
        return count
