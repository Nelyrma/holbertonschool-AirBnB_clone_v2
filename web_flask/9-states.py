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


@app.route('/states/')
@app.route('/states/<id>')
def states(id=None):
    ''' Display states and state '''
    states = storage.all(State)
    if id is not None:
        id = 'State.' + id
    return render_template('9-states.html', states=states, id=id)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
