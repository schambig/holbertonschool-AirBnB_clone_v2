#!/usr/bin/python3
''' Start a Flask web aplication '''
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
# replace 'strict_slashes = False' in every route definition
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown(self):
    ''' Remove the current SQLAlchemy Session '''
    storage.close()


@app.route('/states_list')
def states():
    ''' Display the list of states '''
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
