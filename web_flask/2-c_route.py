#!/usr/bin/python3
""" starts a Flask web application: """
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def welcome():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'Hello HBNB!'"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """Displays “C ” followed by the value of the text"""
    text_without_underscore = escape(text.replace('_', ' '))
    return 'C {}'.format(text_without_underscore)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
