from turtle import Turtle

class Blocks(Turtle):
    def __init__(self, x_pos, y_pos, color):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.penup()
        self.setposition(x_pos, y_pos)
