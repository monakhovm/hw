import random
import string

def generate_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation.strip('\'(),`"~')

    while True:
        password = ''.join(random.choice(all_characters) for _ in range(length))
        if (any(c.islower() for c in password) and
                any(c.isupper() for c in password) and
                any(c.isdigit() for c in password) and
                any(c in string.punctuation for c in password)):
            return password

print("Welcome to the Linux User Password Generator!\n")

while True:
    try:
        pass_length = int(input("Please enter the desired password length: "))
        if pass_length < 4:
            raise ValueError("Length of the password is too small!")
        break
    except ValueError as e:
        print(e)


password = generate_password(pass_length)

print("\nGenerated password: ", password)
