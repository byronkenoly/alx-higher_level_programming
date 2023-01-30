#!/usr/bin/python3
"""
function that prints text with 2 new lines after these chars: ., ? and :
"""


def text_indentation(text):
    """
        text_indentation - modifies string

        Args:
            text (string): string to be modified
    """
    try:
        if isinstance(text, str) is False:
            raise TypeError

        count = 0
        start = True
        for element in text:
            if start == True:
                if element == " ":
                    element = element.replace(" ", "")
                    start = False
            print(element, end="") 
            if element == "." or element == "?" or element == ":":
                count += 1
            if count > 0:
                print("\n")
                count = 0
                start = True
                continue

    except TypeError:
        print("text must be a string")    
