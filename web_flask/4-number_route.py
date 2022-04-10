#!/usr/bin/python3
"""
starts a Flask web application
"""

from os import abort
from flask import Flask
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
    """ this will show the database and give what asked """
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
    """ this will show the database and give what asked """
    meh = ""
    for x in text:
        if x != '_':
            meh = meh + x
        else:
            meh = meh + " "
    return ("Python {}".format(meh))


@app.route('/number/<int:n>', strict_slashes=False)
def int_or_not(n=None):
    """ this will show the database and give what asked """
    return ("{} is a number".format(n))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
