#!/usr/bin/python3
"""Start web application with two routings
"""

from models import storage
from models.state import State
from models.city import City
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states')
def states():
    """Render template with states
    """
    states = storage.all(State).values()
    states = sorted(states, key=lambda x: x.name)
    return render_template('9-states.html', states=states)

@app.route('/states/<id>')
def state(id):
    """Render template with state id
    """
    state = storage.get(State, id)
    if state:
        cities = storage.all(City).values()
        cities = [city for city in cities if city.state_id == state.id]
        cities = sorted(cities, key=lambda x: x.name)
        return render_template('9-state.html', state=state, cities=cities)
    else:
        return render_template('9-not-found.html'), 404


@app.teardown_appcontext
def app_teardown(arg=None):
    """Clean-up session
    """
    storage.close()


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
