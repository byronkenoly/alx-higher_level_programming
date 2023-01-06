#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    count = 0

    for i, arg in enumerate(sys.argv):
        if i == 0:
            continue
        count += 1

    if count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operand = sys.argv[2]

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    if operand == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif operand == "-":
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif operand == "*":
        print("{} * {} = {}".format(a, b, mul(a, b)))
    elif operand == "/":
        print("{} / {} = {}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
