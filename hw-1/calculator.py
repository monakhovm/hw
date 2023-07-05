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
        x = float(input("Please enter the first number (integer or float): ").replace(',', '.'))
        break
    except ValueError:
        print("Not a number! Input correct value (integer or float with floating point)")


while True:
    try:
        y = float(input("Please enter the second number (integer or float): ").replace(',', '.'))
        break
    except ValueError:
        print("Not a number! Input correct value (integer or float with floating point)")


print("""
    Please select an operation:
        1. Addition (x+y)
        2. Subtraction (x-y)
        3. Multiplication (x*y)
        4. Division (x/y)
""")

while True:
    try:
        n = int(input("Choose desired operation. Enter number from 1 to 4: "))
        if n < 1 or n > 4:
            raise KeyError("Incorrect operation number! Input correct value according to main instructions!")
        break
    except KeyError as keyError:
        print(str(keyError).replace('\'', ''))
    except ValueError:
        print("That's not a number! Try again with correct value (integer or float with floating point) from 1 to 4")


print(calculator(x,y,n))