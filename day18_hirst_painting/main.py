import colorgram
from turtle import Turtle, Screen
import random
import turtle as turtle1
# rgb = []
# colors = colorgram.extract('painting.jpeg', 50)
# for color in colors:
#     red = color.rgb.r
#     blue = color.rgb.b
#     green = color.rgb.g
#     new_colors = (red, blue, green)
#     rgb.append(new_colors)
#
# print(rgb)
turtle1.colormode(255)
color_list = [(244, 46, 235), (196, 34, 12), (221, 69, 159), (43, 178, 80), (238, 143, 39), (40, 68, 215), (238, 5, 229), (30, 154, 40), (23, 26, 147), (207, 22, 74), (202, 91, 34), (186, 9, 16), (19, 42, 18), (216, 191, 141), (57, 10, 15), (88, 28, 8), (227, 9, 161), (78, 157, 212), (67, 221, 73), (13, 61, 95), (78, 225, 194), (239, 215, 158), (94, 204, 233), (220, 48, 76), (15, 46, 67), (7, 238, 226), (100, 236, 226), (243, 155, 164), (170, 240, 175), (252, 60, 6), (5, 224, 245)]

timmy = Turtle()
timmy.speed(30)
timmy.penup()
timmy.hideturtle()
timmy.setpos(-220, -220)
for _ in range(5): #back and forth (2 rows)

    for _ in range(9):
        timmy.dot(20, color_list[random.randint(0, 30)])
        timmy.penup()
        timmy.forward(50)
    timmy.dot(20, color_list[random.randint(0, 30)])
    timmy.left(90)
    timmy.forward(50)
    timmy.left(90)
    for _ in range(9):
        timmy.dot(20, color_list[random.randint(0, 30)])
        timmy.penup()
        timmy.forward(50)
    timmy.dot(20, color_list[random.randint(0, 30)])
    timmy.right(90)
    timmy.forward(50)
    timmy.right(90)



screen = Screen()
screen.exitonclick()