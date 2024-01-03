# Project 14
# Simple Python Dictionary

"""
# 1st Way ->

word_dict = {
    'eyes' : 'an organ for seeing',
    'ears' : 'an organ for hearing',
    'nose' : 'an organ for smelling',
    'tongue' : 'an organ for tasting',
    'skin' : 'an organ for feeling/touching things'
}

while True:
    word = input("Enter the word you want to search the meaning of: ")
    if word == "":
        break

    if word in word_dict:
        print("Word:", word,"\nMeaning:", word_dict[word])
    else:
        print("Word not in the dictionary...")

print("Since you not entered anything, program stopped...")

"""

# 2nd Way ->

# 1. install PyDictionary library of python from the termianl
# 2. Command: pip install PyDictionary

from PyDictionary import PyDictionary

dict = PyDictionary()

while True:
    word = input("Enter the word you want to search the meaning of: ")
    if word == "":
        break

    print("Word:", word,"\nMeaning:", dict.meaning(word))

print("Since you not entered anything, program stopped...")
