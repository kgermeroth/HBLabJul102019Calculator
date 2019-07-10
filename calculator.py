"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

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
print("Quit")


# repeat forever:
while True:

    print("Type your choice followed by integers separated by a space")
#     read input
    user_prompt = input("> ").lower()
#     tokenize input
    #
    token = user_prompt.split(" ") #list of inputs
#     if the first token is "q":
    if token[0].startswith("q"):
        break
#         quit
#     else:
#         decide which math function to call based on first token
    elif token[0].startswith("add") or token[0] == "+":
        print(add(int(token[1]), int(token[2])))
        