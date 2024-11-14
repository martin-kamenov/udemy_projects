import time
from turtle import Turtle, Screen


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

for position in starting_positions:
    new_segment = Turtle(shape="square")
    new_segment.penup()
    new_segment.color("white")
    new_segment.goto(position)
    segments.append(new_segment)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_number in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_number - 1].xcor()
        new_y = segments[seg_number - 1].ycor()
        segments[seg_number].goto(new_x, new_y)

    segments[0].forward(20)