word_list = ["camel"]

#todo1
import random
chosen_word = random.choice(word_list)

#todo2
guess = input("guess a letter: ").lower()

#todo3
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")