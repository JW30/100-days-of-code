import time
from turtle import Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball

DARK_GREY = 25, 25, 30

screen = Screen()
screen.setup(800, 600)
screen.colormode(255)
screen.bgcolor(DARK_GREY)
screen.tracer(0)

scoreboard = Scoreboard(screen)

l_paddle = Paddle(-screen.window_width() / 2 + 40)
r_paddle = Paddle(screen.window_width() / 2 - 40)

ball = Ball()

screen.listen()

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True


def _score_point(which_paddle):
    scoreboard.update_score(which_paddle)
    ball.reset()
    ball.set_angle(which_paddle)
    screen.update()
    time.sleep(1)


while game_is_on:
    screen.update()
    ball.move()

    # Detect collision with walls
    if ball.ycor() > screen.window_height() / 2 - 10 or ball.ycor() < - screen.window_height() / 2 + 10:
        ball.bounce_wall()

    # Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > screen.window_width() / 2 - 50 or ball.distance(
            l_paddle) < 50 and ball.xcor() < - screen.window_width() / 2 + 50:
        ball.bounce_paddle()

    # Detect if left player scores a point
    if ball.xcor() > screen.window_width() / 2 - 10:
        _score_point(Paddle.LEFT)

    # Detect if right player scores a point
    if ball.xcor() < - screen.window_width() / 2 + 10:
        _score_point(Paddle.RIGHT)


screen.exitonclick()
