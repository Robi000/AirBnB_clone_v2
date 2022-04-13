#!/usr/bin/python3
"""
starts a Flask web application
"""

from models import storage
from models.state import State
from models.city import City
from flask import Flask
from flask import render_template
from operator import itemgetter

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_state():
    """ this will show the databas asked """
    print(storage.all(State))

    x = storage.all(State)
    statex = []
    cityx = []
    state_city = []
    final = []
    for x, y in x.items():
        statex.append([y.to_dict()["id"], y.to_dict()["name"]])
    print(
        storage.all(City)
        ['City.521a55f4-7d82-47d9-b54c-a76916479545'].to_dict())
    # print(storage.all(City))
    for x, y in storage.all(City).items():
        cityx.append(
            [y.to_dict()['state_id'],
             y.to_dict()["name"],
             y.to_dict()["id"]])
    meh = sorted(cityx, key=itemgetter(1))

    for x in statex:
        state_city = []

        for y in meh:
            if x[0] == y[0]:
                state_city.append([y[1], y[2]])
                # meh.remove(y)
        final.append([x[0], x[1], state_city])

    print("------ final --------\n\n")
    print(final)

    return render_template("8-cities_by_states.html", States=final)


@app.teardown_appcontext
def session(exception):
    """ this will show the """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
