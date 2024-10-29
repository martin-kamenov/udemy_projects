from turtle import Turtle, Screen


def cross_line():
    for _ in range(4):
        t.forward(10)
        t.up()
        t.forward(10)
        t.down()


t = Turtle()
screen = Screen()

for _ in range(15):
    cross_line()

screen.exitonclick()