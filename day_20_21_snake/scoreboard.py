from turtle import Turtle

LIGHT_GREY = 230, 230, 235
ALIGNMENT = "center"
FONT = ('Menlo', 20, 'normal')
Y_POSITION = 215


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self._get_high_score()
        self.create_scoreboard()

    def create_scoreboard(self):
        self.hideturtle()
        self.penup()
        self.sety(Y_POSITION)
        self.color(LIGHT_GREY)
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(arg=f"Score: {self.score}" + " "*3 + f"Best: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.show_score()

    def reset_score(self):
        self.score = 0
        self.show_score()

    @staticmethod
    def _get_high_score():
        with open("highscore.txt", "r") as f:
            return int(f.read())

    def save_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt", "w") as f:
                f.write(str(self.high_score))
