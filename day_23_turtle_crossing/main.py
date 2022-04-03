from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FINISH_LINE_Y = 280


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")
screen.onkey(player.move, "w")
screen.onkey(player.move, "space")


game_is_on = True
while game_is_on:
    screen.update()

    manager.move_cars()

    # Check for win
    if player.ycor() > FINISH_LINE_Y:
        player.reset()
        manager.increase_speed()
        scoreboard.update_level()

    # Detect car collision
    if manager.check_collision(player):
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
