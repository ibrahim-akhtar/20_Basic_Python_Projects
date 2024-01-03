# Project 15
# Rock, Paper, and Scissor

import random

user_points = 0
comp_points = 0
total = 0

while True:
    user = input("\nEnter b/w 'r' for rock, 'p' for paper, & 's' for scissor\nor just press Enter for Exit: ")

    options = ['r', 'p', 's']
    comp = random.choice(options)

    if user == "":
        break;

    elif user == 'r':
        if comp == 'p':
            comp_points += 1
            total += 1
            print("\nYou :", user, "- Computer :", comp,
                  "\nYou Lose!!!\n"
                  "Score -> You :", user_points, "- Computer :", comp_points)
        elif comp == 's':
            user_points += 1
            total += 1
            print("\nYou :", user, "- Computer :", comp,
                  "\nYou Win!!!\n"
                  "Score -> You :", user_points, "- Computer :", comp_points)
        else:
            total += 1
            print("\nYou :", user, "- Computer :", comp,
                  "\nRound Drawn!!!\n"
                  "Score -> You :", user_points, "- Computer :", comp_points)

    elif user == 'p':
        if comp == 's':
            comp_points += 1
            total += 1
            print("\nYou :", user, "- Computer :", comp,
                  "\nYou Lose!!!\n"
                  "Score -> You :", user_points, "- Computer :", comp_points)
        elif comp == 'r':
            user_points += 1
            total += 1
            print("\nYou :", user, "- Computer :", comp,
                  "\nYou Win!!!\n"
                  "Score -> You :", user_points, "- Computer :", comp_points)
        else:
            total += 1
            print("\nYou :", user, "- Computer :", comp,
                  "\nRound Drawn!!!\n"
                  "Score -> You :", user_points, "- Computer :", comp_points)

    elif user == 's':
        if comp == 'r':
            comp_points += 1
            total += 1
            print("\nYou :", user, "- Computer :", comp,
                  "\nYou Lose!!!\n"
                  "Score -> You :", user_points, "- Computer :", comp_points)
        elif comp == 'p':
            user_points += 1
            total += 1
            print("\nYou :", user, "- Computer :", comp,
                  "\nYou Win!!!\n"
                  "Score -> You :", user_points, "- Computer :", comp_points)
        else:
            total += 1
            print("\nYou :", user, "- Computer :", comp,
                  "\nRound Drawn!!!\n"
                  "Score -> You :", user_points, "- Computer :", comp_points)

    else:
        print("WRONG INPUT!!!\nEnter again...")


print("Match Ends...\n"
      "Stats...\n"
      "Total No. of Rounds:", total,
      "\nRounds Won:", user_points,
      "\nRounds Lost:", comp_points,
      "\nRounds Drawn:", total - (user_points + comp_points))
