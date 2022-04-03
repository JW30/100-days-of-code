from turtle import Turtle
from paddle import Paddle

ALIGNMENT = "center"
FONT = ('Menlo', 30, 'normal')
LIGHT_GREY = 230, 230, 235


class Scoreboard(Turtle):

    def __init__(self, screen):
        super().__init__()
        self.hideturtle()
        self.color(LIGHT_GREY)
        self.screen = screen
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def draw_middle_line(self, screen):
        self.penup()
        self.sety(screen.window_height() / 2)
        self.pendown()

        while self.ycor() > - screen.window_height() / 2:
            self.sety(self.ycor() - 10)
            self.penup()
            self.sety(self.ycor() - 10)
            self.pendown()

        self.penup()

        self.sety(screen.window_height() / 2 - 50)

    def update_score(self, which_side=None):
        self.clear()
        self.draw_middle_line(self.screen)
        if which_side == Paddle.LEFT:
            self.l_score += 1
        if which_side == Paddle.RIGHT:
            self.r_score += 1
        self.write(arg=f"{self.l_score}" + " "*8 + f"{self.r_score}", align=ALIGNMENT, font=FONT)
