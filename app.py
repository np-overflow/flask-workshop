import json
import random
import atexit
from random import choices

from flask import Flask, redirect, url_for, request, render_template, make_response

app = Flask(__name__)

with open("database.json", "r") as file:
    db = json.load(file)

def save_db():
    with open("database.json", "w") as file:
        file.write(json.dumps(db, indent=2))

atexit.register(save_db)

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

def find_choice(choice_id):
    if not db:
        raise Exception("Database not initialized yet")
    for choice in db["choices"]:
        print(choice)
        if choice["id"] == choice_id:
            return choice
    else:
        return None # we don't want to raise an exception here and crash the server.

@app.route('/', methods=["GET", "POST"])  # #methods=['GET', 'POST'])
def home():
    ## TODO: POST scores
    if request.method == "GET":
        choices = get_random_choices()
        return render_template('index.html', choices=choices)  # GET request
    if request.method == "POST":
        print(request.json)
        choice = find_choice(request.json["choice"])
        if not choice:
            return "Invalid choice", 400
        choice["votes"] += 1
        save_db()
        return "Success", 200

@app.route('/leaderboard')
def leaderboard():
    ## TODO: Get scores
    return render_template('leaderboard.html')


if __name__ == "__main__":
    app.run(debug=True)