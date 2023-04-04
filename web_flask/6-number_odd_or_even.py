#!/usr/bin/python3
"""start a flask web application"""

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """returns “Hello HBNB!” to the user"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ returns “HBNB” to the user"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """returns “C ” followed by the value of the text variable"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False, defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def python_text_default(text):
    """display “Python ”, followed by the value of the text variable"""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """display “n is a number” only if n is an integer"""
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def html_file(n):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', num=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even(n):
    """display a HTML page only if n is an integer"""
    return render_template('6-number_odd_or_even.html', num=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
