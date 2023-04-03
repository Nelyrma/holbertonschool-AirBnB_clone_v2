#!/usr/bin/python3
''' Flask web aplication '''
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def view():
    ''' return this message to the user '''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def view_hbnb():
    ''' return this 'hbnb' to the user '''
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
