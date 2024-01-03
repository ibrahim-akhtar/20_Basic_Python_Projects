# Project 02
# Word Replacement

def replace_word():

    str = "Simple program to demonstrate the word replacement program..."
    print (str)
    word_to_replace = input("Enter the word you want to replace: ")
    replacing_word = input("Enter the word you want to replace with: ")
    print(str.replace(word_to_replace, replacing_word))

replace_word()
