import random
import colorgram
from turtle import Turtle, Screen

COLORS = [(c.rgb.r, c.rgb.g, c.rgb.b) for c in colorgram.extract("hirst-spot-painting.jpeg", 50)]
COLORS = [c for c in COLORS if all(x < 240 for x in c)]

WINDOW_SIZE = 500
DOTS = 10
BG_COLOR = (248, 247, 246)

tim = Turtle()
tim.hideturtle()
tim.speed("fastest")
screen = Screen()
screen.colormode(255)
screen.bgcolor(BG_COLOR)


def draw_hirst(window_size, dots):
    screen.setup(window_size, window_size)
    window_size -= 15
    dot_size = window_size / (dots * 2 - 1)
    tim.penup()
    x_start_pos = dot_size / 2 - screen.window_width() / 2 + 3
    tim.goto(x_start_pos, screen.window_width() / 2 - dot_size / 2 - 4)
    for _ in range(dots):
        for _ in range(dots):
            tim.dot(dot_size, random.choice(COLORS))
            tim.forward(dot_size * 2)
        tim.setx(x_start_pos)
        tim.sety(tim.ycor() - dot_size * 2)


draw_hirst(WINDOW_SIZE, DOTS)

screen.exitonclick()
