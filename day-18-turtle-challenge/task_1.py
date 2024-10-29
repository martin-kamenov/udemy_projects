from turtle import Turtle, Screen

def create_square():
    for _ in range(4):
        my_turtle.forward(100)
        my_turtle.right(90)


my_turtle = Turtle()

my_turtle.shape('turtle')
my_turtle.color('green')

create_square()

screen = Screen()
screen.exitonclick()