from turtle import Turtle, Screen
import turtle as t
import random


#Challenge 1: Draw a box
timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)
# timmy_the_turtle.forward(100)

#Challenge 2: Draw a dashed line.
# for _ in range(10):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()

#Challenge 3: Draw all the shapes from triangle to decagon
# sides = 3
# for _ in range(0, 8):
#     angle = 360 / sides
#     for _ in range(0, sides):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(angle)
#     sides += 1

#Challenge 4: Draw the turtle walking in a random orientation.

t.colormode(255)

def random_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color = (red, green, blue)
    return color


# direction = [0, 90, 180, 270]
# timmy_the_turtle.pensize(5)
# timmy_the_turtle.speed(8)
# for _ in range(200):
#     timmy_the_turtle.color(random_color())
#     timmy_the_turtle.forward(20)
#     timmy_the_turtle.right(random.choice(direction))


#Challenge 5: Make a Spirograph
def make_spirograph(angle):
    timmy_the_turtle.speed(30)
    for _ in range(int(360 / angle)):
        timmy_the_turtle.circle(100)
        timmy_the_turtle.color(random_color())
        timmy_the_turtle.setheading(timmy_the_turtle.heading() + angle)

make_spirograph(5)

screen = t.Screen()
screen.exitonclick()
