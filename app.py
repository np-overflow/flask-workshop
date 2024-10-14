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
    pass

def find_choice(choice_id):
    pass

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

