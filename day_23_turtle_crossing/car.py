import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
SPEED_MULTIPLIER = 1.2
STARTING_MAX_SPEED = 15


class Car(Turtle):

    def __init__(self):
        super().__init__()

        self.penup()
        self.shape("square")
        self.setheading(180)
        self.shapesize(1, 3)
        self.color(random.choice(COLORS))
        self.max_speed = STARTING_MAX_SPEED
        self.move_speed = None
        self.reset()

    def move(self):
        self.forward(self.move_speed)

    def reset(self):
        self.setx(random.randint(320, 620))
        self.sety(random.randint(-240, 250))
        self.move_speed = random.randint(self.max_speed // 2, int(self.max_speed)) / 10

    def increase_speed(self):
        self.max_speed *= SPEED_MULTIPLIER
        self.move_speed *= SPEED_MULTIPLIER
