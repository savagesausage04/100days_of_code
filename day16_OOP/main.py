# from turtle import Turtle, Screen
#
# teddy = Turtle()
# teddy.shape("turtle")
# teddy.color("coral")
# print(teddy)
# teddy.forward(100)
#
# my_screen = Screen()
# my_screen.exitonclick()
# print(my_screen.canvheight)

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])

print(table)