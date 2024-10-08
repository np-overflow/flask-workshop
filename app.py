import json
import random

from flask import Flask, redirect, url_for, request, render_template, make_response

app = Flask(__name__)

with open("database.example.json", "r") as file:
    db = json.load(file)

def get_random_topic():
    if not db:
        raise Exception("Database not initialized yet")
    return random.choice(db["topics"])

@app.route('/', methods=["GET", "POST"])  # #methods=['GET', 'POST'])
def home():
    ## TODO: POST scores
    if request.method == "GET":
        topic = get_random_topic()
        return render_template('index.html', topic=topic)  # GET request
    if request.method == "POST":
        return json.dumps({})

@app.route('/leaderboard')
def leaderboard():
    ## TODO: Get scores
    return render_template('leaderboard.html')


if __name__ == "__main__":
    app.run(debug=True)

    # app.run is thread blocking and hence, the following code will only run on exit.
    with open("database.example.json", "w") as file:
        file.write(json.dumps(db, indent=2))
