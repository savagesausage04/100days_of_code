from flask import Flask, render_template, request
import requests
from email.message import EmailMessage
import ssl
import smtplib

email_sender = "kylieh1104@gmail.com"
email_receiver = "kyleh1104@gmail.com"
subject = "Someone Messaged You!"

app = Flask(__name__)
endpoint = "https://api.npoint.io/7230603669dfcae807bc"
blogs = requests.get(endpoint).json()
@app.route("/")
def home():
    return render_template("index.html", posts=blogs)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        name = request.form["username"]
        email = request.form["email"]
        phone_num = request.form["phone"]
        message = request.form["message"]
        body = f"Name: {name}\nEmail: {email}\nPhone Number: {phone_num}\nMessage: {message}"
        em = EmailMessage()
        em["From"] = email
        em["To"] = email_receiver
        em["Subject"] = "Someone Contacted You!"
        em.set_content(body)
        email_password = "jkismqutbbdencoi"
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())


    return render_template("contact.html")









@app.route("/post/<int:num>")
def post(num):
    requested_post = None
    for blog_post in blogs:
        if blog_post["id"] == num:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)



if __name__ == "__main__":
    app.run(debug=True)