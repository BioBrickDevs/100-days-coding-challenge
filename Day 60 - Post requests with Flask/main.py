from flask import render_template, Flask, request

app = Flask(__name__)


@app.route("/")
def index():

    return render_template("index.html")


@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        request.form["firstname"]
        request.form["lastname"]

    return request.form["firstname"] + request.form["lastname"]


app.run(debug=True)
