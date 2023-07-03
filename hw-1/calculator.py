#!/bin/env python3
def addition(x: float, y: float):
    try:
        return x+y
    except ValueError:
        print("Error: " + ValueError)

def substraction(x: float, y: float):
    try:
        return x-y
    except ValueError:
        print("Error: " + ValueError)

def multiplication(x: float, y: float):
    try:
        return x*y
    except ValueError:
        print("Error: " + ValueError)

def division(x: float, y: float):
    try:
        return x/y
    except ValueError:
        print("Error: " + ValueError)
    except ZeroDivisionError:
        return "infinity"

operations = {
    1:addition, 
    2:substraction, 
    3:multiplication, 
    4:division
}

def calculator(x: float, y: float, n: int):
    result = operations[n](x,y)
    if y!=0 and result*10%10==0:
        result = int(result)
    return "\nThe result of " + operations[n].__name__ + " is: " + str(result)
    

print("Welcome to the Calculator Program!\n")

while True:
    try:
        x = float(input("Please enter the first number: "))
        break
    except ValueError:
        print("Not a number! Input correct value (integer or float with floating point)")


while True:
    try:
        y = float(input("Please enter the second number: "))
        break
    except ValueError:
        print("Not a number! Input correct value (integer or float with floating point)")


print("""
    Please select an operation:
        1. Addition
        2. Subtraction
        3. Multiplication
        4. Division
""")

while True:
    try:
        n = int(input("Enter your choice (1-4): "))
        if n < 1 or n > 4:
            raise KeyError("Incorrect operation! Input correct value according to main instructions!")
        break
    except KeyError as keyError:
        print(str(keyError).replace('\'', ''))
    except ValueError:
        print("Not a number! Input correct value (integer or float with floating point)")


print(calculator(x,y,n))