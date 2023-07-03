#!/bin/env python3
import random
import string

def generate_password(length, file = None):
    all_characters = string.ascii_letters + string.digits + string.punctuation.translate({ord(i): None for i in '\',~()'})

    while True:
        password = ''.join(random.choice(all_characters) for symbols in range(length))
        if (any(char.islower() for char in password) and
                any(char.isupper() for char in password) and
                any(char.isdigit() for char in password) and
                any(char in string.punctuation for char in password)):
            if file == 'y':
                with open("password.txt", "w") as passwordFile:
                    passwordFile.write(password)
                return "The password was saved to \'password.txt\' file."
            return password

print("Welcome to the Linux User Password Generator!\n")

while True:
    try:
        pass_length = int(input("Please enter the desired password length: "))
        if pass_length < 4:
            raise ValueError("Length of the password is too small!")
        elif pass_length > 999999:
            raise KeyError("To long password. Input new password length: ")
        elif pass_length > 64:
            while True:
                try:
                    file = input("\nDo you really want so long password? \nIf yes type \"y\". This will create file with name password.txt containing your new password. \nIf no type \"n\" and try again.\n=> ")
                    if file not in ['y', 'n']:
                        raise ValueError("Input correct value (\"y\" or \"n\")")
                    elif file == 'n':
                        raise KeyError("Input new password length: ")
                    break
                except ValueError as valueError:
                    print(valueError)
        break
    except ValueError as sizeError:
        print(sizeError)
    except KeyError as keyError:
        print(str(keyError).replace('\'', ''))


password = generate_password(pass_length, file)

print("\nGenerated password: ", password)
