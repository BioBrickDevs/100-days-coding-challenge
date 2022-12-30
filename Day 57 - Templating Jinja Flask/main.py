from flask import Flask, render_template, url_for
import requests

app = Flask(__name__)


@app.route("/posts/<int:post_id>")
def blog_post(post_id):
    response = requests.get("https://api.npoint.io/8d91184012b990882667")
    data = response.json()

    return render_template("post.html", data=data[post_id])


@app.route("/")
def blog():

    response = requests.get("https://api.npoint.io/8d91184012b990882667")
    data = response.json()


    return render_template("index.html", data= data)


@app.route("/guess/<name>")
def guess(name):
    name = name.title()
    parameters = {
        "name": name
    }
    agify_response = requests.get("https://api.agify.io/", params=parameters)
    agify_data = agify_response.json()
    age_prediction = agify_data["age"]

    gender_response = requests.get(
        "https://api.genderize.io", params=parameters)
    gender_data = gender_response.json()
    sexuality_prediction = gender_data["gender"]

    return render_template("guess.html", name=name, years_old=age_prediction, gender=sexuality_prediction)


app.run(debug=True)
