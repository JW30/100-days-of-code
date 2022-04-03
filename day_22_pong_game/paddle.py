from turtle import Turtle

LIGHT_GREY = 230, 230, 235
PADDLE_HEIGHT = 5
PADDLE_WIDTH = 1
SPEED = 50


class Paddle(Turtle):
    LEFT = 0
    RIGHT = 1

    def __init__(self, x_pos):
        super().__init__()
        self.color(LIGHT_GREY)
        self.shape("square")
        self.shapesize(PADDLE_HEIGHT, PADDLE_WIDTH)
        self.penup()
        self.setx(x_pos)

    def go_up(self):
        self.sety(self.ycor() + SPEED)

    def go_down(self):
        self.sety(self.ycor() - SPEED)
