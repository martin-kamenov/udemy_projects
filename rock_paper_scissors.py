import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

computer_choice = random.randint(0, 2)

statement = ""
if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
    raise SystemExit
elif user_choice == 0 and computer_choice == 2:
    statement = "You win"
elif user_choice == 2 and computer_choice == 0:
    statement = "You lose"
elif user_choice > computer_choice:
    statement = "You win"
elif user_choice < computer_choice:
    statement = "You lose"
elif user_choice == computer_choice:
    statement = "Draw"

print(game_images[user_choice])

print("Computer chose:")
print(game_images[computer_choice])

print(statement)