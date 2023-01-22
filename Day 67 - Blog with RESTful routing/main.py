from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
import datetime as dt

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)


# CONNECT TO DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# CONFIGURE TABLE


class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


# WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


@app.route('/')
def get_all_posts():
    get_all_posts = db.session.query(BlogPost).all()

    return render_template("index.html", all_posts=get_all_posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    post = BlogPost.query.get(index)
    requested_post = post
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/new-post", methods=["GET", "POST"])
def new_post():
    form = CreatePostForm()

    if form.validate() and request.method == "POST":

        title = form.data["title"]
        subtitle = form.data["subtitle"]
        author = form.data["author"]
        img_url = form.data["img_url"]
        body = form.data["body"]

        now = dt.datetime.now()

        formated_now = now.strftime("%B %-d, %Y")

        new_post = BlogPost(
            title=title,
            subtitle=subtitle,
            date=formated_now,
            body=body,
            author=author,
            img_url=img_url,
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('get_all_posts'))

    return render_template("make-post.html", form=form)


@app.route("/edit-post/<int:id>", methods=["GET", "POST"])
def edit_post(id):
    form = CreatePostForm()
    if request.method == "POST" and form.validate:
        values = list(request.form.values())
        update = {}
        for index, key in enumerate(request.form):
            update[key] = values[index]
        del update["csrf_token"]
        del update["submit"]

        old_post = BlogPost.query.get(id)
        update["date"] = old_post.date
        update_to_post = BlogPost(**update)
        update_to_post.id = id

        db.session.delete(old_post)
        db.session.add(update_to_post)
        db.session.commit()

        # print(update_to_post)
        return redirect(url_for('get_all_posts'))
    if request.method == "GET":
        post_to_edit = BlogPost.query.get(id)
        form = CreatePostForm(obj=post_to_edit)
        return render_template("make-post.html", form=form, edit_post=True)


@app.route("/delete/<int:id>")
def delete(id):
    post_to_delete = BlogPost.query.get(id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


if __name__ == "__main__":
    app.run(debug=True)
