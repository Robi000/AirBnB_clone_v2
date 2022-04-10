#!/usr/bin/python3

"""
starts a Flask web application
"""

from contextlib import redirect_stderr
from models import storage
from models import city
from models.state import State
from models.city import City
from operator import itemgetter
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def state_listt():
    print(storage.all(State))

    x = storage.all(State)
    statex = []
    for x, y in x.items():
        statex.append([y.to_dict()["id"], y.to_dict()["name"]])

    print(statex)
    return render_template("7-states_list.html", States=statex)
    # return storage.all(State)[
    #     'State.421a55f4-7d82-47d9-b54c-a76916479545'].to_dict()["name"]


@app.route('/states/<id>', strict_slashes=False)
def state_list(id):
    def state_city_finder(n):
        final = []
        for x in statex:
            if x[0] == n:
                for y in meh:
                    if y[0] == n:
                        state_city.append([y[1], y[2]])
                final.append([x[0], x[1], state_city])
        return final
    print(storage.all(State))

    x = storage.all(State)
    statex = []
    cityx = []
    state_city = []
    final = []
    for x, y in x.items():
        statex.append([y.to_dict()["id"], y.to_dict()["name"]])
    for x, y in storage.all(City).items():
        cityx.append([y.to_dict()['state_id'], y.to_dict()
                      ["name"], y.to_dict()["id"]])
    meh = sorted(cityx, key=itemgetter(1))
    print("\n*******statexx*******")
    print(statex)
    print("\n*******cityx*******")
    print(cityx)
    print("\n*******meh*******")
    print(meh)
    print("\n*********** final **********")
    try:
        return render_template("h.html.j2", state=state_city_finder(id))
    except:
        return render_template("error.html")


@app.teardown_appcontext
def session(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')


# """
# starts a Flask web application
# """


# from models import storage
# from models.state import State
# from flask import Flask
# from flask import render_template
# app = Flask(__name__)


# @app.route('/states_list', strict_slashes=False)
# def even_or_odd():
#     session()
#     print(storage.all(State)[
#           'State.421a55f4-7d82-47d9-b54c-a76916479545'].to_dict()["name"])
    # return storage.all(State)[
    #     'State.421a55f4-7d82-47d9-b54c-a76916479545'].to_dict()["name"]


# @app.teardown_appcontext
# def session(exception):
#     storage.close()


# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port='5000')
