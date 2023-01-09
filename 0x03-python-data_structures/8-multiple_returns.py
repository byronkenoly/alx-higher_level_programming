#!/usr/bin/python3

def multiple_returns(sentence):
    count = 0

    if sentence == "":
        tuple1 = (count, None)
        return tuple1

    for i in sentence:
        count += 1

    char1 = sentence[0]
    tuple1 = (count, char1)

    return tuple1
