#!/usr/bin/python3
"""
script to start an app listening on 0.0.0.0 port 5000

"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_states():
    """func to list all cities"""

    states = [sts for sts in storage.all("State").values()]
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def tearDown():
    """remove current SQLAlchemy session after each request"""
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0")