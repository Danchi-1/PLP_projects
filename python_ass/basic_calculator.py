numOne = input("Enter a number: ")
numTwo = input("Enter another number: ")
operation = input("Enter the operation: ")

def add(numOne, numTwo):
    return int(numOne) + int(numTwo)


def substraction(numOne, numTwo):
    return int(numOne) + int(numTwo)


def product(numOne, numTwo):
    return int(numOne) + int(numTwo)


def division(numOne, numTwo):
    return int(numOne) + int(numTwo)

try:
    if operation == "+":
        print(add(numOne, numTwo))
    elif operation == "-":
        print(substraction(numOne, numTwo))
    elif operation == "*":
        print(product(numOne, numTwo))
    elif operation == "/":
        print(division(numOne, numTwo))
    else:
        print("Operation should be specified correctly: write + for addition, - for substraction, * for product, and / for division")
except ValueError:
    rules = "number must be an integer"
    print(rules)