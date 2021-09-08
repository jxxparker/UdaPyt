deck_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []
import random

def deal_card():
    deck_cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(deck_cards)
    return card

for run in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    
def calculate_score():
    if sum(deck_cards) == 21 and len(deck_cards) == 2:
        return 69
    #--------------
    if 11 in cards and sum(deck_cards) > 21:
        deck_cards.remove(11)
        deck_cards.append(1)

    return sum(deck_cards)

user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

print(f" your cards: {user_cards}, current score: {user_score}")
print(f" computer's first card: {computer_cards[0]}")

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
