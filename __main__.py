from turtle import Screen
from .paddle import Paddle
from .ball import Ball
from .scoreboard import Scoreboard
from . import __doc__
import time
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
ORIGINAL_SLEEP = 0.05

def main():
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
    WINNING_SCORE = 11

    while True:
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
            if scoreboard.left_score == WINNING_SCORE:
                scoreboard.game_over(False)
                break
            ball.start_over()
            sleep_time = ORIGINAL_SLEEP

        elif ball.xcor() < -(SCREEN_WIDTH / 2):
            scoreboard.keep_right_score()
            if scoreboard.right_score == WINNING_SCORE:
                scoreboard.game_over(True)
                break
            ball.start_over()
            sleep_time = ORIGINAL_SLEEP

    screen.exitonclick()


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == 'help':
        print(__doc__)
    else:
        try:
            main()
        except:
            pass # so as not to print out the error message if the user x's out of the game early.
        print("See you again soon!")