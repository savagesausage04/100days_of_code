from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.setposition(x=0, y=-220)
        self.x = 10
        self.y = 10
        self.speed = 0.08

    def move(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)

    def bounce_side_wall(self):
        self.x *= -1

    def bounce_top_wall(self):
        self.y *= -1

    def bounce_paddle(self):
        self.y *= -1

    def change_speed(self):
        self.speed = 0.05

    def reset(self):
        self.goto(0, 220)
        self.color("red")
        self.write("GAME OVER", align="center", font=("Courier", 60))
        # self.goto(0, -220)
        # self.speed = 0.1
        # self.x *= -1
        # self.y *= -1

    def win(self):
        self.goto(0, 220)
        self.color("green")
        self.hideturtle()
        self.write("YOU WIN!", align="center", font=("Courier", 60))




