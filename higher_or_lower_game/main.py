import random
from art import logo, vs
from game_data import data


def display_account(account):
    """Takes the account data and returns the printable format."""
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']

    return f"{account_name}, a {account_description}, from {account_country}."

def check_answer(user_guess, a_followers, b_followers):
    """Takes user's guess and the count of followers and returns if they got it correct."""
    if a_followers > b_followers:
        return user_guess == 'A'
    else:
        return user_guess == 'B'

print(logo)
user_score = 0
account_b = random.choice(data)
on_streak = True

while on_streak:
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {display_account(account_a)}")
    print(vs)
    print(f"Against B: {display_account(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    account_a_followers = account_a['follower_count']
    account_b_followers = account_b['follower_count']

    print("\n" * 20)
    print(logo)

    is_correct = check_answer(guess, account_a_followers, account_b_followers)

    if is_correct:
        user_score += 1
        print(f"You're correct! Current score: {user_score}")
    else:
        print(f"Sorry, that's wrong. Final score: {user_score}")
        on_streak = False