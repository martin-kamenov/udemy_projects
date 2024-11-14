from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

for position in starting_positions:
    new_block = Turtle(shape='square')
    new_block.color('white')
    new_block.goto(position)

screen.exitonclick()