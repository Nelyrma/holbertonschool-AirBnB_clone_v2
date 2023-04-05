#!/usr/bin/python3
"""start a flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/cities_by_states', strict_slashes = False)
def all_cities_by_states():
    """list cities by states"""
    cities_list = storage.all(State)
    return render_template('8-cities_by_states.html', cities_list=cities_list)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
