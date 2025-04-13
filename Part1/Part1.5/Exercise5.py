number1 = int(input("Number 1: "))
number2 = int(input("Number 2: "))
operation = input("Operation: ")

add_result = number1 + number2
multiply_result = number1 * number2
subtract_result = number1 - number2

if operation == "add":
    print(f"{number1} + {number2} = {add_result}")

if operation == "multiply":
    print(f"{number1} * {number2} = {multiply_result}")

if operation == "subtract":
    print(f"{number1} - {number2} = {subtract_result}")