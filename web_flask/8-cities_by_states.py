#!/usr/bin/python3
''' Start a Flask web aplication '''
from flask import Flask, abort, render_template
from models import storage
from models.state import State
# from models.city import City

app = Flask(__name__)
# replace 'strict_slashes = False' in every route definition
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def run_all_states_and_cities():
    ''' Display all cities by states '''
    city_list = storage.all(State)
    return render_template('8-cities_by_states.html', city_list=city_list)


@app.teardown_appcontext
def do_teardown(self):
    ''' Remove the current SQLAlchemy Session '''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
