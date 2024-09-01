from flask import Flask
import random
app = Flask(__name__)

number = random.randint(1, 9)

@app.route("/")
def introduce():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/ysMx3dTbUtp95u6aJ2/giphy.gif'>"

@app.route("/<int:user_input>")
def check_num(user_input):
    if user_input > number:
        return "<h1>The number is too high!</h1>" \
               "<img src='https://media.giphy.com/media/5h9qt9hnglkMp21Bty/giphy.gif'>"

    elif user_input < number:
        return "<h1>The number is too low!</h1>" \
               "<img src='https://media.giphy.com/media/5h9qt9hnglkMp21Bty/giphy.gif'>"

    elif user_input == number:
        return "<h1>You got it!</h1>" \
               "<img src='https://media.giphy.com/media/3o7abKhOpu0NwenH3O/giphy.gif'>"



if __name__ == "__main__":
    app.run()
