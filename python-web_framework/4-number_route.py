#!/usr/bin/python3
"""
    Script that starts a Flask web application with two routes
"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """Function that returns a simple string"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """Function that returns HBNB string"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_print(text):
    """Function that returns a C string"""
    result = text.replace('_', ' ')
    return "C {}".format(result)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_print(text="is cool"):
    """Function that returns a Python string"""
    result = text.replace('_', ' ')
    return "Python {}".format(result)


@app.route("/number/<int:n>", strict_slashes=False)
def num(n):
    """Function that returns a string only if n is a number"""
    if isinstance(n, int):  # Fix here
        return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
