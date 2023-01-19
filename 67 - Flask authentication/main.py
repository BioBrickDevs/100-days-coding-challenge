from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# CREATE TABLE IN DB
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
# Line below only required once, when creating DB.
# db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=["POST", "GET"])
def register():
    if request.method == "POST":
        values = list(request.form.values())
        update = {}
        for index, key in enumerate(request.form):
            update[key] = values[index]

        data = User.query.filter_by(email=update["email"]).first()
        print(data)
        if data:
            flash("User account already exits.")
            return redirect(url_for('login'))

        else:
            update["password"] = generate_password_hash(update["password"])
            new_user_to_table = User(**update)
            db.session.add(new_user_to_table)
            db.session.commit()

            return redirect(url_for('secrets'))

    if request.method == "GET":

        return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        values = list(request.form.values())
        update = {}
        for index, key in enumerate(request.form):
            update[key] = values[index]

        user = User.query.filter_by(email=update["email"]).first()
        if not user:
            flash("Email does not exits")
            return render_template("login.html")

        if check_password_hash(user.password, update["password"]):
            login_user(user)
            flash("you were logged in")
            return redirect(url_for("secrets"))
        else:
            flash("Wrong password, try again")
            return render_template("login.html")


@app.route('/secrets')
@login_required
def secrets():
    name = current_user.name
    return render_template("secrets.html", name=name)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory(directory="./static/files", path='cheat_sheet.pdf')


if __name__ == "__main__":
    app.run(debug=True)
