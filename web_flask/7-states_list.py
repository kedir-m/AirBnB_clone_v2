#!/usr/bin/python3
""" starts a Flask web application listening on 0.0.0.0, port 5000"""
from models import storage
from flask import Flask, render_template
from sqlalchemy.sql import text

app = Flask(__name__)


@app.route("/states_list/", strict_slashes=False)
def states_list():
    """Display a list of all States"""
    states = storage.all('State')
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
