from flask import Flask
from flask import render_template
from flask import request
import model

app = Flask(__name__)


@app.route('/')
@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

def headsetchoice(answer):
    if answer == "PC":
        return "artics1"
    elif answer == "Playstation4":
        return "Logitech G Pro"
    elif answer == "XboxOne":
        return "razerkraken"
    elif answer == "Phone":
        return "TurtleBeach550"
    elif answer == "Nintendo Switch":
        return "Cloud Alpha"

@app.route('/results', methods = ['GET', 'POST'])
def results():
    headset = request.form["platform"]
    headset_name = headsetchoice(headset)
    print(headset)
    return render_template('results.html', headset = headset, headset_name = headset_name)

