from flask import Flask
from flask import render_template
from flask import request
import model

app = Flask(__name__)


@app.route('/')
@app.route('/quiz')
def quiz():
    return render_template('quiz.html')

@app.route('/results', methods = ['GET', 'POST'])
def results():
    headset = request.form["platform"]
    genre = request.form["genre"]
    setup = request.form["setup"]
    headset_name = model.headsetchoice(headset, genre, setup)
    return render_template('results.html', headset = headset, headset_name = headset_name, genre = genre, setup = setup)
