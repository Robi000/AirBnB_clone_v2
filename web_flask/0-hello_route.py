from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False
""" this will show the database and give what asked """

@app.route('/')
def hello_world():
    """ this will show the database and give what asked """
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
