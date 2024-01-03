# Project 09
# Random Password Generator

import string
import random

characters = list(string.ascii_letters + string.digits + '!@#$%^&*()_<>,.?/')
def gen():
    length = int(input("Enter the length of the password: "))
    random.shuffle(characters)
    password = []

    for x in range(length):
        password.append(random.choice(characters))

    random.shuffle(password)
    password = "".join(password)

    print("Password :", password)


choice = int(input("Enter 1. to Generate Password\nEnter 2. to NOT Generate Password: "))
if choice == 1:
    gen()
elif choice == 2:
    exit()
else:
    print("Wrong Input!!!")