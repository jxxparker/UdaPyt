from hangman_art import stages
from hangman_art import logo
from hangman_word import word_list
import random

chosen_word = random.choice(word_list) #chooses a random word
word_length = len(chosen_word)

end_of_game = False
lives = 6
print(f"the answer is {chosen_word}") #this is the answer for testing

display = []
for _ in range(word_length):
    display += "_"
# print(display)

while not end_of_game: #making end of game true
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You already guessed {guess}") #telling player alerady guessed letter is guessed

    #check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess: 
            display[position] = letter
            print(f"You have {lives} left.")
        
    #check if user is wrong
    if guess not in chosen_word:
        print(f"You guessed {guess} and that is not in the word. you lose a life")
        lives -= 1
        print(f"You have {lives} left")
        if lives == 0:
            end_of_game = True
            print("You lose.") 
        
    print(f"currently {' '.join(display)}")

        #check if user has got all the letters.
    if "_" not in display:
        end_of_game = True
        print("You win")

    print(stages[lives])
