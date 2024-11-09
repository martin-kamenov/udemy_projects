import random
from turtle import Turtle, Screen

screen = Screen()

def random_color():
    return random.choice(colors)


screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:  ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-80, -50, -20, 10, 40, 70]

for turtle_index in range(6):
    jimmy = Turtle(shape='turtle')
    jimmy.penup()
    jimmy.color(colors[turtle_index])
    jimmy.goto(x=-230, y=y_positions[turtle_index])

screen.exitonclick()