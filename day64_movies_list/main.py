from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

API_KEY = "44c5139687c72bd8701d0124239bcbf9"

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///movies.db'


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable=False)
    rating = db.Column(db.Float, nullable=True, unique=False)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(250), nullable=True)
    img_url = db.Column(db.String(250), nullable=False)

db.create_all()

# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# db.session.add(new_movie)
# db.session.commit()

class RateMovieForm(FlaskForm):
    new_rating = StringField('Your rating out of 10', validators=[DataRequired()])
    new_review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Done')

class AddMovieForm(FlaskForm):
    movie_title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')

@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)

@app.route("/find")
def find():
    api_id = request.args.get("id")
    if api_id:
        api_url = f"https://api.themoviedb.org/3/movie/{api_id}"
        response = requests.get(api_url, params={"api_key": API_KEY})
        data = response.json()
        print(data)
        new_movie = Movie(
            title=data["title"],
            year=data["release_date"].split("-")[0],
            img_url=f"https://image.tmdb.org/t/p/w500{data['poster_path']}",
            description=data["overview"],
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("edit", id=new_movie.id))


@app.route("/edit", methods=["GET", "POST"])
def edit():
    form = RateMovieForm()
    movie_id = request.args.get('id')
    movie = Movie.query.get(movie_id)
    print(movie)
    if form.validate_on_submit():
        movie.rating = float(form.new_rating.data)
        movie.review = form.new_review.data
        db.session.commit()
        return redirect(url_for('home'))

    return render_template("edit.html", form=form, movie=movie)

@app.route("/delete")
def delete():
    movie_id = request.args.get('id')
    movie = Movie.query.get(movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/add", methods=["GET", "POST"])
def add():
    movie_to_add = AddMovieForm()
    if movie_to_add.validate_on_submit():
        movie_title = movie_to_add.movie_title.data
        response = requests.get('https://api.themoviedb.org/3/search/movie', params={"api_key": API_KEY, "query": movie_title})
        data = response.json()["results"]
        return render_template('select.html', options=data)
    return render_template('add.html', form=movie_to_add)


if __name__ == '__main__':
    app.run()
