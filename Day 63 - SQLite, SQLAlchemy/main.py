
from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from flask_sqlalchemy import SQLAlchemy


connection = sqlite3.connect("books-collection.db")

db = SQLAlchemy()
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books-collection.db"


db.init_app(app)

all_books = []


class BookRating(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    rating = db.Column(db.Float,)


with app.app_context():

    db.create_all()


@ app.route('/')
def home():
    all_books = db.session.query(BookRating).all()

    return render_template("index.html", all_books=all_books)


@ app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        book_name = request.form['book_name']
        book_author = request.form['book_author']
        book_rating = request.form['book_rating']
        book = BookRating(book=book_name,
                          author=book_author, rating=book_rating)
        db.session.add(book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html")


@app.route("/edit/id/<int:id>", methods=["GET", "POST"])
def edit(id):
    if request.method == "POST":
        book = BookRating.query.get(id)
        new_value = request.form['value']
        book.rating = new_value
        db.session.commit()
        return redirect(url_for('home'))
    book = BookRating.query.get(id)
    print(book.book)
    return render_template("edit.html", book=book)


@app.route("/delete/<int:id>")
def delete(id):
    book_id = id
    book_to_delete = BookRating.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
