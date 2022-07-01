from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.setposition(x=0, y=0)
        self.x = 10
        self.y = 10 #amount of pixels it moves
        self.speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)

    def bounce_wall(self):
        self.y *= -1

    def bounce_paddle(self):
        self.x *= -1
        self.speed *= 0.85

    def reset(self):
        self.goto(0, 0)
        self.speed = 0.1
        self.x *= -1
        self.y *= -1
