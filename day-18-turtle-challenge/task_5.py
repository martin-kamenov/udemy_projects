import random
import turtle as t

todor = t.Turtle
t.colormode(255)

def random_colour():
    red = random.randint(0, 255)
    blue = random.randint(0, 255)
    green = random.randint(0, 255)

    return red, blue, green

t.speed('fastest')
def draw_spirograph(gap_size):
    for _ in range(int(360 / gap_size)):
        t.color(random_colour())
        t.circle(50)
        t.setheading(t.heading() + gap_size)


draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()