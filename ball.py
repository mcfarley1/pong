from turtle import Turtle
import random
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BALL_LENGTH = 1
BALL_WIDTH = 1
BALL_MOVE = 10
STANDARD_SIZE = 20
HEADING_LIST = [-BALL_MOVE, BALL_MOVE]



class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_len=BALL_LENGTH, stretch_wid=BALL_WIDTH)
        self.x_direction = BALL_MOVE
        self.y_direction = BALL_MOVE
        self.start_over()
        self.speed("fastest")

    def move(self):
        self.goto(self.xcor() + self.x_direction, self.ycor() + self.y_direction)


    def start_over(self):
        self.goto(0, random.randint(-int(SCREEN_HEIGHT / 2 - 30), int(SCREEN_HEIGHT / 2 - 30)))
        self.x_direction *= -1
