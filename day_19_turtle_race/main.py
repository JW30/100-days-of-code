import random
from turtle import Turtle, Screen

COLORS = ["yellow", "orange", "red", "purple", "blue", "green"]

screen = Screen()
screen.colormode(255)
screen.bgcolor(75, 75, 77)
screen.setup(500, 400)

bet = screen.textinput("Make your bet", "Who will win the race? Enter a color:")

turtles = []

y = 75
for color in COLORS:
    new_turtle = Turtle("turtle")
    new_turtle.color(color)
    turtles.append(new_turtle)
    new_turtle.penup()
    new_turtle.goto(-230, y)
    y -= 30

winner_color = None
while not winner_color:
    for turtle in turtles:
        turtle.forward(random.randint(0, 10))
        if turtle.xcor() > 230:
            winner_color = turtle.pencolor()
            break

if winner_color == bet.lower():
    print(f"Congratulations! {bet.capitalize()} won the race! :)")
else:
    print(f"You lose. {winner_color.capitalize()} won the race. :(")

screen.exitonclick()
