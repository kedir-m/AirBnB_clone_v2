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


if __name__ == "__main__":
    app.run(host="0.0.0.0")
    print(url_for('hbnb'))
