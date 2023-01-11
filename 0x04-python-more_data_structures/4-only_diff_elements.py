#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    combined = list(set_1 | set_2)
    my_list = []
    for i in set_1:
        for j in set_2:
            if i == j:
                my_list.append(j)

    for k in my_list:
        for x in combined:
            if k == x:
                combined.remove(x)

    return combined
