# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#
#     new_color = r, g, b
#     rgb_colors.append(new_color)

# colors = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]


import turtle as t_modul
import random


def random_color():
    return random.choice(colors)

def draw_dots_line():
    for _ in range(10):
        timmy.dot(20, random_color())
        timmy.penup()
        timmy.forward(50)
        timmy.pendown()


def start_new_row():
    timmy.penup()
    timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(180)
    timmy.forward(500)
    timmy.setheading(0)


def create_start_point():
    timmy.hideturtle()
    timmy.penup()
    timmy.setheading(225)
    timmy.forward(300)
    timmy.setheading(0)


t_modul.colormode(255)
colors = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
timmy = t_modul.Turtle()
timmy.speed('fastest')

create_start_point()

for row in range(10):
    draw_dots_line()
    start_new_row()

screen = t_modul.Screen()
screen.exitonclick()