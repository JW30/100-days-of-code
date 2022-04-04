import turtle
from turtle import Screen
from drawer import Drawer
import data

screen = Screen()
screen.setup(width=725, height=491)
screen.bgpic("blank_states_img.gif")
screen.title("Can you name the US states?")
screen.tracer(0)

drawer = Drawer()
guessed_states = []

while len(guessed_states) < 50:
    answer = screen.textinput(f"Score: {len(guessed_states)}/50", "Enter State:").title()
    if answer.lower() == "quit":
        drawer.draw_score(guessed_states)
        drawer.draw_remaining(guessed_states)
        data.save_missing_states(guessed_states)
        break
    elif answer not in guessed_states and data.state_exists(answer):
        drawer.draw_state_name(answer)
        guessed_states.append(answer)

drawer.draw_score(guessed_states)


turtle.mainloop()
