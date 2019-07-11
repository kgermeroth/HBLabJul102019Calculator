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
print("Power of two integers")
print("Mod or %")
print("Quit")


# repeat forever:
while True:

    print("Type your choice followed by integers separated by a space")
#     read input
    user_prompt = input("> ").lower()
#     tokenize input
    #
    token_list = user_prompt.split(" ") #list of 

    for idx, item in enumerate(token_list):
        if item.isdigit():
            token_list[idx] = int(token_list[idx])

    operator, x, *other_nums = token_list

    if len(token_list) == 3:
        y = other_nums[0]

#     if the first token is "q":
    if operator.startswith("q"):
        break
#         quit
#     else:
#         decide which math function to call based on first token
    elif operator.startswith("add") or operator == "+":
        print(add(x, y))

    elif operator.startswith("sub") or operator =="-":
        print(subtract(x, y))

    elif operator.startswith("mul") or operator == "*":
        print(multiply(x, y))

    elif operator.startswith("div") or operator == "/":
        print(divide(x, y))

    elif operator.startswith("squ"):
        print(square(x))

    elif operator.startswith("cub"):
        print(cube(x))

    elif operator.startswith("pow"):
        print(power(x, y))

    elif operator.startswith("mod") or operator == "%":
        print(mod(x, y))

    else:
        print("that is not a valid input, try again! ")



