from turtle import Turtle

LIGHT_GREY = 230, 230, 235
ALIGNMENT = "center"
FONT = ('Menlo', 20, 'normal')
Y_POSITION = 215


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.create_scoreboard()

    def create_scoreboard(self):
        self.hideturtle()
        self.penup()
        self.sety(Y_POSITION)
        self.color(LIGHT_GREY)
        self.show_score()

    def show_score(self):
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.show_score()

    def draw_game_over(self):
        self.sety(0)
        self.write(arg=f"Game Over!", align=ALIGNMENT, font=FONT)


