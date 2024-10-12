import json
import random
import atexit

from flask import Flask, request, render_template

app = Flask(__name__)

## INITIALISE DB ##
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


## ROUTING ##
@app.route('/', methods=["GET", "POST"]) #VOTING PAGE
def home():
    if request.method == "GET":
        ## TODO: # GET request
        return render_template()
    
    if request.method == "POST":
        ## TODO: # POST request
        return

@app.route('/leaderboard')
def leaderboard():
    ## TODO: Display leaderboard
    return render_template()


## TODO: RUN APPLICATION

