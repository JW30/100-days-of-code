from turtle import Turtle

LIGHT_GREY = 230, 230, 235


class Segment(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(LIGHT_GREY)
        self.penup()
