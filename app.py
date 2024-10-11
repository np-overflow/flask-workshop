import json
import random

from flask import Flask, redirect, url_for, request, render_template, make_response

app = Flask(__name__)

with open("database.json", "r") as file:
    db = json.load(file)

def get_random_choices():
    if not db:
        raise Exception("Database not initialized yet")
    if len(db["choices"]) < 2:
        raise Exception("Please add more than 2 choices")
    choice1 = random.choice(db["choices"])
    choice2 = random.choice(db["choices"])
    while choice2 == choice1:
        choice2 = random.choice(db["choices"])
    return choice1, choice2

@app.route('/', methods=["GET", "POST"])  # #methods=['GET', 'POST'])
def home():
    ## TODO: POST scores
    if request.method == "GET":
        choices = get_random_choices()
        return render_template('index.html', choices=choices)  # GET request
    if request.method == "POST":
        return json.dumps({})

@app.route('/leaderboard')
def leaderboard():
    ## TODO: Get scores
    return render_template('leaderboard.html')


if __name__ == "__main__":
    app.run(debug=True)

    # app.run is thread blocking and hence, the following code will only run on exit.
    with open("database.json", "w") as file:
        file.write(json.dumps(db, indent=2))
