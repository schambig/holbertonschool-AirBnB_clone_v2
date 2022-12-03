#!/usr/bin/python3
''' Start a Flask web application '''
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity

app = Flask(__name__)
# replace 'strict_slashes = False' in every route definition
app.url_map.strict_slashes = False


@app.route('/hbnb_filters')
def display_dropdown():
    ''' Display header, footer and a filters box with dropdown '''
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


@app.teardown_appcontext
def teardown(self):
    ''' Remove the current SQLAlchemy Session '''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
