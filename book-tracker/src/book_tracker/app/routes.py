from flask import render_template

from book_tracker.app import app
from book_tracker.app.variables import user, books

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home', user=user, books=books)