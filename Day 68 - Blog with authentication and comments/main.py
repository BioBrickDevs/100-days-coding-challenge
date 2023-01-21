from functools import wraps
from genericpath import exists
from flask import Flask, render_template, redirect, url_for, flash, request
from flask import abort
from flask_bootstrap import Bootstrap
from flask_ckeditor import CKEditor
from datetime import date
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from flask_login import UserMixin, login_user, LoginManager, login_required
from flask_login import current_user, logout_user
from forms import CreatePostForm, LoginForm, UserForm
from flask_gravatar import Gravatar

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'


login_manager = LoginManager()
login_manager.init_app(app)
ckeditor = CKEditor(app)
Bootstrap(app)


# CONNECT TO DB
app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class BlogPost(db.Model):
    __tablename__ = "blog_posts"
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, db.ForeignKey(
        "users.id"))
    author = relationship("User", back_populates="posts")
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    img_url = db.Column(db.String(250), nullable=False)


class User(UserMixin, db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    posts = relationship("BlogPost", back_populates="author")


def admin_only(f):
    @ wraps(f)
    def decorated_function(*args, **kwargs):
        # If id is not 1 then return abort with 403 error
        try:
            if current_user.id != 1:
                return abort(403)
        except AttributeError:
            return abort(403)
        # Otherwise continue with the route function
        return f(*args, **kwargs)
    return decorated_function


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# CONFIGURE TABLES


db.create_all()


@ app.route('/')
def get_all_posts():
    posts = BlogPost.query.all()
    for post in posts:
        print(post.author.username)

    return render_template("index.html", all_posts=posts)


@ app.route('/register', methods=["POST", "GET"])
def register():
    form = UserForm()
    if request.method == "POST" and form.validate():

        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]

        check_if_exist = User.query.filter_by(email=email).first()

        if check_if_exist:
            flash("You are already registered. "
                  "Login with your login details.")
            return redirect(url_for('login'))
        else:
            salted_and_hashed = generate_password_hash(password)

            new_user = User(username=username, email=email,
                            password=salted_and_hashed)
            login_user(new_user)
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('get_all_posts'))
    else:

        return render_template("register.html", form=form)


@ app.route('/login', methods=["POST", "GET"])
def login():
    form = LoginForm()
    if request.method == "POST" and form.validate():

        password = request.form["password"]
        email = request.form["email"]

        check_if_exist = User.query.filter_by(email=email).first()
        if check_if_exist:
            if check_password_hash(check_if_exist.password, password):
                login_user(check_if_exist)
                return redirect(url_for("get_all_posts"))
                # lodged in

            else:
                flash("Wrong password")
                return render_template("login.html", form=form)
                # not loged in
        else:
            # no user for that email
            flash("No user for email, Create a account")
            return render_template("login.html", form=form)

    if request.method == "GET":
        return render_template("login.html", form=form)


@ app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('get_all_posts'))


@ app.route("/post/<int:post_id>")
def show_post(post_id):
    requested_post = BlogPost.query.get(post_id)
    return render_template("post.html", post=requested_post)


@ app.route("/about")
def about():
    return render_template("about.html")


@ app.route("/contact")
def contact():
    return render_template("contact.html")


@ app.route("/new-post", methods=["GET", "POST"])
@ admin_only
def add_new_post():
    form = CreatePostForm()
    if form.validate_on_submit():
        new_post = BlogPost(
            author_id=current_user.id,
            title=form.title.data,
            subtitle=form.subtitle.data,
            body=form.body.data,
            img_url=form.img_url.data,
            author=current_user,
            date=date.today().strftime("%B %d, %Y")
        )
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("get_all_posts"))
    return render_template("make-post.html", form=form)


@ app.route("/edit-post/<int:post_id>", methods=["POST", "GET"])
@ admin_only
def edit_post(post_id):
    post = BlogPost.query.get(post_id)
    edit_form = CreatePostForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        body=post.body
    )
    if edit_form.validate_on_submit():
        post.title = edit_form.title.data
        post.subtitle = edit_form.subtitle.data
        post.img_url = edit_form.img_url.data
        post.body = edit_form.body.data
        db.session.commit()
        return redirect(url_for("show_post", post_id=post.id))

    return render_template("make-post.html", form=edit_form)


@ app.route("/delete/<int:post_id>")
@ admin_only
def delete_post(post_id):
    post_to_delete = BlogPost.query.get(post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))


if __name__ == "__main__":
    app.run(debug=True)
