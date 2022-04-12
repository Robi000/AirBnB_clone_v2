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
    return 'C {}'.format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
