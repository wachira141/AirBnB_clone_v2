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


if __name__ == "__main__":
    app.run(host="0.0.0.0")
