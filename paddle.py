from turtle import Turtle
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PADDLE_LENGTH = 5
PADDLE_WIDTH = 1
PADDLE_MOVE = 20
STANDARD_SIZE = 20


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_len=PADDLE_LENGTH, stretch_wid=PADDLE_WIDTH)
        self.setheading(90)
        self.goto(position)
        self.speed("fastest")

    def move_up(self):
        top_edge = self.top_edge()
        if top_edge < (SCREEN_HEIGHT / 2 - 10):
            self.goto(self.xcor(), self.ycor() + PADDLE_MOVE)

    def move_down(self):
        bottom_edge = self.bottom_edge()
        if bottom_edge > -(SCREEN_HEIGHT / 2 - 10):
            self.goto(self.xcor(), self.ycor() - PADDLE_MOVE)

    def top_edge(self):
        return self.ycor() + STANDARD_SIZE * PADDLE_LENGTH / 2

    def bottom_edge(self):
        return self.ycor() - STANDARD_SIZE * PADDLE_LENGTH / 2
