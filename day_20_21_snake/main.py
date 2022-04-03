from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

DARK_GREY = 25, 25, 30
WINDOW_WIDTH, WINDOW_HEIGHT = 700, 500  # Do not change!
SLEEP_TIME = 0.08
EAT_DISTANCE = 15

screen = Screen()
screen.setup(WINDOW_WIDTH, WINDOW_HEIGHT)
screen.colormode(255)
screen.bgcolor(DARK_GREY)
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(SLEEP_TIME)

    snake.move()

    if snake.is_colliding():
        scoreboard.save_high_score()
        scoreboard.reset_score()
        snake.reset()

    if snake.head.distance(food) < EAT_DISTANCE:
        food.refresh(snake.segments)
        snake.add_new_segment()
        scoreboard.increase_score()
