#!/usr/bin/python3
"""Start web application with two routings
"""

from models import storage
from models.state import State
from models.city import City
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """Render template with states
    """
    states = storage.all(State).values()
    states = sorted(states, key=lambda x: x.name)
    return render_template('9-states.html', states=states)

@app.route('/states/<id>', strict_slashes=False)
def state(id):
    """Render template with state id
    """
    state = storage.get(State, id)
    if state:
        cities = state.cities
        cities = sorted(cities, key=lambda x: x.name)
        return render_template('9-states.html', state=state, cities=cities)
    else:
        return render_template('9-states.html', state=None), 404


@app.teardown_appcontext
def app_teardown(arg=None):
    """Clean-up session
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
