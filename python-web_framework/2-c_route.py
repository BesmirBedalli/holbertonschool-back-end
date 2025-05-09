#!/usr/bin/python3
"""
    Script that starts a Flask web application with two routes
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """display Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello1():
    """display HBNB"""
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def hello2(text):
    """display C followed by the value of the text variable"""
    text = text.replace("_", " ")
    return "C {}".format(text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
