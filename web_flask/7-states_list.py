#!/usr/bin/python3
"""importing flask and storage"""

from flask import Flask
from flask import render_template
from models import State
from models import storage


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def s_list():
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def tearitdown():
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
