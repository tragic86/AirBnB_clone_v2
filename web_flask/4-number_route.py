#!/usr/bin/python3
"""script to start flask with c & py"""

from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb')
def holberton():
    return 'HBNB'


@app.route('/c/<text>')
def texy(text):
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/python', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python_texy(text):
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route('/number/<int:n>')
def numbers(n):
        return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
