#!/usr/bin/python3
''' Flask web aplication '''
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def view():
    ''' return this message to the user '''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def view_hbnb():
    ''' return this 'hbnb' to the user '''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def variable_text(text):
    ''' return 'C' followed by the value of text '''
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False, defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def variable_text_default(text):
    '''
    Display 'Python' followed by the value of text
    '''
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def only_int(n):
    ''' Display `n is a number` only if n is int '''
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def html_file(n):
    ''' Display a html page only if n in an integer '''
    return render_template('5-number.html', num=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
