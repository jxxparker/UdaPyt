from random import randint

def play_game():
    print("Welcome to number guessing game")
    level = input("Choose Level Easy or Hard: ").lower()

    def easy_level():
        lives = 10
        answer = randint(1,100)
        print(f" this is answer {answer}")
        print(f" you have {lives} guesses")
        
        while lives != 0:
            guess = int(input("Please guess your number: "))
            if guess == answer:
                print("    You got it right")
                print("---Thank you for playing---")
                play_game
            elif guess != answer:
                lives -= 1
                print("  X Wrong!")
                print(f" You have {lives} guesses left")

                if guess > answer:
                    print("    Too high")
                elif answer > guess:
                    print("    Too low")
            
            if lives == 0:
                print("   You hit 0 lives. You lose")
                print("---Thank you for playing---")
                play_game
        
    def hard_level():
        lives = 5
        answer = randint(1,100)
        print(f" this is answer {answer}")
        print(f"you have {lives} guesses")
        
        while lives != 0:
            guess = int(input("Please guess your number: "))
            if guess == answer:
                print("    You got it right")
                print("---Thank you for playing---")
                play_game
            elif guess != answer:
                lives -= 1
                print("  X Wrong!")
                print(f" You have {lives} guesses left")

                if guess > answer:
                    print("    Too high")
                elif answer > guess:
                    print("    Too low")
            
            if lives == 0:
                print("   You hit 0 lives. You lose")
                print("---Thank you for playing---")
                play_game
            

    if level == "easy":
        easy_level()
    if level ==  "hard":
        hard_level()
    else:
        print("Please enter proper input")
    
play_game()