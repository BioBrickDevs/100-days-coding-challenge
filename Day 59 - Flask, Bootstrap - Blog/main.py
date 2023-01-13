from flask import Flask, render_template, url_for, request

import requests
app = Flask(__name__)

@app.route("/")
def index():
    response = requests.get("https://api.npoint.io/822589dc28ac41dfd5f0")
    posts =response.json()
    
    return render_template("index.html", posts=posts)



@app.route("/about/")
def about():
    return render_template("about.html")


@app.route("/contact/")
def contact():
    return render_template("contact.html")



@app.route("/posts/<int:id>")
def posts(id):
    response = requests.get("https://api.npoint.io/822589dc28ac41dfd5f0")
    post =response.json()[id-1]
    print(post)
    return render_template("post.html",post=post)

if __name__ == "__main__":

    app.run(debug=True)