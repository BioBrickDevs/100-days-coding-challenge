from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import tmdbsimple
import dotenv
import os
dotenv.load_dotenv()


TMDB_API_KEY = os.getenv("TMDB_API_KEY")
# The movie database API key.

tmdbsimple.API_KEY = TMDB_API_KEY
tmdbsimple.REQUESTS_SESSION = requests.Session()

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"


class Form(FlaskForm):
    rating = StringField('Your Rating Out of 10 e.g 7.5',
                         validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired()])

    submit = SubmitField()


class AddMovie(FlaskForm):
    movie_name = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField()


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    year = db.Column(db.Integer)
    description = db.Column(db.String)
    rating = db.Column(db.String)
    ranking = db.Column(db.String)
    review = db.Column(db.String)
    img_url = db.Column(db.String)


db.init_app(app)
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()

    return render_template("index.html", all_movies=all_movies)


@app.route("/edit/id/<int:id>", methods=["GET", "POST"])
def edit(id):
    form = Form()

    if request.method == "POST" and form.validate():
        new_rating = request.form['rating']
        new_review = request.form['review']
        movie_to_edit = Movie.query.get(id)
        movie_to_edit.rating = new_rating
        movie_to_edit.review = new_review
        db.session.commit()
        return redirect(url_for('home'))

    movie_to_find = Movie.query.get(id)
    return render_template("edit.html", form=form, title=movie_to_find.title)


@app.route("/delete/<int:id>", methods=["GET"])
def delete(id):

    movie_to_edit = Movie.query.get(id)
    db.session.delete(movie_to_edit)

    db.session.commit()
    return redirect(url_for('home'))


@app.route("/add_movie/", methods=["POST", "GET"])
def add_movie():
    form = AddMovie()
    if request.method == "POST" and form.validate():
        movie_to_find = request.form["movie_name"]

        search = tmdbsimple.Search()
        response = search.movie(query=movie_to_find)
        for result in search.results:
            print(result['id'])
            print(result["title"])
            print(result["poster_path"])
            print(result["release_date"])
            print(result["overview"])
        return render_template("select.html", results=search.results)

    return render_template("add.html", form=form)


@app.route("/find/<int:id>")
def find(id):
    print(id)
    movie = tmdbsimple.Movies(id)
    response = movie.info()
    print(movie.title, movie.poster_path,
          movie.release_date, movie.overview)

    try:
        img = "https://image.tmdb.org/t/p/original" + movie.poster_path
    except TypeError:
        img = "No image"

    new_movie = Movie(
        title=movie.title,
        year=movie.release_date,
        description=movie.overview,
        rating=None,
        ranking=None,
        review=None,
        img_url=img
    )
    db.session.add(new_movie)
    db.session.commit()
    movie_to_find = Movie.query.filter_by(title=movie.title).first()

    print(movie.id)
    return redirect(url_for('edit', id=movie_to_find.id))


if __name__ == '__main__':
    app.run(debug=True)
