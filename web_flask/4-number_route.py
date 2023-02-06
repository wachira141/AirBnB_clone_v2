#!/usr/bin/python3
"""script that starts a Flask web app
must listen on 0.0.0.0:5000
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """this route returns Hello HBNB"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """this route returns HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def var_path(text):
    """pass variables to the path"""
    if "_" in text:
        text = text.replace("_", " ")
    return "C %s" % text


@app.route('/python', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def default_var(text='is cool'):
    """var's path with a default value of cool"""
    if "_" in text:
        text = text.replace("_", " ")
    return "Python %s" % text


@app.route('/number/<int:n>', strict_slashes=False)
def is_int(n):
    """run if the n is an int"""
    return "%d is a number" % n


if __name__ == "__main__":
    app.run(host="0.0.0.0")
