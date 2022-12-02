#!/usr/bin/python3
''' Start a Flask web aplication '''
from flask import Flask
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def greeting():
    ''' Display a message to the user '''
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# first make sure you installed flask
# also make sure you have created a virtual environment
# also make sure you have activated the venv
## . venv/bin/activate
# run this script from another tab
# change to the virtual enviroment
# to indicate the location of our scr ipt use:
## export FLASK_APP=0-hello_route.py (mac)
## set FLASK_APP=0-hello_route.py (win)
