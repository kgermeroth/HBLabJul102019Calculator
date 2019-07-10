"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *



# repeat forever:
while True:
    #show a list of options:
    print("Here are your options:")
    print("Add or +")
    print("Subtract or -")
    print("Multiply or *")
    print("Divide or /")
    print("Square")
    print("Cube")
    print("Power")
    print("Mod or %")

    print("Type your choice followed by integers separated by a space")
#     read input
    user_prompt = input("> ")
#     tokenize input
    #
#     if the first token is "q":
#         quit
#     else:
#         decide which math function to call based on first token