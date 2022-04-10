#!/usr/bin/python3
"""
starts a Flask web application
"""


from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """returns HBNB"""
    return 'HBNB'


@app.route('/c/<text>')
def with_input(text):
    # show the subpath after /path/
    meh = ""
    for x in text:
        if x != '_':
            meh = meh + x
        else:
            meh = meh + " "
    return 'C {}'.format(meh)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>')
def either_or(text="is cool"):
    meh = ""
    for x in text:
        if x != '_':
            meh = meh + x
        else:
            meh = meh + " "
    return ("Python {}".format(meh))


@app.route('/number/<int:n>', strict_slashes=False)
def int_or_not(n=None):
    return ("{} is a number".format(n))


@app.route('/number_template/<int:n>', strict_slashes=False)
def render_index(n=None):
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def even_or_odd(n=None):
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
