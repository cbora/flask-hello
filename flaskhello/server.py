from flaskhello import app

from flask import render_template


@app.route('/')
def index2():
    return render_template('home.html')
