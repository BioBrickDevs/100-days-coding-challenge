from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
app.secret_key = "rleajrelajrlkeajrlkeajrlkeja"


class LoginForm(FlaskForm):
    email = StringField(label="email", validators=[Email()])
    password = PasswordField(label="password", validators=[DataRequired()])
    submit = SubmitField(label="Login")


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['POST', 'GET'])
def login():
    login_form = LoginForm()
    login_form.validate_on_submit()
    if login_form.validate_on_submit():
        if login_form.email.data == "admin@gmail.com" and login_form.password.data == "1234":
            return render_template("success.html")
        else:
            return render_template("denied.html")
    print(login_form.errors)

    return render_template("login.html", form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
