from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(x_pos, y_pos)

    def go_left(self):
        new_x = self.xcor() - 30
        self.goto(new_x, self.ycor())

    def go_right(self):
        new_x = self.xcor() + 30
        self.goto(new_x, self.ycor())