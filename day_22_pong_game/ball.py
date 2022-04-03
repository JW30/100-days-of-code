import random
from turtle import Turtle
from paddle import Paddle

LIGHT_GREY = 230, 230, 235


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color(LIGHT_GREY)
        self.penup()
        self.set_angle()
        self.move_speed = 5

    def move(self):
        self.forward(self.move_speed)

    def bounce_wall(self):
        self.setheading(360 - self.heading())

    def bounce_paddle(self):
        self.setheading(540 - self.heading() % 360)
        self.move_speed *= 1.1

    def set_angle(self, scoring_paddle=None):
        # Sets random angle, can't be steeper than 60 degrees
        random_left = random.randint(120, 240)
        random_right = random.choice((random.randint(0, 60), random.randint(300, 359)))
        if scoring_paddle == Paddle.LEFT:
            ball_direction = random_left
        elif scoring_paddle == Paddle.RIGHT:
            ball_direction = random_right
        else:
            ball_direction = random.choice((random_left, random_right))
        self.setheading(ball_direction)

    def reset(self):
        self.goto(0, 0)
        self.move_speed = 5
