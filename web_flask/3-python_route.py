#!/usr/bin/python3
"""
starts a Flask web application
"""

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
    print("=> {}".format(type(text)))
    meh = ""
    for x in text:
        if x != '_':
            meh = meh + x
        else:
            meh = meh + " "

    return ("Python {}".format(meh))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
