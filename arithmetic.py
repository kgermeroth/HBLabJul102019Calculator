"""Math functions for calculator."""


# def add(num1, num2):
#     """Return the sum of the two inputs."""
#     return num1 + num2
test_list = [10,7,2]
def add(list):
    """Return the sum of the two inputs."""
    return sum(list)


# def subtract(num1, num2):
#     """Return the second number subtracted from the first."""
#     return num1 - num2

def subtract(list):
    """Return the second number subtracted from the first."""
    total = None

    for num in list:
        if total == None:
            total = num
        else:
            total -= num

    return total

# def multiply(num1, num2):
#     """Multiply the two inputs together."""
#     return num1 * num2

def multiply(list):
    """Multiply the two inputs together."""
    total = None

    for num in list:
        if total == None:
            total = num
        else:
            total *=num
    return total

# def divide(num1, num2):
#     """Divide the first input by the second and return the result."""
#     return num1/num2

def divide(list):
    """Divide the first input by the second and by any subsequent and return the result"""
    total = None

    for num in list:
        if total == None:
            total = num
        else:
            total /=num
    return total

# def square(num1):
#     """Return the square of the input."""

#     return num1**2

def square(list):
    """Return the square of the input."""
    total = []

    for num in list:
        total.append(num**2)
    return total

def cube(list):
    """Return the cube of the input."""
    total = []

    for num in list:
        total.append(num**3)
    return total


def power(list):
    """Raise num1 to the power of num2 and return the value."""
    total = None

    for num in list:
        if total == None:
            total = num
        else:
            total **= num
    return total    

def mod(list):
    """Return the remainder of num1 / num2."""
    total = None

    for num in list:
        if total == None:
            total = num
        else:
            total %= num

    return total
 
print("Add test", add(test_list))
print("Subtract test", subtract(test_list))
print("Multiply test", multiply(test_list))
print("Divide test", divide(test_list))
print("Square test", square(test_list))
print("Cube test", cube(test_list))
print("Power test", power(test_list))
print("Mod test", mod(test_list))