from flask import Flask
from markupsafe import escape
import random

app = Flask(__name__)

random_number = random.randint(1, 10)

@app.route("/")
def high_low_game_start():
    html = """<h1>Guess a number between 1 and 10:</h1>
                <img src="./static/game_start_image.gif"> """

    return html
@app.route("/<int:quess>")
def high_low_game(quess):
    global random_number
    if quess == random_number:
        html = """<h1>That's correct! You guessed right!</h1>
                <img src="./static/right.gif"> """
        random_number = random.randint(1, 10)
    elif quess > random_number:
        html = """<h1>Too high, guess again!</h1>
                <img src="./static/too_high.gif"> """
   
    else:
        html = """<h1>Too low, guess again!</h1>
                <img src="./static/too_low.gif"> """
    
    return html

app.run(debug=True)