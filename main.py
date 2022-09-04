from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
ORIGINAL_SLEEP = 0.05

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
screen.listen()

left_pos = (-(SCREEN_WIDTH / 2 - 50), 0)
right_pos = ((SCREEN_WIDTH / 2 - 50), 0)
left_paddle = Paddle(left_pos)
right_paddle = Paddle(right_pos)
ball = Ball()
scoreboard = Scoreboard()

screen.onkeypress(left_paddle.move_up, "w")
screen.onkeypress(left_paddle.move_down, "s")
screen.onkeypress(right_paddle.move_up, "Up")
screen.onkeypress(right_paddle.move_down, "Down")

sleep_time = ORIGINAL_SLEEP
counter = 0
counter_max = 20
game_is_on = True

while game_is_on:
    time.sleep(sleep_time)
    screen.update()
    ball.move()

    # Ball bounces off of vertical limits.
    if ball.ycor() > (SCREEN_HEIGHT / 2 - 20) or ball.ycor() < -(SCREEN_HEIGHT / 2 - 20):
        ball.y_direction *= -1

    # Ball reaches horizontal limits.
    if ball.xcor() == (SCREEN_WIDTH / 2 - 60) and \
            right_paddle.top_edge() >= ball.ycor() >= right_paddle.bottom_edge() or \
            ball.xcor() == -(SCREEN_WIDTH / 2 - 60) and \
            left_paddle.top_edge() >= ball.ycor() >= left_paddle.bottom_edge():
        ball.x_direction *= -1
        sleep_time *= 0.9

    elif ball.xcor() > (SCREEN_WIDTH / 2):
        scoreboard.keep_left_score()
        counter += 1
        if counter == counter_max:
            scoreboard.game_over()
            break
        ball.start_over()
        sleep_time = ORIGINAL_SLEEP

    elif ball.xcor() < -(SCREEN_WIDTH / 2):
        scoreboard.keep_right_score()
        counter += 1
        if counter == counter_max:
            scoreboard.game_over()
            break
        ball.start_over()
        sleep_time = ORIGINAL_SLEEP

screen.exitonclick()
