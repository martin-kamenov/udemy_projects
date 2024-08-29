from random import randint
from art import logo


EASY_MODE = 10
HARD_MODE = 5


def get_difficulty(level):
    if level == "easy":
        return EASY_MODE
    else:
        return HARD_MODE


def check_answer(u_guess, answer, turns):
    if u_guess > answer:
        print("Too high.")
        return turns - 1
    elif u_guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}")


def play_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")

    answer = randint(1, 100)
    turns = get_difficulty(level)
    print(f"Number is {answer}")

    while turns:
        print(f"You have {turns} attempts remaining to guess the number.")

        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)

        if guess == answer:
            return
        elif turns > 0:
            print("Guess again.")

    else:
        print("You've run out of guesses, you lose.")


play_game()