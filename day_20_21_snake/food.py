import random
from turtle import Turtle

X_RANGE = range(-340, 321, 20)
Y_RANGE = range(-220, 240, 20)


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("yellow")
        self.speed("fastest")
        self.refresh()

    def refresh(self, segments=[]):
        new_pos = random.choice(X_RANGE), random.choice(Y_RANGE)
        while any(segment.distance(new_pos) < 1 for segment in segments):
            new_pos = random.choice(X_RANGE), random.choice(Y_RANGE)
        self.goto(new_pos)
