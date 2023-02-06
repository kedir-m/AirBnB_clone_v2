#!/usr/bin/python3
""" starts a Flask web application: """
from unicodedata import name
from flask import Flask, render_template
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


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text='is cool'):
    """Displays “Python” followed by the value of the text"""
    text = escape(text.replace('_', ' '))
    return 'Python {}'.format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def check_number(n):
    """Display “n is a number” only if n is an integer"""
    return '{} is a number'.format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Display a HTML page only if n is an integer"""
    return render_template('5-number.html', name=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """Display a HTML page only if n is an integer"""
    return render_template('6-number_odd_or_even.html', number=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")