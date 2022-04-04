from turtle import Turtle
import data

ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")
SCORE_FONT = ("Menlo", 22, "normal")


class Drawer(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()

    def draw_state_name(self, state):
        self.goto(data.get_state_pos(state))
        self.write(arg=f"{state}", align=ALIGNMENT, font=FONT)

    def draw_remaining(self, guessed_states):
        self.color("red")
        for state in data.get_missing_states(guessed_states):
            self.draw_state_name(state)
        self.color("black")

    def draw_score(self, guessed_states):
        self.goto(200, 200)
        self.write(arg=f"Score: {len(guessed_states)}/50", align=ALIGNMENT, font=SCORE_FONT)
