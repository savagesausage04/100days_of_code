from flask import Flask

app = Flask(__name__)

def bold_decorator(function):
    def wrapper_function():
        return f"<b>{function()}</b>"
    return wrapper_function

def italic_decorator(function):
    def wrapper_function():
        return f"<em>{function()}</em>"
    return wrapper_function

def underline_decorator(function):
    def wrapper_function():
        return f"<u>{function()}</u>"
    return wrapper_function

@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/bye")
@bold_decorator
@italic_decorator
@underline_decorator
def bye():
    return "Bye"

if __name__ == "__main__":
    app.run()


