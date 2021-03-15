from flask import render_template, request, redirect
from app import app
from app.models.game import game
from app.models.player import Player

@app.route('/rock')
def index():
    return render_template('index.html', title = 'Rock, Paper Scissors', game=game)