from turtle import Turtle, Screen
import random
screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Make a bet", prompt="Which color turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
race_on = False
y_values = [-100, -60, -20, 20, 60, 100]
all_turtles = []
for turtle in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle])
    new_turtle.goto(x=-230, y=y_values[turtle])
    all_turtles.append(new_turtle)
if bet:
    race_on = True
while race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 220:
            race_on = False
            if bet == turtle.pencolor():
                print("You got it right!")
            else:
                print(f"Looks like the {turtle.pencolor()} turtle won!")
        turtle.forward(random.randint(10, 50))















screen.exitonclick()


