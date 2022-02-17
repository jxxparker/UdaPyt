from game_data import data
import random
import os

def get_random_data():
    return random.choice(data)

def format_data(account):
    """This takes account and puts name, description and country accessible"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"name: {name}, description: {description}, country: {country}"

def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
    
def game():
    score = 0
    game_should_continue = True
    account_a = get_random_data()
    account_b = get_random_data()

    while game_should_continue:
        account_a = account_b
        account_b = get_random_data()

        while account_a == account_b:
          account_b = get_random_data()
        
        print(f"Compare A: {format_data(account_a)}. ")
        print("---VS---")
        print(f"Compare B: {format_data(account_b)}. ")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct  = check_answer(guess, a_follower_count, b_follower_count)

        os.system('clear')
        if is_correct:
            score += 1
            print("You are right")
            print(f"Current Score: {score}")
        else:
            game_should_continue = False
            print("You are wrong")
            print(f"Final Score: {score}")


game()