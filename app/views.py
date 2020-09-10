from flask import render_template
from app import app

#views
@app.route('/')
def index():
    '''
    function that returns the index page and its data
    '''
    message = 'Home'
    return render_template('index.html', message = message)

