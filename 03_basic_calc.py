# Project 03
# Basic Calculator

def add(x,y):
    res = x+y
    print(x, "+" ,y, "=", res , "\n")

def sub(x,y):
    res = x-y
    print(str(x) + " - "+ str(y) +" = "+ str(res) +"\n")

def mul(x,y):
    res = x*y
    print(x, "*" ,y, "=", res, "\n")

def div(x,y):
    res = x/y
    print(x, "/" ,y, "=", res, "\n")

i = 1

while (i == 1):

    print("MENU...")
    print("Press 1 for Addition(+)")
    print("Press 2 for Subtraction(-)")
    print("Press 3 for Multiplication(*)")
    print("Press 4 for Division(/)")
    print("Press 5 for Exit")
    choice = int(input("Enter the choice: "))

    if choice == 1:
        x = int(input("Enter the 1st Number: "))
        y = int(input("Enter the 2nd Number: "))
        add(x,y)
        continue
    elif choice == 2:
        x = int(input("Enter the 1st Number: "))
        y = int(input("Enter the 2nd Number: "))
        sub(x,y)
        continue
    if choice == 3:
        x = int(input("Enter the 1st Number: "))
        y = int(input("Enter the 2nd Number: "))
        mul(x,y)
        continue
    elif choice == 4:
        x = int(input("Enter the 1st Number (Numerator): "))
        y = int(input("Enter the 2nd Number (Denominator): "))
        div(x,y)
        continue
    elif choice == 5:
        break
    else:
        print("Wrong Input!!!, Enter the choice again...")
        continue

print("Program Exited...") #endpoint to check
