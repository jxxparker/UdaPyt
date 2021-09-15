from random import randint

print("Welcome to the number guessing game!")
print("I am thinking of a number between 1 and 100")
game_level = input("Choose a difficulty. type 'easy' or 'hard': ")

def easy_level():
    life_acc = 10
    answer = randint(1, 100)
    
    print(f"you have {life_acc} guesses")
    
    while life_acc != 0:

        player_guess = int(input("guess a number: "))
        if player_guess != answer:
            life_acc -= 1
            print(f"wrong: you have {life_acc} guesses left")
                
            if player_guess > answer:
                print("too high")
            elif player_guess < answer:
                print("too low")
        else:
            print(f"you got it right. the answer was {answer}")
            life_acc = 0

def hard_level():
    life_acc = 5
    answer = randint(1, 100)
    
    print(f"you have {life_acc} guesses")
    
    while life_acc != 0:

        player_guess = int(input("guess a number: "))
        
        if player_guess != answer:
            life_acc -= 1
            print(f"wrong: you have {life_acc} guesses left")
                
            if player_guess > answer:
                print("too high")
            elif player_guess < answer:
                print("too low")
        
        else:
            print(f"you got it right. the answer was {answer}")
            life_acc = 0

if game_level == "easy":
    easy_level()
elif game_level == "hard":
    hard_level()
else:
    print("please enter proper game level")

