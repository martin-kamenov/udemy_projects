import random

from hangman_art import stages, logo
from hangman_words import word_list

lives = 6

chosen_word = random.choice(word_list)
print(chosen_word)

print(logo)

placeholder = '_' * len(chosen_word)
print(f"Word to guess: {placeholder}")

game_over = False
correct_letters = []

while not game_over:
    print(f"****************************<???>/{lives} LIVES LEFT****************************")

    guess = input("Guess a letter: ").lower()

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += guess
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1

        if lives == 0:
            game_over = True
            print(f"***********************IT WAS {chosen_word.upper()}! YOU LOSE**********************")

    if chosen_word == display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])
