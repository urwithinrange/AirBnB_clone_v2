#!/usr/bin/python3
"""start a Flask web application"""

from flask import Flask
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def td_app(exception=None):
    """
    After each request
    remove the current SQLAlchemy Session
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """display a HTML page"""
    states = list(storage.all('State').values())
    st_list = []
    for k, v in states:
        st_list.append((parse_id(k), v.name))
    st_list.sort(key=lambda tup: tup[0])
    return render_template("7-states_list.html", state_dict=result)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
