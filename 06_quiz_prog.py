# Project 06
# Quiz Program

quiz = {
    "question1": {
        "question": "Capital of England?",
        "answer": "London"
    },
    "question2": {
        "question": "Capital of France?",
        "answer": "Paris"
    },
    "question3": {
        "question": "Capital of Germany?",
        "answer": "Berlin"
    },
    "question4": {
        "question": "Capital of Italy?",
        "answer": "Rome"
    },
    "question5": {
        "question": "Capital of Spain?",
        "answer": "Madrid"
    },
    "question6": {
        "question": "Capital of Portugal?",
        "answer": "Lisbon"
    },
    "question7": {
        "question": "Capital of Switzerland?",
        "answer": "Bern"
    },
    "question8": {
        "question": "Capital of Austria?",
        "answer": "Vienna"
    },
}

score = 0
print("Quiz Starts ...\n")
index = 0

for key, value in quiz.items():

    print("Question", index+1, ":")
    print(value['question'])
    ans = input("Answer : ")

    if ans.lower() == value['answer'].lower():
        print("Correct Answer")
        score = score + 1
        index = index + 1
        print("Score:", score, "/", index)
    else:
        print("Wrong Answer!!!")
        print("Correct Answer is", value['answer'])
        index = index + 1
        print("Score:", score, "/", index)

print("\nQuiz Ends...")
print("Final Score:", score, "/", index)