from art import logo, vs
from game_data import data
import random

def format_data(account):
    """format the account data into printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_followers, b_followers):
    """take the user guess and follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

print(logo) 

#Generate a random account from the game data.
account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:  #this will generate new random account_b if it gets same result as account_a
    account_b = random.choice(data) 

print(f"compare A: {format_data(account_a)}")
print(vs)
print(f"Against B: {format_data(account_b)}")

# Ask user for a guess.
guess = input("Who has more followers? Type 'A' or 'B': ").lower()

# Check if user is correct.
## Get follower count.
a_follower_account = account_a["follower_count"]
b_follower_account = account_b["follower_count"]
is_correct = check_answer(guess, a_follower_account, b_follower_account)

# Feedback.
if is_correct:
    print("You're right")
else:
    print("Sorry that's wrong")
# Score Keeping.

# Make game repeatable.

# Make B become the next A.

# Add art.

# Clear screen between rounds.