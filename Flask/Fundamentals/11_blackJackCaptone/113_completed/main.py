############### Blackjack Project #####################
import random #import random fxn
import os     #this is to import clear
from art import logo   

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card(): #deals random card
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card

def calculate_score(cards): #calculating scores
    if sum(cards) == 21 and len(cards) == 2: #sum(cards) adding cards up.
        return 99 #return 21 because it's blackjack
    
    if 11 in cards and sum(cards) > 21: #turning 11 into 1
        cards.remove(11)
        cards.append(1)
    return sum(cards) #this is where cards get added up

def compare(user_score, computer_score): #comparing each results
    if user_score == computer_score:
        return "DRAW"
    elif computer_score == 99:
        return "LOSE: Computer Blackjack"
    elif user_score == 99:
        return "WIN: PLAYER BLACKJACK"
    elif user_score > 21:
        return "LOSE: PLAYER OVER 21"
    elif computer_score > 21:
        return "WIN COMPUTER OVER 21"
    elif user_score > computer_score:
        return "WIN: PLAYER HIGHER SCORE"
    elif computer_score > user_score:
        return "LOSE: COMPUTER HIGHER SCORE"

def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:

        user_score = calculate_score(user_cards) #calling calculate score from above for player
        computer_score = calculate_score(computer_cards) #calling calculate score from above for computer
        print(f"   Player Cards: {user_cards} || Current Score: {user_score}")
        print(f"   Computer's first card {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to get pass: ").lower()
            if user_should_deal == 'y':
                user_cards.append(deal_card()) #deals random card
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)


    print(f"   Player Final Hands: {user_cards} || Player Final Score: {user_score}")
    print(f"   Computer's final hand: {computer_cards} || Computer Final score: {computer_score}")
    print(compare(user_score, computer_score))

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
while input("Do you want to play a game of blackjack? 'Y' or 'N' ").lower() == "y":
    os.system('clear')
    play_game()