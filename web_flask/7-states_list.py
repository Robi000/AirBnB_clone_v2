#!/usr/bin/python3

"""
starts a Flask web application
"""


from models import storage
from models.state import State
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def even_or_odd():
    print(storage.all(State))

    x = storage.all(State)
    statex = []
    for x, y in x.items():
        statex.append([y.to_dict()["id"], y.to_dict()["name"]])

    print(statex)
    return render_template("7-states_list.html", States=statex)
    # return storage.all(State)[
    #     'State.421a55f4-7d82-47d9-b54c-a76916479545'].to_dict()["name"]


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
