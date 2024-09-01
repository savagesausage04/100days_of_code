from flask import Flask, render_template
from datetime import date
import requests
import random

app = Flask(__name__)

@app.route("/")
def home():
    random_number = random.randint(1, 10)
    current_year = date.today().year
    return render_template("index.html", current_year=current_year, num=random_number)

@app.route("/guess/<name>")
def guess(name):
    gender_url = f"https://api.genderize.io?name={name}"
    response = requests.get(gender_url)
    data = response.json()
    gender = data["gender"]

    age_url = f"https://api.agify.io?name={name}"
    response = requests.get(age_url)
    data = response.json()
    age = data["age"]
    return render_template("guess.html", name=name, gender=gender, age=age)

@app.route("/blog/<num>")
def get_blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)
