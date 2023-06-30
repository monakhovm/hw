
def addition(x,y: float):
    try:
        return x+y
    except ValueError:
        print("Error: " + ValueError)

def substraction(x,y: float):
    try:
        return x-y
    except ValueError:
        print("Error: " + ValueError)

def multiplication(x,y: float):
    try:
        return x*y
    except ValueError:
        print("Error: " + ValueError)

def division(x,y: float):
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

def calculator(x,y: float, n: int):
    result = operations[n](x,y)
    if result*10%10==0:
        result = int(result)
    return "\nThe result of " + operations[n].__name__ + " is: " + str(result)
    

print("Welcome to the Calculator Program!\n")

while True:
    try:
        x = float(input("Please enter the first number: "))
        break
    except ValueError:
        print("Not a number! Try again!")


while True:
    try:
        y = float(input("Please enter the second number: "))
        break
    except ValueError:
        print("Not a number! Try again!")


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
        break
    except ValueError:
        print("Not a number! Try again!")


print(calculator(x,y,n))