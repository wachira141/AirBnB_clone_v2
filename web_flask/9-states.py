#!/usr/bin/python3
"""script to spinup a Flask web application"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """return all states instance"""
    states = [state for state in storage.all('States').values()]
    return render_template('9-states.html', states=states)


@app.route('/states<id>',strict_slashes=False )
def getSingleState(id):
    """method to get a single state by id"""
    state = None
    for st in storage.all('State').values:
        if st.id == id:
            state = st
    return render_template('9-states.html', state=state)



@app.teardown_appcontext
def tearDown():
    """ter down method"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
