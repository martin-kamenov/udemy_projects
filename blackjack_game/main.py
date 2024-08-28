import random
import art

def deal_card():
    """Return random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards: list):
    """Takes a list of cards and return the calculated score of them."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score_, computer_score_):
    """Compare user score against computer score."""
    if user_score_ == computer_score_:
        return "Draw"
    elif computer_score_ == 0:
        return "Opponent has a blackjack. You lose."
    elif user_score_ == 0:
        return "Blackjack. You win."
    elif user_score_ > 21:
        return "You went over 21. You lose."
    elif computer_score_ > 21:
        return "Opponent went over 21. You win"
    elif user_score_ > computer_score_:
        return "You win."
    else:
        return "You lose."


def play_game():
    print(art.logo)
    user_cards = []
    computer_cards = []

    user_score = -1
    computer_score = -1

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    game_over = False

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_draw_another_card = input("Type 'y' to get another card, type 'n' to pass: ")

            if user_draw_another_card == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()