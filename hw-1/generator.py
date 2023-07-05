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
            if file == 'y' or file == 'Y':
                with open("password.txt", "w") as passwordFile:
                    passwordFile.write(password)
                return "The password was saved to \'password.txt\' file."
            return password
file = 'n'
print("Welcome to the Linux User Password Generator!\n")

while True:
    try:
        pass_length = int(round(float(input("Please enter the desired password length from 4 to 999,999 symbols: ").replace(',','.'))))
        if pass_length < 4:
            raise ValueError("Password length is not enough! Really? " + str(pass_length) + " symbols password?")
        elif pass_length > 999999:
            raise KeyError("To long password. Input new password length Waiting for number from 4 to 999,999: ")
        elif pass_length > 64:
            while True:
                try:
                    file_str = input("\nDo you really want so long password? \nIf yes type \"Y|y\". This will create file with name password.txt containing your new password. If file exists it will be overwritten. \nIf no type \"N|n\" and try again.\n=> ")
                    file_utf = file_str.encode('utf-8', errors='ignore')
                    file = file_utf.decode('utf-8', errors='ignore')
                    if file not in ['y', 'n', 'Y', 'N']:
                        raise ValueError("Input correct value (input \"Y|y\" or \"N|n\")")
                    elif file == 'n' or file == 'N':
                        raise KeyError("Input new password length: ")
                    break
                except ValueError as valueError:
                    print(valueError)
        break
    except ValueError as valueError:
        print(str(valueError).replace('\'', ''))
    except KeyError as keyError:
        print(str(keyError).replace('\'', ''))


password = generate_password(pass_length, file)

print("\nGenerated password: ", password)
