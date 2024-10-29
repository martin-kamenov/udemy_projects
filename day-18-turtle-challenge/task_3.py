import turtle as t
import random

timmy = t.Turtle()
screen = t.Screen()
colors = ['blue', 'red', 'lime', 'dark violet', 'light salmon', 'cyan', 'spring green', 'pale violet red']

def draw_shape(sides_count):
    angel = 360 / sides_count

    for _ in range(sides_count):
        timmy.forward(100)
        timmy.right(angel)

for shape_side_count in range(3, 11):
    timmy.color(random.choice(colors))
    draw_shape(shape_side_count)

screen.exitonclick()