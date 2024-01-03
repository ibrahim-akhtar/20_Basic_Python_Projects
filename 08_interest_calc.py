# Project 08
# Interest Calculator (Simple Interest)

def monthly():
    principal = float(input("Enter the principal amount: ", ))
    rate = float(input("Enter the monthly rate: "))
    time = int(input("Enter the number of months: "))

    interest = (principal * rate * time) / 100
    amount = principal + interest

    print("Monthly interest is: %.2f" %(interest/time))
    print("Total amount will be: %.2f" %amount)


def yearly():
    principal = float(input("Enter the principal amount: ", ))
    rate = float(input("Enter the yearly rate: "))
    time = float(input("Enter the number of years: "))

    interest = (principal * rate * time) / 100
    amount = principal + interest

    print("Yearly interest is: %.3f" %(interest/time))
    print("Total amount will be: %.3f" % amount)


print("Menu...")
choice = int(input("Enter 1. for Monthly Rate.\nEnter 2. for Yearly Rate: "))

if choice == 1:
    monthly()
elif choice == 2:
    yearly()
else:
    print("Wrong Input!!!")