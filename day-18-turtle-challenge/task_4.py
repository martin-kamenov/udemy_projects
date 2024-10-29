import random
import turtle as t


timmy = t.Turtle()
screen = t.Screen()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return r, g, b

t.colormode(255)
directions = [0, 90, 180, 360]
timmy.speed('fastest')
timmy.pensize(10)

for _ in range(100):
    timmy.color(random_color())
    timmy.forward(20)
    timmy.setheading(random.choice(directions))

screen.exitonclick()