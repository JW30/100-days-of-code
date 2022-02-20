import random
import colorgram
from turtle import Turtle, Screen

COLORS = [(c.rgb.r, c.rgb.g, c.rgb.b) for c in colorgram.extract("hirst-spot-painting.jpeg", 50)]
COLORS = [c for c in COLORS if all(x < 240 for x in c)]

WINDOW_SIZE = 487
DOT_SIZE = 25
BG_COLOR = (248, 247, 246)

tim = Turtle()
tim.hideturtle()
tim.speed("fastest")
screen = Screen()
screen.colormode(255)
screen.bgcolor(BG_COLOR)

screen.setup(WINDOW_SIZE, WINDOW_SIZE)
tim.penup()
tim.goto(DOT_SIZE / 2 - screen.window_width() / 2 + 1, screen.window_width() / 2 - DOT_SIZE / 2 - 1)
for _ in range(10):
    for _ in range(10):
        tim.dot(DOT_SIZE, random.choice(COLORS))
        tim.forward(DOT_SIZE * 2)
    tim.setx(DOT_SIZE / 2 - screen.window_width() / 2 + 1)
    tim.sety(tim.ycor() - DOT_SIZE * 2)

screen.exitonclick()
