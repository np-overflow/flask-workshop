import json

from flask import Flask, redirect, url_for, request, render_template, make_response

app = Flask(__name__)

with open("db.json", "r") as file:
    db = json.load(file)


@app.route('/', methods=["GET", "POST"])  # #methods=['GET', 'POST'])
def home():
    ## TODO: POST scores
    if request.method == "GET":
        return render_template('index.html')  # GET request
    if request.method == "POST":
        return json.dumps({})

@app.route('/leaderboard')
def leaderboard():
    ## TODO: Get scores
    return render_template('leaderboard.html')


if __name__ == "__main__":
    app.run(debug=True)

    with open("db.json", "w") as file:
        file.write(json.dumps(db))
