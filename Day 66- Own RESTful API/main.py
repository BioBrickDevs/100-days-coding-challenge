from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random", methods=["GET"])
def random():

    random_cafe = Cafe.query.order_by(db.func.random()).first()
    random_cafe = dict(random_cafe.__dict__)
    del random_cafe["_sa_instance_state"]
    return jsonify(cafe=random_cafe)


@app.route("/all", methods=["GET"])
def all():

    cafes = {"cafes": []}
    all_cafes = db.session.query(Cafe).all()
    for cafe in all_cafes:
        cafe = dict(cafe.__dict__)
        del cafe["_sa_instance_state"]
        cafes["cafes"].append(cafe)
    return jsonify(cafes)


@app.route("/search")
def location():
    query_location = request.args.get("loc")

    search_result = Cafe.query.filter_by(location=query_location).all()

    # print(loc)
    if len(search_result) > 1:
        cafes = {"cafes": []}
    elif len(search_result) == 0:
        error_message = {
            "error": {"Not Found": "Sorry, we don't have a cafe at that location."}}
        return jsonify(error_message)
    else:
        cafes = {"cafe": []}

    all_cafes = search_result
    for cafe in all_cafes:
        cafe = dict(cafe.__dict__)
        del cafe["_sa_instance_state"]
        cafes["cafes"].append(cafe)

    return jsonify(cafes)


@app.route("/add", methods=["POST"])
def add():
    new_cafe = Cafe(
        name=request.form["name"],
        map_url=request.form["map_url"],
        img_url=request.form["img_url"],
        location=request.form["location"],
        seats=request.form["seats"],
        has_toilet=bool(request.form["has_toilet"]),
        has_wifi=bool(request.form["has_wifi"]),
        has_sockets=bool(request.form["has_sockets"]),
        can_take_calls=bool(request.form["can_take_calls"]),
        coffee_price=request.form["coffee_price"]
    )
    try:
        db.session.add(new_cafe)
        db.session.commit()
        message = {"response": {
            "success": "Succesfully added the new cafe."
        }}
        return jsonify(message)
    except:
        message = {"response": {
            "Error": """Either Cafe already exits or your parameters have some wrong syntax.
                    All must be filled"""
        }
        }
        return jsonify(message)


@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update(cafe_id):

    cafe_to_update = Cafe.query.get(cafe_id)

    if cafe_to_update:
        try:
            cafe_to_update.price = request.form["new_price"]
        except:
            message = {"error": "Invalid parameter"}
            return jsonify(message), 404

        db.session.commit()
        message = {
            "success": "Succesfully updated the price."
        }
        return jsonify(message), 200
    else:
        message = {"error": {
            "Not Found": "Sorry a cafe with that id was not found in the database."
        }}
        return jsonify(message), 404


@app.route("/report-closed/<cafe_id>", methods=["DELETE"])
def delete(cafe_id):
    try:
        submited_api_key = request.args.get("api-key")
        print(submited_api_key)
    except:
        return "invalid parameter"

    api_key = "TopSecretAPIKey"
    if submited_api_key == api_key:
        cafe_to_delete = Cafe.query.get(cafe_id)
        if cafe_to_delete:
            db.session.delete(cafe_to_delete)
            db.session.commit()
            message = {"success": {"message": "The cafe was succesfully deleted from the database"

                                   }
                       }
            return jsonify(message), 200
        else:
            message = {
                "error": "No Cafe found in the database. Cannot delete"
            }
            return jsonify(message), 403

    else:
        message = {
            "error": "Sorry, that's not allowed. Make sure you have the correct api_key."}
        return jsonify(message), 401


if __name__ == '__main__':
    app.run(debug=True)
