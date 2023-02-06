#!/usr/bin/python3
""" starts a Flask web application listening on 0.0.0.0, port 5000"""
from models import storage
from flask import Flask, render_template
from sqlalchemy.sql import text

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """Displays a HTML page with a list of all States.
    """
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """Displays a HTML page with info with info about the id."""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
