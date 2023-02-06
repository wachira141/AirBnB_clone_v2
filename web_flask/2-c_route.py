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
    return "C {}".format(text)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
