from turtle import Turtle
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.left_score = 0
        self.right_score = 0
        self.update_score()

    def update_score(self):
        self.dotted_line()
        self.goto(0, SCREEN_HEIGHT / 2 - 30)
        self.write(f"{self.left_score}        {self.right_score}", move=False, align='center',
                   font=('Arial', 16, 'normal'))

    def keep_left_score(self):
        self.clear()
        self.left_score += 1
        self.update_score()

    def keep_right_score(self):
        self.clear()
        self.right_score += 1
        self.update_score()

    def dotted_line(self):
        self.goto(0, SCREEN_HEIGHT / 2)
        self.setheading(270)
        for num in range(int(SCREEN_HEIGHT / 20)):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)

    def game_over(self, right_wins):
        winner = 'RIGHT' if right_wins else 'LEFT'
        self.goto(0, 0)
        self.write(f"{winner} PLAYER WINS!", move=False, align='center', font=('Arial', 16, 'normal'))
