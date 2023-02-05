#!/usr/bin/python3
"""
This script starts Flask web application.
listens on 0.0.0.0 port 5000
"""
from flask import Flask, url_for
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Displays 'Hello HBNB'"""
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Displays 'HBNB'"""
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def text(text):
    """Displays C followed by <text>"""
    text = text.replace("_", " ")
    return 'C {}'.format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_txt(text="is cool"):
    """Displays Python followed by <text>"""
    text = text.replace("_", " ")
    return 'Python {}'.format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def print_num(n):
    """Displays 'n is a number' if n is int"""
    return '{} is a number'.format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
