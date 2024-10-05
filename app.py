from flask import Flask, redirect, url_for, request, render_template, make_response

app = Flask(__name__)

@app.route('/')# #methods=['GET', 'POST'])
def index():
    ## TODO: POST scores
    return render_template('index.html') # GET request

@app.route('/leaderboard')
def leaderboard():
    ## TODO: Get scores
    return render_template('leaderboard.html') 

if __name__ == "__main__":
    app.run(debug=True)
