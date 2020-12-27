from random import *
words = ["apple", "banana", "coffee"]
word = choice(words)
print("answer is", word)
letters = ""

while True:
    succeed = True
    print()
    for w in word:
        if w in letters:
            print(w, end=" ")
        else:
            print("_", end=" ")
            succeed = False
    print()

    if succeed:
        print("SUCCESS")
        break

    letter = input("Input letter > ")

    if letter not in letters:
        letters += letter

    if letter in word:
        print("Currect")
    else:
        print("Wrong")
