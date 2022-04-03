from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.setposition(STARTING_POSITION)
        self.shape("turtle")
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def reset(self):
        self.setposition(STARTING_POSITION)
