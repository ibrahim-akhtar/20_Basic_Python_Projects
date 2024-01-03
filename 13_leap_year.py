# Project 13
# Leap Year Checker

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Leap Year")
            else:
                print("Not a Leap Year")
        else:
            print("Leap Year")
    else:
        print("Not a Leap Year")

is_leap_year(int(input("Enter the year you want to check: ")))
