#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
import random
chosen_word = random.choice(word_list)
print("random word is " + chosen_word)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("guess a letter for the game of hangman:" )
print("user guess word is " + guess)

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
if guess == chosen_word:
    print("you are correct")
else: 
    print("try again")