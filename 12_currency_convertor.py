# Project 12
# Currency Convertor

#Note: Conversion rates are as per 02/01/2024

def pounds_to_euros():
    pounds = float(input("How much Pounds: "))
    euros = pounds * 1.15
    print("Pounds :", pounds,"\nEuros :", euros)

def euros_to_pounds():
    euros = float(input("How much Pounds: "))
    pounds = euros * 0.87
    print("Euros :", euros,"\nPounds :", pounds)

print("Menu...\n"
      "Currency Conversion...")
choice = int(input("Enter 1. for Pounds to Euros.\n"
                   "Enter 2. for Euros to Pounds: "))
if choice == 1:
    pounds_to_euros()
elif choice == 2:
    euros_to_pounds()
else:
    print("Wrong Input!!!")
