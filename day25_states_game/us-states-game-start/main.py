import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")

image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
while len(guessed_states) < 50:

    user_answer = screen.textinput(title=f"{len(guessed_states)} States Correct", prompt="Guess another state: ")
    upper_answer = user_answer.title()

    if upper_answer == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
    new_data = pandas.DataFrame(missing_states)
    new_data.to_csv("missing_states.csv")
    break


    if upper_answer in all_states:
        guessed_states.append(upper_answer)
        state_turtle = turtle.Turtle()
        state_turtle.hideturtle()
        state_turtle.penup()
        data_row = data[data.state == upper_answer]
        state_turtle.goto(int(data_row.x), int(data_row.y))
        state_turtle.write(upper_answer)



turtle.mainloop()
























# # import csv
# #
# #
# # with open("weather_data.csv") as file:
# #     data = csv.reader(file)
# #     temp = []
# #     for row in data:
# #         temperature = row[1]
# #         temp_int = int(temperature)
# #         temp.append(temp_int)
# #
# #     print(temp)
# #
# # import panda
# import csv
# import pandas
#
# data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# gray_squirrels_num = len(data[data["Primary Fur Color"] == "Gray"])
# cinnamon_squirrels_num = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrels_num = len(data[data["Primary Fur Color"] == "Black"])
#
#
# data_dictionary = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [gray_squirrels_num, cinnamon_squirrels_num, black_squirrels_num]
#
# }
#
# dataframe = pandas.DataFrame(data_dictionary)
# dataframe.to_csv("squirrel_count.csv")