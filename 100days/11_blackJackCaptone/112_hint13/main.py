set_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card. 11 is the Ace.
import random
import os

def deal_card():
    """returns a random card from the deck"""
    set_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(set_cards)
    return card

#Hint 6: Create a function called calculate_score() that takes a List of cards as input and returns the score. Look up the sum() function to help you do this.
def calculate_score(set_cards):
    """take a list of set_cards and return the score calculated from the set_cards"""
    #Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    if sum(set_cards) == 21 and len(set_cards) == 2:
        return 0 #black jack completed

    #Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().\
    if 11 in set_cards and sum(set_cards) > 21:
        set_cards.remove(11)
        set_cards.append(1)

    return sum(set_cards)

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has blackjack"
    elif user_score == 0:
        return "Win, you have a blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "oppoent went over. you win"
    elif user_score > computer_score:
        return "you win"
    elif computer_score < user_score:
        return "you lose"
    else:
        return "malfunctioned"

def play_game():
#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
    user_cards = []
    computer_cards = []
    is_game_over = False 

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    #Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
    while not is_game_over:    

    #Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f" your cards: {user_cards}, current score: {user_score} ")
        print(f" computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
            user_should_deal = input("Type 'y' to get another cards, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    #Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f" Your final hand: is {user_cards}, final score: {user_score}")
    print(f" computer final hand: is {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
while input("Do you want to play a game of blackjack? type? 'y' or 'n':") == "y":
    os.system('clear')
    play_game()