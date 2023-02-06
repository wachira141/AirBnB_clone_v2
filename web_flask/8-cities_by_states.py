#!/usr/bin/python3
"""script to start a Flask web application"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def tearDown():
    """remove current SQLAlchemy Session"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def list_states():
    """func to list all cities"""
    states = [sts for sts in storage.all("State").values()]
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states', strict_slashes=False)
def citiesByStates():
    statesObj = [state for state in storage.all("States").values()]

    return render_template('8-cities_by_states.html', stateObj=statesObj)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
