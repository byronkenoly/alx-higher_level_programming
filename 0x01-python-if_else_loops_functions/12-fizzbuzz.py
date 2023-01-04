#!/usr/bin/python3
for i in range(1, 101):
    output = ""
    if i % 3 == 0:
        output += "Fizz"
    if i % 5 == 0:
        output += "Buzz"
    if output == "":
        output = i

    if i != 100:
        print(output, end=" ")
    else:
        print(output)
